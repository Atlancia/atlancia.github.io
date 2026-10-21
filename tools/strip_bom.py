#!/usr/bin/env python3
"""Remove byte order marks from text files in the project.

Editors and shell redirection on Windows sometimes leave a UTF-8 byte order
mark at the start of a file. Hugo refuses to parse a configuration file that
starts with one, and a stray mark shows up in published output.

Usage:
    python tools/strip_bom.py [paths...]
"""

from __future__ import annotations

import sys
from pathlib import Path

BOM = b"\xef\xbb\xbf"
SKIP_DIRS = {".git", "public", "resources", "node_modules"}


def strip(path: Path) -> bool:
    data = path.read_bytes()
    if not data.startswith(BOM):
        return False
    path.write_bytes(data[len(BOM):])
    return True


def main(argv: list[str]) -> int:
    roots = [Path(a) for a in argv] or [Path(".")]
    changed = 0
    for root in roots:
        candidates = [root] if root.is_file() else root.rglob("*")
        for path in candidates:
            if not path.is_file():
                continue
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.suffix.lower() in {".woff2", ".jpg", ".jpeg", ".png", ".webp", ".gif", ".ico"}:
                continue
            try:
                if strip(path):
                    changed += 1
                    print(f"stripped {path}")
            except OSError:
                continue
    print(f"{changed} file(s) changed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
