#!/usr/bin/env python3
"""Build the site in another theme, so a theme can be looked at rather than guessed at.

The content, the figures and the media are copied over and the front matter is
remapped to the conventions of the theme being tried. Everything the theme
brings is used as it comes, which is the point: what you see is the theme as
its author intends, with your writing in it.

This is a way to choose, not a way to ship. The parts of the site that are
yours, the embed shortcode, the gallery, the comment widget, the reading aids
and the colour mode, are re-expressed for whichever theme you settle on.

Usage:
    python tools/theme_lab.py list
    python tools/theme_lab.py build <theme> [base url]
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAB = ROOT.parent / "atlancia-lab"
THEMES = ROOT / "tools" / "themes"


def load_config(name: str) -> dict:
    path = THEMES / f"{name}.json"
    if not path.exists():
        raise SystemExit(f"no theme called {name}. Try: python tools/theme_lab.py list")
    return json.loads(path.read_text(encoding="utf-8"))


def remap_front_matter(text: str, config: dict) -> str:
    """Rename the front matter keys the theme expects."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return text
    end = lines.index("---", 1)
    front = lines[1:end]
    body = lines[end + 1:]

    out = []
    for line in front:
        stripped = line.strip()
        if stripped.startswith("type:") or stripped.startswith("layout:"):
            # The theme decides its own layouts.
            continue
        if stripped.startswith("url:") and config.get("drop_url", True):
            # The theme decides its own addresses.
            continue
        if stripped.startswith("featured_image:") and config.get("featured_image_key"):
            value = stripped.split(":", 1)[1].strip().strip('"')
            key = config["featured_image_key"]
            if config.get("featured_image_style") == "cover":
                # PaperMod reads a table, with the image named inside it. The
                # bundle holds the image under the name the theme looks for.
                out.append(f"{key}:")
                out.append(f"  image: featured{Path(value).suffix}")
            else:
                out.append(f"{key}: {value}")
            continue
        out.append(line)
    return "\n".join(["---"] + out + ["---"] + body)


def toml_value(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return "[" + ", ".join(toml_value(item) for item in value) + "]"
    return json.dumps(value)


def toml_document(settings: dict, prefix: str = "") -> str:
    lines = []
    tables = []
    for key, value in settings.items():
        if isinstance(value, dict):
            tables.append((key, value))
        else:
            lines.append(f"{key} = {toml_value(value)}")
    for key, value in tables:
        name = f"{prefix}{key}"
        lines.append("")
        lines.append(f"[{name}]")
        body = toml_document(value, f"{name}.")
        lines.extend(body.strip("\n").split("\n"))
    return "\n".join(lines) + "\n"


def remove_tree(path: Path) -> None:
    """Remove a directory, including the read-only files a clone leaves behind."""
    import os
    import stat

    def make_writable(function, target, _error):
        os.chmod(target, stat.S_IWRITE)
        function(target)

    shutil.rmtree(path, onerror=make_writable)


def make_bundle(source: Path, destination: Path, media_root: Path, config: dict) -> None:
    """Turn a post into a page bundle with its own images beside it.

    The published site keeps the media in one folder and resolves it with a
    template of its own, which only that site understands. A page bundle is
    the way Hugo expects a post's own media to live, and it works in any
    theme with no image code at all.
    """
    text = remap_front_matter(source.read_text(encoding="utf-8"), config)
    media_id = ""
    for line in text.split("\n"):
        if line.startswith("media_id:"):
            media_id = line.split(":", 1)[1].strip()
    folder = media_root / "posts" / media_id if media_id else None

    destination.mkdir(parents=True, exist_ok=True)
    destination.joinpath("index.md").write_text(text, encoding="utf-8")

    if folder and folder.is_dir():
        for name in set(re.findall(r"\]\(([^)\s]+)", text)):
            if "/" in name or name.startswith("http"):
                continue
            source_image = folder / name
            if source_image.is_file():
                shutil.copy2(source_image, destination / name)

    # The image at the top of the post, which the theme looks for by name.
    featured = ""
    for line in text.split("\n"):
        if line.startswith("featured_image:"):
            featured = line.split(":", 1)[1].strip().strip('"')
    if featured and folder:
        source_image = folder / Path(featured).name
        if source_image.is_file():
            shutil.copy2(source_image, destination / f"featured{Path(featured).suffix}")


def build(name: str, base_url: str | None) -> int:
    config = load_config(name)
    target = LAB / name
    if target.exists():
        remove_tree(target)
    target.mkdir(parents=True)

    print(f"cloning {config['repo']}")
    subprocess.run(
        ["git", "clone", "--depth", "1", "--branch", config.get("branch", "main"), config["repo"], str(target / "themes" / config["name"])],
        check=True,
    )

    # The content, with the front matter remapped.
    content = target / "content"
    content.mkdir()
    for source in sorted((ROOT / "content").rglob("*.md")):
        relative = source.relative_to(ROOT / "content")
        if config.get("skip") and relative.as_posix() in config["skip"]:
            continue
        if config.get("bundles", True) and relative.parent.name == "posts":
            make_bundle(
                source,
                content / relative.parent / source.stem,
                ROOT / "static" / "media",
                config,
            )
            continue
        destination = content / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(remap_front_matter(source.read_text(encoding="utf-8"), config), encoding="utf-8")

    # The media, the fonts, the stylesheet and the content manager.
    shutil.copytree(ROOT / "static", target / "static")
    shutil.copytree(ROOT / "data", target / "data")

    # The shortcode that places a figure in a post is ours, and works in any theme.
    shortcodes = target / "layouts" / "shortcodes"
    shortcodes.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "layouts" / "shortcodes" / "embed.html", shortcodes / "embed.html")

    # The theme's own configuration, if it ships one. Only the English files
    # are taken, so a theme with nine languages does not build nine sites.
    example = target / "themes" / config["name"] / "exampleSite"
    if example.is_dir():
        for item in ("config", "assets", "data", "i18n", "archetypes"):
            source = example / item
            if not source.is_dir():
                continue
            if item == "config":
                destination = target / item
                destination.mkdir(parents=True, exist_ok=True)
                for file in sorted(source.rglob("*")):
                    if not file.is_file():
                        continue
                    name = file.name
                    if "." in name:
                        suffix = name.split(".", 1)[1].replace(".toml", "").replace(".yaml", "").replace(".json", "")
                        if suffix and suffix not in ("en", "toml", "yaml", "json"):
                            continue
                    target_file = destination / file.relative_to(source)
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file, target_file)
            else:
                shutil.copytree(source, target / item, dirs_exist_ok=True)

    settings = {
        "baseURL": base_url or "http://localhost:8080/",
        "languageCode": "en-gb",
        "title": "Atlancia",
        "timeZone": "America/Toronto",
        "enableRobotsTXT": False,
        "summaryLength": 45,
        "uglyURLs": True,
        "permalinks": {"posts": "/:slug"},
    }
    settings.update(config.get("config", {}))
    (target / "hugo.toml").write_text(toml_document(settings), encoding="utf-8")

    print(f"building {target}")
    try:
        from build import find_hugo

        default_hugo = find_hugo()
    except (ImportError, SystemExit):
        default_hugo = "hugo"
    hugo = config.get("hugo", default_hugo)
    result = subprocess.run(
        [hugo, "--cleanDestinationDir", "--destination", "public"], cwd=target
    )
    if result.returncode == 0:
        print(f"\nOpen {target / 'public' / 'index.html'}")
    return result.returncode


def list_themes() -> int:
    if not THEMES.is_dir():
        print("no themes are set up yet")
        return 1
    for path in sorted(THEMES.glob("*.json")):
        config = json.loads(path.read_text(encoding="utf-8"))
        print(f"{path.stem:16} {config.get('repo', '')}")
    return 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] == "list":
        return list_themes()
    if argv[0] != "build":
        print(__doc__)
        return 2
    name = argv[1] if len(argv) > 1 else ""
    base_url = argv[2] if len(argv) > 2 else None
    return build(name, base_url)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
