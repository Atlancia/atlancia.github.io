#!/usr/bin/env python3
"""Check that every post's cover files are actually there.

Two questions, both of them cheap to ask and both of them expensive to get
wrong in production:

    twins        each post's featureimage names a stem whose -cover-light
                 and -cover-dark webp twins sit beside it in static/
    motion       each coverMotion name has a file at assets/covers/<name>.svg

The stem is the featureimage path without its extension and without a
trailing -cover-light, -cover-dark, -rest or -cover tail, so a resting
frame like media/posts/2/ba-cover-rest.webp expects the twins
media/posts/2/ba-cover-light.webp and media/posts/2/ba-cover-dark.webp,
while a light twin like media/posts/2/bapost-cover-light.webp expects
itself and its dark sibling.

Usage:
    python tools/verify_covers.py [repo root]

Exit code 0 means everything checked out, 1 means something is wrong and the
report says what.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path, PurePosixPath

# Tails that mark one rendering of a cover rather than the cover itself.
# Stripped repeatedly, so ba-cover-rest sheds -rest and then -cover.
TAILS = ("-cover-light", "-cover-dark", "-rest", "-cover")

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
FEATUREIMAGE = re.compile(r'^featureimage:\s*"?([^"\s][^"]*?)"?\s*$', re.M)
MOTION = re.compile(r'^coverMotion:\s*"?([A-Za-z0-9_-]+)"?\s*$', re.M)


def frontmatter(text: str) -> str:
    match = FRONTMATTER.match(text)
    return match.group(1) if match else ""


def featureimage(block: str) -> str:
    match = FEATUREIMAGE.search(block)
    return match.group(1).strip() if match else ""


def cover_motion(block: str) -> str:
    match = MOTION.search(block)
    return match.group(1) if match else ""


def stem_of(feature: str) -> str:
    """The cover stem behind a featureimage path.

    Drops any query or fragment and the extension, then sheds render tails
    until none is left, so a resting frame (ba-cover-rest) and either twin
    (bapost-cover-light) both resolve to the stem the pair is published
    under (ba, bapost).
    """
    bare = feature.split("#", 1)[0].split("?", 1)[0]
    stem = PurePosixPath(bare).with_suffix("").as_posix()
    stripped = True
    while stripped:
        stripped = False
        for tail in TAILS:
            if stem.endswith(tail):
                stem = stem[: -len(tail)]
                stripped = True
    return stem


def twins(feature: str) -> tuple[str, str]:
    """The two static-relative twin paths a featureimage requires."""
    stem = stem_of(feature)
    return f"{stem}-cover-light.webp", f"{stem}-cover-dark.webp"


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parents[1]
    posts = root / "content" / "posts"
    static = root / "static"
    covers = root / "assets" / "covers"
    if not posts.is_dir():
        print(f"no posts at {posts}")
        return 1

    problems: list[str] = []
    images = 0
    twins_ok = 0
    motion_ok = 0

    for md in sorted(posts.glob("*.md")):
        try:
            block = frontmatter(md.read_text(encoding="utf-8"))
        except OSError as error:
            problems.append(f"{md.name}: cannot be read: {error}")
            continue
        if not block:
            continue
        feature = featureimage(block)
        name = cover_motion(block)
        if name:
            if (covers / f"{name}.svg").is_file():
                motion_ok += 1
            else:
                problems.append(
                    f'{md.name}: coverMotion "{name}" '
                    f"has no file at assets/covers/{name}.svg"
                )
            # Motion covers are motion-first: the rest frame plus SVG is the
            # artifact. Twins are only required for dither/artwork posts
            # without a coverMotion entry.
            continue
        if feature and not feature.startswith(("http://", "https://")):
            images += 1
            for twin in twins(feature):
                if (static / twin).is_file():
                    twins_ok += 1
                else:
                    problems.append(f"{md.name}: missing twin: static/{twin}")
        name = cover_motion(block)
        if name:
            if (covers / f"{name}.svg").is_file():
                motion_ok += 1
            else:
                problems.append(
                    f'{md.name}: coverMotion "{name}" '
                    f"has no file at assets/covers/{name}.svg"
                )

    if problems:
        print(f"{len(problems)} problems in {posts}:")
        for problem in problems:
            print(f"  {problem}")
        return 1

    print(f"ok: {images} featureimages, {twins_ok} twins, {motion_ok} motion svgs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
