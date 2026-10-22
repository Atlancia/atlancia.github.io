#!/usr/bin/env python3
"""Test the checker by breaking a good build on purpose.

A checker that says "ok" is only worth having if it says "problem" when there
is one. This copies a build that passed, breaks one thing in each copy, and
records what `verify_build.py` said about it. Nothing is kept: the copies live
in a temporary folder.

Usage:
    python tools/test_verify_build.py [output folder]

The folder has to be a build that `verify_build.py` already passes, since the
first case is that it still does. Exit code 0 means every case behaved.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
CHECKER = TOOLS / "verify_build.py"


def srcset_target(site: Path) -> str:
    """A responsive image the build serves, to take away."""
    for page in site.rglob("*.html"):
        text = page.read_text(encoding="utf-8", errors="replace")
        for attribute in text.split('srcset="')[1:]:
            for candidate in attribute.split('"')[0].split(","):
                url = candidate.strip().split()[0] if candidate.strip() else ""
                if url.startswith("/"):
                    return url
    raise SystemExit("no responsive image in this build to take away")


def font_target(site: Path) -> str:
    """The typeface the stylesheet asks for, to take away."""
    for sheet in site.rglob("*.css"):
        for url in sheet.read_text(encoding="utf-8", errors="replace").split("url(")[1:]:
            url = url.lstrip("\"'").split('"')[0].split("'")[0].split(")")[0]
            if url.startswith("/"):
                return url
    raise SystemExit("no font in this build to take away")


def take_away(relative: str, site: Path) -> None:
    target = site / relative.lstrip("/")
    if not target.exists():
        raise SystemExit(f"expected {relative} in the build")
    target.unlink()


def spoil_the_feed(relative: str, site: Path) -> None:
    (site / relative).write_text("{ this is not json", encoding="utf-8")


def add_the_reload_script(relative: str, site: Path) -> None:
    page = site / relative
    page.write_text(
        page.read_text(encoding="utf-8").replace(
            "</head>", '<script src="/livereload.js?port=1313"></script></head>', 1
        ),
        encoding="utf-8",
    )


def break_a_link_home(relative: str, site: Path) -> None:
    """Point a link that names this site's own host at a page that is not there."""
    for page in sorted(site.rglob("*.html")):
        text = page.read_text(encoding="utf-8", errors="replace")
        if relative in text:
            page.write_text(
                text.replace(relative, "https://atlancia.com/no-such-page/"),
                encoding="utf-8",
            )
            return
    raise SystemExit(f"no page carries {relative}")


def cases(site: Path):
    return [
        ("a good build passes", None, None, 0, "ok:"),
        ("an essay is missing", take_away, "/trade-off-mentality.html", 1, "missing address"),
        ("a responsive image is missing", take_away, srcset_target(site), 1, "does not resolve"),
        ("the typeface is missing", take_away, font_target(site), 1, "does not resolve"),
        ("the json feed is spoiled", spoil_the_feed, "feed.json", 1, "does not parse"),
        ("the build came from a server", add_the_reload_script, "index.html", 1, "livereload"),
        ("a link home is broken", break_a_link_home, "https://atlancia.com/tags/", 1, "no-such-page"),
    ]


def main(argv: list[str]) -> int:
    site = (TOOLS.parent / (argv[1] if len(argv) > 1 else "public")).resolve()
    if not site.is_dir():
        print(f"no build at {site}")
        return 1

    failures = 0
    with tempfile.TemporaryDirectory() as temporary:
        for name, break_it, argument, want_code, want_text in cases(site):
            copy = Path(temporary) / "site"
            if copy.exists():
                shutil.rmtree(copy)
            shutil.copytree(site, copy)

            if break_it is not None:
                break_it(argument, copy)

            result = subprocess.run(
                [sys.executable, str(CHECKER), str(copy)],
                capture_output=True,
                text=True,
            )
            said = (result.stdout + result.stderr).strip()
            behaved = result.returncode == want_code and want_text in said
            failures += 0 if behaved else 1
            print(f"[{'ok' if behaved else 'wrong'}] {name}: {said.splitlines()[0]}")
            if not behaved:
                print(f"        wanted exit {want_code} and {want_text!r}")

    if failures:
        print(f"{failures} of {len(cases(site))} cases did not behave")
        return 1

    print(f"ok: all {len(cases(site))} cases behaved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
