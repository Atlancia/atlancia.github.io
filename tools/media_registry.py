#!/usr/bin/env python3
"""Build the media registry the templates read.

The registry maps every file under the site's media folder to the attributes
the theme publishes it with: the address, the responsive set and the size.
It is regenerated on every build so that an image added in the content
manager is picked up without any other step.

Usage:
    python tools/media_registry.py <project folder>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

# The responsive variants the theme published, in order.
RESPONSIVE_WIDTHS: list[tuple[str, int]] = [
    ("xs", 640),
    ("sm", 768),
    ("md", 1024),
    ("lg", 1366),
    ("xl", 1600),
    ("2xl", 1920),
]


def image_dimensions(path: Path) -> tuple[int, int]:
    try:
        from PIL import Image  # type: ignore

        with Image.open(path) as image:
            return image.size
    except Exception:
        return (0, 0)


def build(media_root: Path) -> dict[str, Any]:
    registry: dict[str, Any] = {}
    if not media_root.is_dir():
        return registry

    for path in sorted(media_root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(media_root).as_posix()
        entry: dict[str, Any] = {"src": f"media/{rel}"}

        dimensions = image_dimensions(path)
        if dimensions[0]:
            entry["width"] = str(dimensions[0])
            entry["height"] = str(dimensions[1])

        if path.parent.name != "responsive":
            parts: list[str] = []
            for suffix, width in RESPONSIVE_WIDTHS:
                for candidate in sorted(path.parent.glob(f"responsive/{path.stem}-{suffix}.*")):
                    parts.append(f"media/{candidate.relative_to(media_root).as_posix()} {width}w")
            if parts:
                entry["srcset"] = parts
                entry["sizes"] = "(max-width: 1920px) 100vw, 1920px"

        registry[f"media/{rel}"] = entry
        registry.setdefault(path.name, entry)

    return registry


def write(project: Path) -> dict[str, Any]:
    registry = build(project / "static" / "media")
    data = project / "data"
    data.mkdir(parents=True, exist_ok=True)
    (data / "media.json").write_text(
        json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return registry


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    project = Path(argv[1]).resolve()
    registry = write(project)
    print(f"media registry written with {len(registry)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
