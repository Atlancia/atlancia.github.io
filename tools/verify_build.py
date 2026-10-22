#!/usr/bin/env python3
"""Check a built site before it is published.

Four questions, all of them cheap to answer and all of them expensive to get
wrong in production:

    addresses   are the old site's addresses all still there
    feeds       do /feed.xml and /feed.json parse, and do they carry the essays
    links       does every internal link, image, responsive variant and font
                resolve to a file that the build actually produced
    production  is this the published build, or a `hugo server` one

The counts the feeds and the sitemap are checked against are counted from the
lists below rather than written down, so adding an essay does not quietly
weaken the check.

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
from urllib.parse import urlparse

# The essays. Each one owes the reader an address, an entry in both feeds and
# a place in the sitemap, so this list is the one place that says how many
# there are.
POSTS = [
    "business-analyst-reflection.html",
    "difference-needs-somewhere-to-go.html",
    "diversity-complexity.html",
    "leaders-gardeners.html",
    "trade-off-mentality.html",
]

# The rest of what the old site published. A file at each of these is the
# promise that nothing a reader bookmarked has moved.
PAGES = [
    "index.html",
    "404.html",
    "welcome-to-atlancia.html",
    "authors/liam/index.html",
    "tags/index.html",
    "robots.txt",
]

FEEDS = ["feed.xml", "feed.json"]
SITEMAP = "sitemap.xml"

# The sitemap carries the essays, the home page and the welcome page, and
# nothing else: the author page and the tag page are not listed.
SITEMAP_URLS = len(POSTS) + 2

LINK = re.compile(r'(?:href|src)="([^"]+)"')
SRCSET = re.compile(r'srcset="([^"]+)"')
CSS_URL = re.compile(r"""url\(\s*["']?([^"')]+)""")

# What a browser leaves alone, and what is not this site's to serve.
SKIP = ("#", "mailto:", "data:", "javascript:", "tel:")


def own_host(site: Path) -> str | None:
    """The host the site was built for, taken from its own sitemap."""
    try:
        root = ET.parse(site / SITEMAP).getroot()
    except (OSError, ET.ParseError):
        return None
    for loc in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        host = urlparse(loc.text or "").netloc
        if host:
            return host
    return None


def site_path(target: str, host: str | None) -> str | None:
    """The path this build owes, or None when the address is not this site's.

    An address on the site's own host is still the site's to serve, and the
    theme writes the author and tag links that way. The host has to be read
    out of the address rather than looked for inside it: the share links a
    post carries have this site's address in their query string, and those
    belong to whichever service the reader is being sent to.
    """
    if target.startswith(SKIP):
        return None
    parsed = urlparse(target)
    if parsed.scheme in ("http", "https") or target.startswith("//"):
        if not host or parsed.netloc.lower() != host.lower():
            return None
        return parsed.path or "/"
    return target


def local_targets(html: str, host: str | None):
    """Every address in the page that this build is supposed to serve."""
    for target in LINK.findall(html):
        path = site_path(target.replace("&amp;", "&"), host)
        if path is not None:
            yield path


def srcset_targets(html: str, host: str | None):
    """Every candidate a responsive image offers, without its descriptor."""
    for attr in SRCSET.findall(html):
        for candidate in attr.split(","):
            candidate = candidate.strip()
            if not candidate:
                continue
            path = site_path(candidate.split()[0].replace("&amp;", "&"), host)
            if path is not None:
                yield path


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
    host = own_host(site)

    for address in POSTS + PAGES:
        if not (site / address).is_file():
            problems.append(f"missing address: /{address}")

    try:
        feed = ET.parse(site / FEEDS[0]).getroot()
        entries = feed.findall("{http://www.w3.org/2005/Atom}entry")
        if len(entries) != len(POSTS):
            problems.append(
                f"/{FEEDS[0]} has {len(entries)} entries, expected {len(POSTS)}"
            )
    except (OSError, ET.ParseError) as error:
        problems.append(f"/{FEEDS[0]} does not parse: {error}")

    try:
        data = json.loads((site / FEEDS[1]).read_text(encoding="utf-8"))
        items = data.get("items", [])
        if len(items) != len(POSTS):
            problems.append(
                f"/{FEEDS[1]} has {len(items)} items, expected {len(POSTS)}"
            )
    except (OSError, ValueError) as error:
        problems.append(f"/{FEEDS[1]} does not parse: {error}")

    try:
        sitemap = ET.parse(site / SITEMAP).getroot()
        urls = sitemap.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
        if len(urls) != SITEMAP_URLS:
            problems.append(
                f"/{SITEMAP} has {len(urls)} urls, expected {SITEMAP_URLS} "
                "(the home page, the essays, the welcome page)"
            )
    except (OSError, ET.ParseError) as error:
        problems.append(f"/{SITEMAP} does not parse: {error}")

    broken: dict[str, set[str]] = {}

    def complain(page: Path, target: str) -> None:
        where = page.relative_to(site) if page.is_relative_to(site) else page
        broken.setdefault(str(where), set()).add(target)

    for page in site.rglob("*.html"):
        html = page.read_text(encoding="utf-8", errors="replace")

        # A `hugo server` build carries the reload script, and so does a
        # folder that a server has written over. Publishing it would put a
        # websocket to port 1313 in front of every reader.
        if "livereload.js" in html:
            problems.append(
                f"{page.relative_to(site)}: the livereload script is in this "
                "build, so it is a server build and not the published one"
            )
            break

        for target in local_targets(html, host):
            if not resolves(site, target):
                complain(page, target)
        for target in srcset_targets(html, host):
            if not resolves(site, target):
                complain(page, target)

    # The stylesheet asks for the fonts by address. A missing one is not a
    # broken link a reader can see, it is the wrong typeface.
    for sheet in site.rglob("*.css"):
        for target in CSS_URL.findall(sheet.read_text(encoding="utf-8", errors="replace")):
            target = target.replace("&amp;", "&").strip()
            if target.startswith(("http://", "https://", "//", "data:")):
                continue
            resolved = target if target.startswith("/") else "/" + str(
                (sheet.parent / target).relative_to(site)
            ).replace("\\", "/")
            if not resolves(site, resolved):
                complain(sheet, target)

    for page, targets in sorted(broken.items()):
        for target in sorted(targets):
            problems.append(f"{page}: {target} does not resolve")

    if problems:
        print(f"{len(problems)} problem{'' if len(problems) == 1 else 's'} in {site}:")
        for problem in problems:
            print(f"  {problem}")
        return 1

    print(
        f"ok: {len(POSTS) + len(PAGES)} addresses, {len(POSTS)} essays in both "
        f"feeds, {SITEMAP_URLS} sitemap urls, no broken internal links"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
