#!/usr/bin/env python3
"""Build the site.

The media registry is regenerated first so that any image added since the
last build is published with the right responsive set, then Hugo renders the
site.

Usage:
    python tools/build.py [output folder] [base url]

The base url defaults to the one in hugo.toml, which is what the published
site uses. Pass a different one to build a copy for local testing, where the
assets have to come from the local server rather than from the live site.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import media_registry  # noqa: E402


def main(argv: list[str]) -> int:
    project = Path(__file__).resolve().parent.parent
    output = argv[1] if len(argv) > 1 else "public"
    base_url = argv[2] if len(argv) > 2 else None

    registry = media_registry.write(project)
    print(f"media registry: {len(registry)} entries")

    command = ["hugo", "--cleanDestinationDir", "--destination", output]
    if base_url:
        command += ["--baseURL", base_url]
    print(" ".join(command))
    result = subprocess.run(command, cwd=project)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
