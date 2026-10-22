#!/usr/bin/env python3
"""Build the light mode version of the wordmark.

The wordmark is a white shape on a transparent background, which disappears on
a light page. The light version is the same shape with the same transparency
and a dark fill, so the two match exactly.

The extraction calls this so that the variant is always in step with the
original.

Usage:
    python tools/make_logo_variant.py
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "static" / "media" / "website" / "logo-2.png"
TARGET = ROOT / "static" / "media" / "website" / "logo-2-dark.png"
INK = (22, 22, 26, 255)


def build_variant(source: pathlib.Path, target: pathlib.Path, ink=INK) -> bool:
    """Write the dark fill variant of a white wordmark next to it."""
    if not source.exists():
        return False
    try:
        from PIL import Image
    except ImportError:
        print("Pillow is not available, so the wordmark variant was not built")
        return False

    image = Image.open(source).convert("RGBA")
    alpha = image.getchannel("A")
    dark = Image.new("RGBA", image.size, ink)
    dark.putalpha(alpha)
    target.parent.mkdir(parents=True, exist_ok=True)
    dark.save(target, "PNG", optimize=True)
    return True


def main() -> int:
    if not build_variant(SOURCE, TARGET):
        print(f"missing {SOURCE}", file=sys.stderr)
        return 1
    print(f"wrote {TARGET} ({TARGET.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
