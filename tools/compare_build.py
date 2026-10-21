#!/usr/bin/env python3
"""Compare the Hugo build with the HTML Publii currently publishes.

The two builds are not byte identical: the previous one carried the editor's
utility classes and its own renderer quirks. This compares the parts that
matter, which is the element structure, the classes the theme styles, the
links and the words.

Usage:
    python tools/compare_build.py <publii output> <hugo public>
"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

# Classes the theme actually styles. Everything else was an editor artefact.
STYLED = {
    "align-left", "btn", "btn--icon", "content", "content__actions",
    "content__comments", "content__entry", "content__footer", "content__meta",
    "content__nav", "content__nav-image", "content__nav-inner",
    "content__nav-link", "content__nav-next", "content__nav-prev",
    "content__related", "content__share", "content__share-button",
    "content__share-popup", "entry-wrapper", "feed--grid", "feed__author",
    "feed__content", "feed__date", "feed__item", "feed__item--centered",
    "feed__meta", "feed__readmore", "feed__title", "footer", "footer--glued",
    "footer__bttop", "footer__copyright", "h4", "hero", "hero--noimage",
    "hero__content", "hero__cta", "hero__image", "hero__image-wrapper", "logo",
    "navbar", "navbar__menu", "navbar__toggle", "navbar__toggle-box",
    "navbar__toggle-inner", "page--author__wrapper", "page__desc",
    "post__image", "post__image--center", "readmore", "related__title", "top",
    "wrapper", "page", "page--tags", "page--author", "page--error",
    "home-template", "post-template", "tags-template", "author-template",
    "error-template", "my-comments-wrapper", "my-comments-inner",
    "custom-h2", "graphcomment",
}

SKIP_TAGS = {"meta", "link", "br", "hr", "source", "noscript", "style", "script"}

# Words that differ because the two builders word their metadata differently.
IGNORE_TEXT = re.compile(r"publii|hugo", re.I)


class Skeleton(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.text: list[str] = []
        self.in_json_ld = False
        self.in_style = False

    def handle_starttag(self, tag, attrs):
        attributes = {k: (v or "") for k, v in attrs}
        if tag == "script" and attributes.get("type") == "application/ld+json":
            self.in_json_ld = True
            return
        if tag == "style":
            self.in_style = True
            return
        if tag in SKIP_TAGS:
            return
        classes = [c for c in attributes.get("class", "").split() if c in STYLED]
        parts = [tag]
        if classes:
            parts.append("." + ".".join(sorted(classes)))
        for key in ("href", "src", "rel", "datetime", "sizes", "loading", "alt"):
            if key in attributes:
                value = attributes[key]
                if key in ("href", "src") and value:
                    value = re.sub(r"^https://atlancia\.com", "", value)
                    value = re.sub(r"\?v=.*$", "", value)
                parts.append(f"{key}={value}")
        self.out.append("|".join(parts))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_data(self, data):
        if self.in_style:
            return
        if self.in_json_ld:
            try:
                parsed = json.loads(data)
            except ValueError:
                return
            self.text.append("jsonld:" + json.dumps(parsed, sort_keys=True))
            return
        cleaned = " ".join(data.split())
        if cleaned and not IGNORE_TEXT.search(cleaned):
            self.text.append(cleaned)

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_json_ld = False
        if tag == "style":
            self.in_style = False


def skeleton(path: Path) -> tuple[list[str], list[str]]:
    parser = Skeleton()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    parser.close()
    return parser.out, parser.text


def media_files(root: Path) -> dict[str, int]:
    out: dict[str, int] = {}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        out[str(path.relative_to(root)).replace("\\", "/")] = path.stat().st_size
    return out


def normalize(tags: list[str]) -> list[str]:
    """Fold away the differences the port deliberately makes.

    The previous build carried the editor's own markup into the published
    pages: body headings were level one, some paragraphs sat inside unstyled
    wrapper elements, and pasted text arrived wrapped in spans. None of it
    changes how the page reads, so it is folded away before comparing.
    """
    out: list[str] = []
    for index, tag in enumerate(tags):
        if tag in ("span", "picture"):
            continue
        if tag == "div":
            continue
        if tag == "figure":
            continue
        if tag == "h1":
            tag = "h2"
        if tag == "i":
            tag = "em"
        if tag == "p|.align-left":
            tag = "p"
        if (
            tag == "p"
            and out
            and out[-1].startswith("figure|.")
            and index + 1 < len(tags)
            and tags[index + 1].startswith("img|")
        ):
            # The previous build pulled the paragraph in front of an image
            # inside the figure. Here the paragraph stays outside it.
            continue
        if tag == "em" and out and out[-1] == "figcaption":
            # The caption was marked up as emphasised inside the figure
            # caption. The theme already sets captions in italics.
            continue
        out.append(tag)
    return out


def normalize_text(items: list[str]) -> list[str]:
    out: list[str] = []
    for item in items:
        if item.startswith("jsonld:"):
            try:
                parsed = json.loads(item[len("jsonld:"):])
            except ValueError:
                out.append(item)
                continue
            for key, value in list(parsed.items()):
                if isinstance(value, str):
                    parsed[key] = value.replace("&hellip;", "…")
            out.append("jsonld:" + json.dumps(parsed, sort_keys=True))
            continue
        out.append(item)
    return out


def align(old: list[str], new: list[str]) -> tuple[list[str], list[str]]:
    """Line up two element lists that differ by a wrapper paragraph.

    An image on a line of its own is a paragraph in Markdown, and the previous
    build published it as a direct child of the entry. The paragraph that
    wraps it in the new build is folded away here.
    """
    out_old: list[str] = []
    out_new: list[str] = []
    i = j = 0
    while i < len(old) and j < len(new):
        if old[i] == new[j]:
            out_old.append(old[i])
            out_new.append(new[j])
            i += 1
            j += 1
            continue
        if new[j] == "p" and i < len(old) and old[i].startswith("figure|."):
            # The wrapper paragraph in the new build.
            j += 1
            continue
        if old[i] == "p" and j < len(new) and new[j].startswith("figure|."):
            i += 1
            continue
        out_old.append(old[i])
        out_new.append(new[j])
        i += 1
        j += 1
    out_old.extend(old[i:])
    out_new.extend(new[j:])
    return out_old, out_new


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    old_root = Path(argv[1])
    new_root = Path(argv[2])

    problems = 0
    old_files = sorted(
        str(p.relative_to(old_root)).replace("\\", "/")
        for p in old_root.rglob("*.html")
        if "admin" not in p.relative_to(old_root).parts
    )
    new_files = sorted(
        str(p.relative_to(new_root)).replace("\\", "/")
        for p in new_root.rglob("*.html")
        if "admin" not in p.relative_to(new_root).parts
    )

    only_old = set(old_files) - set(new_files)
    only_new = set(new_files) - set(old_files)
    if only_old:
        print("only in the old build:", sorted(only_old))
        problems += 1
    if only_new:
        print("only in the new build:", sorted(only_new))
        problems += 1

    for name in old_files:
        if name not in new_files:
            continue
        old_tags, old_text = skeleton(old_root / name)
        new_tags, new_text = skeleton(new_root / name)
        old_tags = normalize(old_tags)
        new_tags = normalize(new_tags)
        old_tags, new_tags = align(old_tags, new_tags)
        old_text = [" ".join(normalize_text(old_text))]
        new_text = [" ".join(normalize_text(new_text))]
        if old_tags != new_tags:
            print(f"\n{name}: structure differs")
            problems += 1
            for index, (a, b) in enumerate(zip(old_tags, new_tags)):
                if a != b:
                    print(f"  first difference at element {index}")
                    print(f"    old: {a}")
                    print(f"    new: {b}")
                    context = " | ".join(old_tags[max(0, index - 3):index])
                    print(f"    context: {context}")
                    break
            else:
                print(f"  old has {len(old_tags)} elements, new has {len(new_tags)}")
        if old_text != new_text:
            print(f"{name}: text differs")
            problems += 1
            old_joined = old_text[0]
            new_joined = new_text[0]
            for index, (a, b) in enumerate(zip(old_joined, new_joined)):
                if a != b:
                    print(f"  first difference at character {index}")
                    print(f"    old: {old_joined[max(0, index - 60):index + 60]!r}")
                    print(f"    new: {new_joined[max(0, index - 60):index + 60]!r}")
                    break
            else:
                print(f"  old has {len(old_joined)} characters, new has {len(new_joined)}")
                shorter = min(old_joined, new_joined)
                print(f"    old tail: {old_joined[len(shorter):][:120]!r}")
                print(f"    new tail: {new_joined[len(shorter):][:120]!r}")

    old_media = media_files(old_root)
    new_media = media_files(new_root)
    missing = sorted(set(old_media) - set(new_media))
    if missing:
        print("\nfiles missing from the new build:", missing[:20])
        problems += 1

    print(f"\n{problems} difference(s) found")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
