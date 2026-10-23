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


PINNED = "hugo-0.167.0-extended-windows-amd64.exe"


def find_hugo() -> str:
    """The Hugo to build with. The pinned binary ships in tools/bin."""
    chosen = os.environ.get("HUGO")
    if chosen:
        return chosen

    project = Path(__file__).resolve().parent.parent
    vendored = project / "tools" / "bin" / PINNED
    if vendored.exists():
        return str(vendored)

    for candidate in sorted((project / "tools" / "bin").glob("hugo*")):
        if candidate.is_file():
            return str(candidate)

    legacy = Path.home() / "bin" / "hugo-0.167-extended.exe"
    if legacy.exists():
        return str(legacy)

    found = shutil.which("hugo")
    if found:
        return found

    raise SystemExit(
        "no Hugo found: expected tools/bin/" + PINNED + " in the repository, "
        "or set HUGO to a Hugo 0.167 extended binary"
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
