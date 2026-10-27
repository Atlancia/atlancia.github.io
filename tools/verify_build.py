#!/usr/bin/env python3
"""Check a built site before it is published.

Three questions, all of them cheap to answer and all of them expensive to get
wrong in production:

    addresses   are the old site's addresses all still there
    feeds       do /feed.xml and /feed.json parse, and do they carry the posts
    links       does every internal link and image in the pages resolve to a
                file that the build actually produced

Usage:
    python tools/verify_build.py [output folder]

Exit code 0 means everything checked out, 1 means something is wrong and the
report says what.
"""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

# The addresses the old site published. A file at each of these is the promise
# that nothing a reader bookmarked has moved.
REQUIRED = [
    "index.html",
    "404.html",
    "feed.xml",
    "feed.json",
    "sitemap.xml",
    "robots.txt",
    "authors/liam/index.html",
    "tags/index.html",
    "business-analyst-reflection.html",
    "difference-needs-somewhere-to-go.html",
    "diversity-complexity.html",
    "leaders-gardeners.html",
    "trade-off-mentality.html",
    "welcome-to-atlancia.html",
]

POSTS = 5

LINK = re.compile(r'(?:href|src)="([^"]+)"')


def local_targets(html: str):
    for target in LINK.findall(html):
        if target.startswith(("http://", "https://", "//", "#", "mailto:", "data:")):
            continue
        yield target


def resolves(site: Path, target: str) -> bool:
    """Does this site-relative address point at something in the build?"""
    path = target.split("#", 1)[0].split("?", 1)[0]
    if not path or path == "/":
        return (site / "index.html").exists()
    relative = path.lstrip("/")
    candidate = site / relative
    if candidate.is_file():
        return True
    if candidate.is_dir():
        return (candidate / "index.html").exists()
    return (site / relative / "index.html").exists()


def main(argv: list[str]) -> int:
    site = Path(argv[1] if len(argv) > 1 else "public").resolve()
    if not site.is_dir():
        print(f"no build at {site}")
        return 1

    problems: list[str] = []

    for address in REQUIRED:
        if not (site / address).is_file():
            problems.append(f"missing address: /{address}")

    try:
        feed = ET.parse(site / "feed.xml").getroot()
        entries = feed.findall("{http://www.w3.org/2005/Atom}entry")
        if len(entries) != POSTS:
            problems.append(f"/feed.xml has {len(entries)} entries, expected {POSTS}")
    except (OSError, ET.ParseError) as error:
        problems.append(f"/feed.xml does not parse: {error}")

    try:
        data = json.loads((site / "feed.json").read_text(encoding="utf-8"))
        if len(data.get("items", [])) != POSTS:
            problems.append(
                f"/feed.json has {len(data.get('items', []))} items, expected {POSTS}"
            )
    except (OSError, ValueError) as error:
        problems.append(f"/feed.json does not parse: {error}")

    try:
        sitemap = ET.parse(site / "sitemap.xml").getroot()
        urls = sitemap.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
        if len(urls) != POSTS + 1:
            problems.append(
                f"/sitemap.xml has {len(urls)} urls, expected {POSTS + 1} "
                "(the home page, the essays, the welcome page)"
            )
    except (OSError, ET.ParseError) as error:
        problems.append(f"/sitemap.xml does not parse: {error}")

    broken: dict[str, set[str]] = {}
    for page in site.rglob("*.html"):
        for target in local_targets(page.read_text(encoding="utf-8", errors="replace")):
            if not resolves(site, target):
                broken.setdefault(str(page.relative_to(site)), set()).add(target)

    for page, targets in sorted(broken.items()):
        for target in sorted(targets):
            problems.append(f"{page}: {target} does not resolve")

    if problems:
        print(f"{len(problems)} problems in {site}:")
        for problem in problems:
            print(f"  {problem}")
        return 1

    print(
        f"ok: {len(REQUIRED)} addresses, {POSTS} entries in both feeds, "
        f"{POSTS + 1} sitemap urls, no broken internal links"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
