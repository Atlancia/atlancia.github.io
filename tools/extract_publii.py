#!/usr/bin/env python3
"""Extract a Publii site into a Hugo project.

Reads the Publii desktop site folder (a SQLite content database, a JSON config
and a media tree) and writes a Hugo project: Markdown content, a media
registry, the theme's static assets and a data file describing the site.

The goal is fidelity. The output is checked against the HTML that Publii
currently publishes, so anything the converter cannot express in Markdown is
preserved as raw HTML rather than approximated.

Usage:
    python tools/extract_publii.py --site <publii sites dir> --out <hugo dir>
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import sqlite3
import sys
from dataclasses import dataclass, field
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))

import make_logo_variant  # noqa: E402
import media_registry  # noqa: E402

# Publii responsive image variants, in the order the theme emits them.
RESPONSIVE_WIDTHS: list[tuple[str, int]] = [
    ("xs", 640),
    ("sm", 768),
    ("md", 1024),
    ("lg", 1366),
    ("xl", 1600),
    ("2xl", 1920),
]

# Classes that carry meaning in the published theme. Everything else is an
# editor artefact from Publii's WYSIWYG editor and is dropped.
KEEP_CLASSES = {
    "post__image",
    "post__image--center",
    "post__image--wide",
    "post__image--full",
    "align-left",
    "align-right",
    "align-center",
    "align-justify",
}

VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

# Tags whose children are emitted as raw HTML rather than Markdown.
RAW_TAGS = {"figure", "picture", "svg", "video", "audio", "iframe", "table"}

DROP_ATTRS = {
    "id", "data-selectable-paragraph", "data-path-to-node",
    "data-index-in-node", "contenteditable", "data-testid",
    "data-is-external-image", "style",
}


# --------------------------------------------------------------------------- #
# HTML tree
# --------------------------------------------------------------------------- #

@dataclass
class Node:
    tag: str
    attrs: dict[str, str] = field(default_factory=dict)
    children: list[Any] = field(default_factory=list)  # Node | str
    parent: "Node | None" = None

    @property
    def is_text(self) -> bool:
        return isinstance(self, str)

    def iter_elements(self) -> Iterable["Node"]:
        for child in self.children:
            if isinstance(child, Node):
                yield child
                yield from child.iter_elements()


class TreeBuilder(HTMLParser):
    """Builds a forgiving tree from Publii's editor HTML."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node(tag="#root")
        self.stack = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        node = Node(tag=tag.lower(), attrs={k: (v or "") for k, v in attrs})
        node.parent = self.stack[-1]
        self.stack[-1].children.append(node)
        if tag.lower() not in VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        node = Node(tag=tag.lower(), attrs={k: (v or "") for k, v in attrs})
        node.parent = self.stack[-1]
        self.stack[-1].children.append(node)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data: str) -> None:
        self.stack[-1].children.append(data)


def parse_html(source: str) -> Node:
    builder = TreeBuilder()
    builder.feed(source)
    builder.close()
    return builder.root


# --------------------------------------------------------------------------- #
# Markdown emission
# --------------------------------------------------------------------------- #

ESCAPE_RE = re.compile(r"([\\`*_\[\]])")


def escape_text(text: str) -> str:
    return ESCAPE_RE.sub(r"\\\1", text)


def clean_attrs(attrs: dict[str, str]) -> dict[str, str]:
    """Drop editor artefacts, keep everything else.

    Raw HTML blocks are copied through to the Markdown file, so their classes
    are preserved even though none of the paste artefacts are styled.
    """
    out: dict[str, str] = {}
    for key, value in attrs.items():
        lowered = key.lower()
        if lowered in DROP_ATTRS:
            continue
        out[key] = value
    return out


def render_attrs(attrs: dict[str, str]) -> str:
    parts = []
    for key, value in attrs.items():
        parts.append(f'{key}="{html.escape(value, quote=True)}"')
    return ("" if not parts else " " + " ".join(parts))


def node_to_html(node: Node) -> str:
    """Serialise a node back to HTML, preserving only meaningful attributes."""
    attrs = clean_attrs(node.attrs)
    inner = "".join(
        node_to_html(child) if isinstance(child, Node) else html.escape(child, quote=False)
        for child in node.children
    )
    if node.tag in VOID_TAGS:
        return f"<{node.tag}{render_attrs(attrs)}>"
    return f"<{node.tag}{render_attrs(attrs)}>{inner}</{node.tag}>"


def inline_to_markdown(nodes: list[Any]) -> str:
    out: list[str] = []
    for child in nodes:
        if isinstance(child, str):
            out.append(escape_text(child))
            continue
        tag = child.tag
        if tag == "br":
            out.append("  \n")
        elif tag in ("strong", "b"):
            inner = inline_to_markdown(child.children)
            if inner != inner.strip():
                # Markdown cannot close a marker that is followed by a space,
                # so the element is kept as markup instead.
                out.append(f"<{tag}>{inner}</{tag}>")
            else:
                out.append(f"**{inner}**")
        elif tag in ("em", "i"):
            inner = inline_to_markdown(child.children)
            if inner != inner.strip():
                out.append(f"<{tag}>{inner}</{tag}>")
            else:
                out.append(f"*{inner}*")
        elif tag == "code":
            out.append(f"`{''.join(c for c in child.children if isinstance(c, str))}`")
        elif tag == "a":
            label = inline_to_markdown(child.children).strip()
            href = child.attrs.get("href", "")
            title = child.attrs.get("title", "")
            suffix = f' "{title}"' if title else ""
            out.append(f"[{label}]({href}{suffix})")
        elif tag == "img":
            alt = child.attrs.get("alt", "")
            src = child.attrs.get("src", "")
            title = child.attrs.get("title", "")
            suffix = f' "{title}"' if title else ""
            out.append(f"![{alt}]({src}{suffix})")
        elif tag in ("sup", "sub"):
            inner = inline_to_markdown(child.children)
            out.append(f"<{tag}>{inner}</{tag}>")
        elif tag in RAW_TAGS:
            out.append(node_to_html(child))
        else:
            out.append(inline_to_markdown(child.children))
    return "".join(out)


def contains_block(node: Node) -> bool:
    for element in node.iter_elements():
        if element.tag in ("div", "figure", "picture", "ul", "ol", "blockquote", "h1",
                           "h2", "h3", "h4", "h5", "h6", "p", "table", "hr", "pre"):
            return True
    return False


def node_text(node: Node) -> str:
    parts: list[str] = []
    for child in node.children:
        if isinstance(child, str):
            parts.append(child)
        else:
            parts.append(node_text(child))
    return "".join(parts)


def figure_to_markdown(node: Node) -> tuple[str, bool] | None:
    """Turn a figure holding one image and an optional caption into Markdown.

    The published theme styles a captioned image as a figure and an
    uncaptioned one as a bare centred image, so the distinction has to survive
    the conversion. The caption becomes the Markdown image title.

    A figure that did not carry the class itself, with the class on the image
    inside it, was published with a figure nested inside a figure. That shape
    is recorded so the templates can reproduce it.
    """
    images = [c for c in node.children if isinstance(c, Node) and c.tag == "img"]
    captions = [c for c in node.children if isinstance(c, Node) and c.tag == "figcaption"]
    others = [c for c in node.children if isinstance(c, Node) and c.tag not in ("img", "figcaption")]
    stray_text = [c for c in node.children if isinstance(c, str) and c.strip()]
    if len(images) != 1 or others or stray_text or len(captions) > 1:
        return None
    image = images[0]
    src = image.attrs.get("src", "")
    alt = image.attrs.get("alt", "")
    title = ""
    if captions:
        title = re.sub(r"\s+", " ", node_text(captions[0])).strip()
    suffix = f' "{title}"' if title else ""
    figure_classes = node.attrs.get("class", "").split()
    nested = "post__image" not in figure_classes and "post__image" in image.attrs.get("class", "").split()
    return f"![{alt}]({src}{suffix})", (src if nested else "")


LIST_MARKER_RE = re.compile(r"^([-*+]|\d+\.)\s")


def escape_leading_marker(text: str) -> str:
    """Keep a paragraph that starts with a dash or a number from becoming a list.

    A line that begins with "- " is a list in Markdown, and one essay quotes a
    source that way inside a block quotation.
    """
    if LIST_MARKER_RE.match(text):
        return "\\" + text
    return text


def blocks_to_markdown(nodes: list[Any], nested: list[str] | None = None) -> str:
    blocks: list[str] = []

    def add(text: str) -> None:
        text = text.strip()
        if text:
            blocks.append(text)

    def walk(children: list[Any]) -> None:
        for child in children:
            if isinstance(child, str):
                stripped = child.strip()
                if stripped:
                    add(escape_text(stripped))
                continue
            tag = child.tag
            if tag == "p":
                if contains_block(child):
                    walk(child.children)
                else:
                    text = inline_to_markdown(child.children)
                    if text and not text.strip():
                        # A paragraph holding only a blank was published as an
                        # empty line with its spacing.
                        add("<p>&nbsp;</p>")
                    else:
                        add(escape_leading_marker(text))
            elif tag == "div":
                # Publii wraps some blocks in unstyled layout divs. Unwrap them
                # so the Markdown stays readable; the published layout is
                # unaffected because those classes carry no CSS.
                walk(child.children)
            elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                level = max(2, int(tag[1]))
                add("#" * level + " " + inline_to_markdown(child.children).strip())
            elif tag in ("ul", "ol"):
                add(render_list(child))
            elif tag == "blockquote":
                inner = blocks_to_markdown(child.children, nested)
                quoted = "\n".join(("> " + line) if line else ">" for line in inner.split("\n"))
                add(quoted)
            elif tag == "figure":
                converted = figure_to_markdown(child)
                if converted is None:
                    add(node_to_html(child))
                else:
                    markdown, nested_source = converted
                    if nested_source and nested is not None:
                        nested.append(nested_source)
                    add(markdown)
            elif tag == "img":
                add(inline_to_markdown([child]))
            elif tag in RAW_TAGS:
                add(node_to_html(child))
            elif tag == "hr":
                add("---")
            elif tag == "pre":
                add(node_to_html(child))
            else:
                walk(child.children)

    walk(nodes)
    return "\n\n".join(blocks)


def render_list(node: Node) -> str:
    ordered = node.tag == "ol"
    lines: list[str] = []
    for index, item in enumerate([c for c in node.children if isinstance(c, Node) and c.tag == "li"], 1):
        marker = f"{index}." if ordered else "-"
        inner_nodes = [c for c in item.children if not (isinstance(c, str) and not c.strip())]
        if any(isinstance(c, Node) and c.tag in ("ul", "ol") for c in inner_nodes):
            head: list[Any] = []
            tail: list[Any] = []
            seen_list = False
            for child in inner_nodes:
                if isinstance(child, Node) and child.tag in ("ul", "ol") and not seen_list:
                    seen_list = True
                    tail.append(child)
                elif seen_list:
                    tail.append(child)
                else:
                    head.append(child)
            text = inline_to_markdown(head).strip()
            nested = render_list(tail[0]) if tail else ""
            lines.append(f"{marker} {text}")
            if nested:
                lines.append(nested)
        else:
            lines.append(f"{marker} {inline_to_markdown(inner_nodes).strip()}")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Publii site reading
# --------------------------------------------------------------------------- #

@dataclass
class ImageEntry:
    src: str
    srcset: str = ""
    sizes: str = ""
    width: str = ""
    height: str = ""
    alt: str = ""


class PubliiSite:
    def __init__(self, site_dir: Path) -> None:
        self.site_dir = site_dir
        self.input_dir = site_dir / "input"
        self.config = json.loads((self.input_dir / "config" / "site.config.json").read_text("utf-8"))
        self.theme_config = json.loads(
            (self.input_dir / "config" / "theme.simple.config.json").read_text("utf-8")
        )
        self.plugins = json.loads(
            (self.input_dir / "config" / "site.plugins.json").read_text("utf-8")
        )
        self.db = sqlite3.connect(f"file:{self.input_dir / 'db.sqlite'}?mode=ro", uri=True)
        self.db.row_factory = sqlite3.Row

    # -- content ----------------------------------------------------------- #

    def posts(self) -> list[sqlite3.Row]:
        return list(self.db.execute("SELECT * FROM posts ORDER BY created_at DESC"))

    def additional_data(self, post_id: int) -> dict[str, dict[str, Any]]:
        rows = self.db.execute(
            "SELECT key, value FROM posts_additional_data WHERE post_id = ?", (post_id,)
        ).fetchall()
        out: dict[str, dict[str, Any]] = {}
        for row in rows:
            try:
                out[row["key"]] = json.loads(row["value"])
            except (TypeError, ValueError):
                continue
        return out

    def featured_image(self, post_id: int) -> sqlite3.Row | None:
        row = self.db.execute(
            "SELECT * FROM posts_images WHERE post_id = ? ORDER BY id LIMIT 1", (post_id,)
        ).fetchone()
        return row

    def authors(self) -> list[sqlite3.Row]:
        return list(self.db.execute("SELECT * FROM authors ORDER BY id"))

    def tags(self) -> list[sqlite3.Row]:
        return list(self.db.execute("SELECT * FROM tags ORDER BY id"))

    def posts_with_tag(self, tag_id: int) -> int:
        row = self.db.execute(
            "SELECT COUNT(*) AS n FROM posts_tags WHERE tag_id = ?", (tag_id,)
        ).fetchone()
        return int(row["n"]) if row else 0

    def close(self) -> None:
        self.db.close()


# --------------------------------------------------------------------------- #
# Media
# --------------------------------------------------------------------------- #

def image_dimensions(path: Path) -> tuple[int, int]:
    try:
        from PIL import Image  # type: ignore

        with Image.open(path) as image:
            return image.size
    except Exception:
        return (0, 0)


def build_media_registry(site: PubliiSite) -> dict[str, Any]:
    """Map every image file to the attributes the theme publishes it with."""
    return media_registry.build(site.input_dir / "media")


def copy_media(site: PubliiSite, out_dir: Path) -> None:
    source = site.input_dir / "media"
    target = out_dir / "static" / "media"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)
    # The wordmark is white, so the light mode needs a dark version of it.
    make_logo_variant.build_variant(
        target / "website" / "logo-2.png", target / "website" / "logo-2-dark.png"
    )


def strip_visual_override(css: str) -> str:
    """Remove the background colour the old theme forced on every page.

    The Publii theme compiled its override into the stylesheet, so the colour
    was set with !important on the root element, on the html element and on
    the body. Those rules would win over any colour scheme, so they come out
    and the palette lives in the templates instead.
    """
    def replace(match: re.Match[str]) -> str:
        body = match.group(2)
        if "!important" in body and "#23233d" in body and ("--page-bg" in body or "background" in body):
            return ""
        return match.group(0)

    return re.sub(r"([^{}]+)\{([^{}]*)\}", replace, css)


def copy_theme_assets(site: PubliiSite, out_dir: Path) -> None:
    theme_dir = site.input_dir / "themes" / "simple"
    assets = theme_dir / "assets"

    css_target = out_dir / "static" / "assets" / "css"
    css_target.mkdir(parents=True, exist_ok=True)
    for name in ("style.css", "main.css", "editor.css"):
        source = assets / "css" / name
        if not source.is_file():
            continue
        if name == "style.css":
            (css_target / name).write_text(
                strip_visual_override(source.read_text(encoding="utf-8")), encoding="utf-8"
            )
        else:
            shutil.copy2(source, css_target / name)

    for folder in ("js", "svg"):
        source = assets / folder
        if source.is_dir():
            target = out_dir / "static" / "assets" / folder
            target.mkdir(parents=True, exist_ok=True)
            for item in source.iterdir():
                if item.is_file():
                    shutil.copy2(item, target / item.name)

    custom = site.theme_config.get("customConfig", {})
    font = custom.get("fontBody", "")
    if font and font != "system-ui":
        source = assets / "dynamic" / "fonts" / font
        if source.is_dir():
            target = out_dir / "static" / "assets" / "dynamic" / "fonts" / font
            target.mkdir(parents=True, exist_ok=True)
            for item in source.iterdir():
                if item.is_file():
                    shutil.copy2(item, target / item.name)


# --------------------------------------------------------------------------- #
# Emission
# --------------------------------------------------------------------------- #

def yaml_scalar(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


SITE_ZONE = ZoneInfo("America/Toronto")


def iso_timestamp(milliseconds: int) -> str:
    """Format a timestamp the way the editor and the theme read dates.

    The published site showed its dates in the site's own time zone, so the
    timestamps are written with that offset rather than in UTC.
    """
    moment = datetime.fromtimestamp(milliseconds / 1000, SITE_ZONE)
    return moment.strftime("%Y-%m-%dT%H:%M:%S%z")[:-2] + ":" + moment.strftime("%z")[-2:]


# The theme stores date formats the way the editor writes them. Go needs its
# own layout language, so the format is translated once, here.
DATE_TOKENS = {
    "YYYY": "2006",
    "MMMM": "January",
    "MMM": "Jan",
    "MM": "01",
    "DD": "02",
    "HH": "15",
    "hh": "03",
    "mm": "04",
    "ss": "05",
    "YY": "06",
    "M": "1",
    "D": "2",
    "A": "PM",
    "a": "pm",
}
DATE_TOKEN_RE = re.compile("|".join(sorted(DATE_TOKENS, key=len, reverse=True)))


def to_go_layout(value: str) -> str:
    return DATE_TOKEN_RE.sub(lambda match: DATE_TOKENS[match.group(0)], value)


def write_post(
    out_dir: Path,
    site: PubliiSite,
    post: sqlite3.Row,
    media_id: int,
    featured: ImageEntry | None,
) -> list[str]:
    slug = post["slug"]
    created = post["created_at"] / 1000
    modified = post["modified_at"] / 1000
    flags = [f.strip() for f in (post["status"] or "").split(",") if f.strip()]

    body = (post["text"] or "").replace("#DOMAIN_NAME#", "")
    tree = parse_html(body)
    nested_sources: list[str] = []
    markdown = blocks_to_markdown(tree.children, nested_sources)

    # The images in the body are named by their file name. The render hook
    # resolves them against the post's own media folder.
    markdown = markdown

    extra = site.additional_data(post["id"])
    core = extra.get("_core", {})

    front: list[str] = [
        "---",
        f"title: {yaml_scalar(post['title'])}",
        f"date: {yaml_scalar(iso_timestamp(post['created_at']))}",
        f"lastmod: {yaml_scalar(iso_timestamp(post['modified_at']))}",
        f"slug: {yaml_scalar(slug)}",
        "type: posts",
        "layout: posts/single",
        f"media_id: {media_id}",
        'authors: ["liam"]',
    ]
    if "hidden" in flags:
        front.append("hidden: true")
    if "excluded_homepage" in flags:
        front.append("exclude_from_home: true")
    if core.get("metaDesc"):
        front.append(f"description: {yaml_scalar(core['metaDesc'])}")
    if core.get("metaTitle"):
        front.append(f"meta_title: {yaml_scalar(core['metaTitle'])}")
    if core.get("canonicalUrl"):
        front.append(f"canonical_url: {yaml_scalar(core['canonicalUrl'])}")
    if core.get("metaRobots"):
        front.append(f"meta_robots: {yaml_scalar(core['metaRobots'])}")
    if featured and featured.src:
        front.append(f"featured_image: {yaml_scalar(featured.src)}")
        if featured.alt:
            front.append(f"featured_image_alt: {yaml_scalar(featured.alt)}")
    front.append("---")
    front.append("")

    target = out_dir / "content" / "posts" / f"{slug}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(front) + markdown + "\n", encoding="utf-8")
    return [f"media/posts/{media_id}/{source}" for source in nested_sources]


def write_site_data(out_dir: Path, site: PubliiSite, registry: dict[str, Any]) -> None:
    config = site.config
    custom = site.theme_config.get("customConfig", {})
    domain = config.get("domain", "").rstrip("/")

    menus = json.loads((site.input_dir / "config" / "menu.config.json").read_text("utf-8"))
    if isinstance(menus, dict):
        menus = [menus]
    main_menu = []
    for menu in menus:
        if menu.get("position") != "mainMenu":
            continue
        for item in menu.get("items", []):
            if item.get("isHidden"):
                continue
            kind = item.get("type", "")
            link = item.get("link", "")
            if kind == "blogpage":
                url = f"{domain}/" if domain else "/"
            elif kind == "external":
                url = link
            else:
                url = link or "/"
            main_menu.append(
                {
                    "label": item.get("label", ""),
                    "url": url,
                    "target": item.get("target", "_self"),
                    "rel": item.get("rel", ""),
                }
            )

    logo = site.theme_config.get("config", {}).get("logo", "")
    hero = custom.get("uploadHero", "")

    data = {
        "name": config.get("displayName") or config.get("name", "Atlancia"),
        "slug": config.get("name", "atlancia"),
        "description": config.get("description", ""),
        "domain": domain,
        "logo": logo,
        "logo_width": 500,
        "logo_height": 162,
        "favicon": custom.get("faviconUpload", ""),
        "favicon_extension": custom.get("faviconExtension", "image/png"),
        "hero": hero,
        "hero_alt": custom.get("uploadHeroAlt", ""),
        "hero_caption": custom.get("uploadHeroCaption", ""),
        "hero_text": custom.get("textHero", ""),
        "hero_height": custom.get("heightHero", "30vh"),
        "align_hero": custom.get("alignHero", "left"),
        "align_feed": custom.get("alignFeed", "center"),
        "feed_read_more": custom.get("feedtReadMore", True),
        "posts_per_page": site.theme_config.get("config", {}).get("postsPerPage", 5),
        "excerpt_length": site.theme_config.get("config", {}).get("excerptLength", 45),
        "format_date": to_go_layout(custom.get("formatDate", "MMMM D, YYYY")),
        "navbar_height": custom.get("navbarHeight", "6rem"),
        "mobile_menu": custom.get("mobilemenu", "sidebar"),
        "mobile_menu_expandable": custom.get("mobilemenuExpandableSubmenus", True),
        "submenu": custom.get("submenu", "auto"),
        "submenu_width": custom.get("submenuWidth", "240"),
        "back_to_top": custom.get("backToTopButton", True),
        "color_scheme": custom.get("colorScheme", "dark"),
        "primary_color": custom.get("primaryColor", "#D73A42"),
        "primary_dark_color": custom.get("primaryDarkColor", "#FFC074"),
        "page_background": "#23233d",
        "copyright_text": custom.get("copyrightText", ""),
        "menu": main_menu,
        "comments": {
            "provider": "graphcomment",
            "shortname": json.loads(
                (site.input_dir / "config" / "plugins" / "graphComment.json").read_text("utf-8")
            ).get("shortname", ""),
            "wrapper_class": "my-comments-wrapper",
            "inner_class": "my-comments-inner",
            "heading_class": "custom-h2",
            "header": "Comments",
            "fallback": "Please enable JS to use the comments form.",
        },
    }

    (out_dir / "data").mkdir(parents=True, exist_ok=True)
    (out_dir / "data" / "site.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def write_authors_and_tags(out_dir: Path, site: PubliiSite) -> None:
    authors_dir = out_dir / "content" / "authors"
    authors_dir.mkdir(parents=True, exist_ok=True)
    for author in site.authors():
        config = json.loads(author["config"] or "{}")
        term_dir = authors_dir / author["username"]
        term_dir.mkdir(parents=True, exist_ok=True)
        (term_dir / "_index.md").write_text(
            "\n".join(
                [
                    "---",
                    f"title: {yaml_scalar(author['name'])}",
                    f"username: {yaml_scalar(author['username'])}",
                    f"description: {yaml_scalar(config.get('description', ''))}",
                    f"url: \"/authors/{author['username']}/index.html\"",
                    "body_class: author-template",
                    "---",
                    "",
                ]
            ),
            encoding="utf-8",
        )

    # The authors listing was never published, only the individual author pages.
    (authors_dir / "_index.md").write_text(
        "\n".join(
            [
                "---",
                "title: \"Authors\"",
                "build:",
                "  render: never",
                "  list: never",
                "---",
                "",
            ]
        ),
        encoding="utf-8",
    )

    tags_dir = out_dir / "content" / "tags"
    tags_dir.mkdir(parents=True, exist_ok=True)
    (tags_dir / "_index.md").write_text(
        "\n".join(
            [
                "---",
                "title: \"Tags\"",
                "url: \"/tags/index.html\"",
                "body_class: tags-template",
                "---",
                "",
            ]
        ),
        encoding="utf-8",
    )
    for tag in site.tags():
        term_dir = tags_dir / tag["slug"]
        term_dir.mkdir(parents=True, exist_ok=True)
        (term_dir / "_index.md").write_text(
            "\n".join(
                [
                    "---",
                    f"title: {yaml_scalar(tag['name'])}",
                    f"description: {yaml_scalar(tag['description'] or '')}",
                    "---",
                    "",
                ]
            ),
            encoding="utf-8",
        )


def write_home(out_dir: Path, site: PubliiSite) -> None:
    content = out_dir / "content"
    content.mkdir(parents=True, exist_ok=True)
    (content / "_index.md").write_text(
        "\n".join(
            [
                "---",
                "title: \"Atlancia\"",
                "type: home",
                "layout: home",
                "body_class: home-template",
                "---",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (content / "posts").mkdir(parents=True, exist_ok=True)
    (content / "posts" / "_index.md").write_text(
        "\n".join(
            [
                "---",
                "title: \"Posts\"",
                "type: posts",
                "build:",
                "  render: never",
                "  list: always",
                "---",
                "",
            ]
        ),
        encoding="utf-8",
    )


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", required=True, help="Path to the Publii site folder")
    parser.add_argument("--out", required=True, help="Path to the Hugo project folder")
    args = parser.parse_args(argv)

    site_dir = Path(args.site).resolve()
    out_dir = Path(args.out).resolve()
    if not (site_dir / "input" / "db.sqlite").exists():
        print(f"Not a Publii site folder: {site_dir}", file=sys.stderr)
        return 2

    site = PubliiSite(site_dir)
    registry = build_media_registry(site)

    copy_media(site, out_dir)
    copy_theme_assets(site, out_dir)
    write_site_data(out_dir, site, registry)
    write_authors_and_tags(out_dir, site)
    write_home(out_dir, site)

    nested: list[str] = []
    for post in site.posts():
        media_id = int(post["id"])
        featured = None
        image = site.featured_image(post["id"])
        if image and image["url"]:
            rel = f"posts/{media_id}/{image['url']}"
            entry = registry.get(f"media/{rel}") or registry.get(image["url"]) or {}
            featured = ImageEntry(
                src=entry.get("src", f"media/{rel}"),
                srcset=entry.get("srcset", ""),
                sizes=entry.get("sizes", ""),
                width=entry.get("width", ""),
                height=entry.get("height", ""),
                alt=json.loads(image["additional_data"] or "{}").get("alt", ""),
            )
        nested.extend(write_post(out_dir, site, post, media_id, featured))
        print(f"post {post['id']:>3}  {post['slug']}")

    # A few figures were published with a figure nested inside a figure. The
    # templates need to know which ones, so the shape survives the move.
    figures = {path: True for path in sorted(set(nested))}
    (out_dir / "data" / "figures.json").write_text(
        json.dumps(figures, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    site.close()
    print(f"extracted to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
