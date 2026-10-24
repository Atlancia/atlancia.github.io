# Build-time cover treatment generator for Atlancia.
#
# Publishes the duotone twins of a treated cover, one per appearance mode:
#
#     static/media/posts/<n>/<stem>-cover-dark.webp
#     static/media/posts/<n>/<stem>-cover-light.webp
#
# Each variant maps the photograph onto the site's two palette colours
# (#23233D navy, #FFC074 amber) and then Floyd-Steinberg dithers it into a
# pure two-tone texture. The modes differ in which colour leads the ramp:
# amber plays the highlights on the dark cover, navy plays them on the light
# cover, so the light-mode figure reads as the darker tone sitting on the
# site's cream ground.
#
# An essay opts in through its frontmatter, pointing featureimage at the
# LIGHT variant and naming the treatment:
#
#     featureimage: "media/posts/2/bapost-cover-light.webp"
#     coverStyle: "dither"
#
# Or, for a pair authored outside this pipeline (a hand-made duotone kept as
# PNG sources beside the photos), name the ARTWORK style instead. The tool
# then generates nothing: it only checks that both twin webps exist at the
# stem, and --force is a no-op, so rebuilding the machine-made covers can
# never clobber a hand-made pair. The authored sources stay untouched.
#
# The site stacks both twins in the cover slot and crossfades between them
# on appearance mode and on hover (layouts + custom.css), so these two files
# are the only build output. The source photograph stays untouched. Outputs
# are skipped while newer than their source; --force rebuilds.
#
# Publish a new or changed treatment with:  python tools/make_covers.py

import re
import sys
from pathlib import Path

import yaml
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "posts"
STATIC = ROOT / "static"

WIDTH = 1200

NAVY = (35, 35, 61)     # #23233D
AMBER = (255, 192, 116) # #FFC074


def frontmatter(md_path):
    text = md_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return {}
    return yaml.safe_load(match.group(1)) or {}


def load_source(featureimage):
    """The source photograph behind a featureimage path.

    Accepts the original photo path or either variant name, so re-running
    after a frontmatter edit still finds the untouched source.
    """
    stem = featureimage
    for suffix in ("-cover-light", "-cover-dark"):
        stem = stem.replace(suffix, "")
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        candidate = STATIC / Path(stem).with_suffix(ext).as_posix()
        if candidate.exists():
            return candidate
    return None


H_RATIO = 1 / 3
TOP_BIAS = 0.42


def to_cover_size(im):
    w, h = im.size
    if w > WIDTH:
        im = im.resize((WIDTH, max(1, int(h * WIDTH / w))), Image.LANCZOS)
    return im


def fs_two_tone(gray, dark_color, light_color):
    """Floyd-Steinberg dither into exactly two colours, nearest by luminance."""
    lo = luminance(dark_color)
    hi = luminance(light_color)
    mid = (lo + hi) / 2
    px = gray.load()
    w, h = gray.size
    for y in range(h):
        for x in range(w):
            old = px[x, y]
            i = 0 if old < mid else 1
            err = old - (lo if i == 0 else hi)
            px[x, y] = i
            for dx, dy, weight in ((1, 0, 7 / 16), (-1, 1, 3 / 16), (0, 1, 5 / 16), (1, 1, 1 / 16)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h:
                    px[nx, ny] = max(0, min(255, int(px[nx, ny] + err * weight)))
    out = Image.new("RGB", (w, h))
    o = out.load()
    for y in range(h):
        for x in range(w):
            o[x, y] = (dark_color, light_color)[px[x, y]]
    return out


def luminance(rgb):
    r, g, b = rgb
    return 0.299 * r + 0.587 * g + 0.114 * b


def treat(mode, source):
    """One duotone twin: the two site colours, then a two-tone dither.

    Amber leads the dark variant's ramp; navy leads the light variant's.
    """
    im = Image.open(source).convert("RGB")
    # 3:1 band, biased slightly above center so ground-texture subjects keep
    # their horizon lines and the skies stay out of the frame.
    w, h = im.size
    band_h = min(h, int(w * H_RATIO + 0.5))
    top = int((h - band_h) * TOP_BIAS)
    band = im.crop((0, top, w, top + band_h))
    band = to_cover_size(band)
    gray = band.convert("L")
    if mode == "dark":
        duo = ImageOps.colorize(gray, black=NAVY, white=AMBER)
    else:
        duo = ImageOps.colorize(gray, black=AMBER, white=NAVY)
    return fs_two_tone(duo.convert("L"), NAVY, AMBER)


def process(md_path, force=False):
    fm = frontmatter(md_path)
    feature = fm.get("featureimage") or ""
    style = fm.get("coverStyle") or ""
    if not feature:
        return None
    if style and style not in ("dither", "artwork"):
        print(f"{md_path.name}: unknown coverStyle: {style}", file=sys.stderr)
        return None
    if not style:
        return None
    stem = Path(feature).with_suffix("").as_posix()
    for suffix in ("-cover-light", "-cover-dark", "-cover"):
        stem = stem.replace(suffix, "")
    if style == "artwork":
        outs = []
        for mode in ("dark", "light"):
            target = STATIC / f"{stem}-cover-{mode}.webp"
            if not target.exists():
                print(f"{md_path.name}: artwork twin missing: {target.relative_to(ROOT)}", file=sys.stderr)
                return None
            outs.append(target.relative_to(ROOT).as_posix())
        return outs
    original = load_source(feature)
    if not original:
        print(f"{md_path.name}: source photo not found for {feature}", file=sys.stderr)
        return None
    outs = []
    for mode in ("dark", "light"):
        target = STATIC / f"{stem}-cover-{mode}.webp"
        if force or not target.exists() or target.stat().st_mtime < original.stat().st_mtime:
            cover = treat(mode, original)
            cover.save(target, "WEBP", quality=92, method=6)
            outs.append(target.relative_to(ROOT).as_posix())
    return outs


def main():
    force = "--force" in sys.argv
    generated = []
    for md in sorted(CONTENT.glob("*.md")):
        made = process(md, force)
        if made:
            name = "; ".join(made) if made else "up to date"
            print(f"{md.stem}: {name}")
            generated.extend(made)
    if not generated:
        print("all treated covers up to date")


if __name__ == "__main__":
    main()
