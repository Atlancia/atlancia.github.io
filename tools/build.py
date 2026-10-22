#!/usr/bin/env python3
"""Build the site.

Hugo renders the site into the output folder. The theme processes the images,
so the extended build of Hugo is required: the plain one cannot resize WebP.

Usage:
    python tools/build.py [output folder] [base url]

The base url defaults to the one in config/_default/hugo.toml, which is what
the published site uses. Pass a different one to build a copy for local
testing, where the assets have to come from the local server rather than from
the live site.

Set HUGO to choose a particular binary. Otherwise the build looks for the
extended 0.167 build in C:\\Users\\<you>\\bin, then for hugo on the path.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def find_hugo() -> str:
    """The Hugo to build with, preferring the pinned extended build."""
    chosen = os.environ.get("HUGO")
    if chosen:
        return chosen

    pinned = Path.home() / "bin" / "hugo-0.167-extended.exe"
    if pinned.exists():
        return str(pinned)

    found = shutil.which("hugo")
    if found:
        return found

    raise SystemExit(
        "no Hugo found: put hugo-0.167-extended.exe in ~/bin, put hugo on the "
        "path, or set HUGO to the binary"
    )


def main(argv: list[str]) -> int:
    project = Path(__file__).resolve().parent.parent
    output = argv[1] if len(argv) > 1 else "public"
    base_url = argv[2] if len(argv) > 2 else None

    command = [find_hugo(), "--cleanDestinationDir", "--destination", output]
    if base_url:
        command += ["--baseURL", base_url]
    print(" ".join(command))
    result = subprocess.run(command, cwd=project)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
