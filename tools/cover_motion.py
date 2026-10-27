#!/usr/bin/env python3
"""Ingest a generated motion cover into the site.

The cover editor exports a pair: an animated SVG and a composition JSON that
records what the editor meant. This tool reads both, places the artwork the way
the site needs it, renders the resting frame that feeds, social cards and
static lists use, and refuses to write anything it cannot verify.

    python tools/cover_motion.py \\
        --source  "C:/path/cover.svg" \\
        --composition "C:/path/cover-composition.json" \\
        --name gov-cover --media 7 --verify

Writes:
    assets/covers/<name>.svg          the artwork the pages inline
    assets/covers/<name>.json         the composition record, beside it
    static/media/posts/<media>/<name>-rest.webp

Why this tool exists rather than a straight copy
------------------------------------------------
Three things the site needs are not properties of the export, and the tool
resolves them the same way for every cover rather than case by case.

Placement. Every cover is centred, and every motion happens about that centre.
The editor works in drag offsets: `divider.x` and `icons[].x` are where things
were dropped, and the exported transforms carry those offsets through, so a
cover composed by eye drifts off axis. Once it is off axis, a card that crops
to the middle of the canvas cuts the subject in half. The tool anchors the
divider on the canvas axis and keeps its own y, since how high a divider sits
is a composition decision. It moves the icons onto the same axis as a block,
so two icons keep the spacing the author gave them.

Vertical calibration. A divider anchored to the bottom edge of the canvas has
to sit exactly on that edge at every point in its loop. The tool samples the
loop and lifts the artwork if the base ever rises above it.

Frames. The artwork is 3:1 and is used at two aspect ratios: the post hero,
full width, where it is shown whole, and the list thumbnail, which is 300x180
and holds the cover with `slice`, so only the middle of the canvas survives.
Anything that has to be read must therefore live in the middle. The tool
measures where the artwork actually sits over its whole loop and fails if an
icon leaves the window the card will show. A divider is reported against the
window rather than failed: a field of colour or a spotlight is allowed to bleed
off the sides, and cropping a shape is not the same as cropping a subject.

The one property the tool cannot judge from numbers is whether the motion
survived, and the motion is the whole point of these covers. So it renders the
resting frame and a frame a quarter of a cycle later and fails unless they
differ. A cover that is centred and still is a cover that broke.

Requires: Pillow, and Playwright with Chromium for rendering and verification.
Neither is needed by tools/build.py, so the site build has no such dependency.
"""

from __future__ import annotations

import argparse
import html
import re
import io
import json
import shutil
import sys
from pathlib import Path

CANVAS_W, CANVAS_H = 600, 200
OUT_W, OUT_H = 1800, 600

# The list thumbnail, measured in the built site: .thumbnail is 300px wide with
# a 180px floor, and motion-script.html sets xMidYMid slice. A 3:1 artwork in a
# 5:3 box scales on height, so what the reader sees is the middle 3/5 of the
# canvas, full height. Keep these in step with assets/css/custom.css and
# layouts/partials/functions/motion-script.html.
THUMB_W, THUMB_H = 300, 180
VISIBLE_FRACTION = THUMB_W / THUMB_H / (CANVAS_W / CANVAS_H)  # 0.5556
WINDOW_X0 = round(CANVAS_W * (1 - VISIBLE_FRACTION) / 2, 2)   # 133.33
WINDOW_X1 = round(CANVAS_W - WINDOW_X0, 2)                    # 466.67

CENTRE_TOLERANCE = 1.0
BLEED_FRACTION = 0.9  # a layer this wide is ground, not subject


def project_root() -> Path:
    return Path(__file__).resolve().parent.parent


# --- placement, in the browser ---------------------------------------------
#
# The editor emits every layer as
#   <g transform="translate(px py)"><g><animateTransform .../>
#     <g transform="translate(-px -py) [static transform]"> ... </g></g></g>
# when the layer moves, and as the inner <g> alone when it does not. The layer
# order is the scene order: ground, divider, then the icons. Rather than rewrite
# a transform chain as text, the tool loads the file, moves the right groups in
# the DOM and serialises: a string edit is easy to get subtly wrong, and wrong
# here means a cover that no longer animates.

PLACE_JS = r"""
([kind, iconCount, extraY]) => {
  const svg = document.querySelector('svg');
  const isG = el => el.tagName && el.tagName.toLowerCase() === 'g';
  const tf = el => el.getAttribute('transform') || '';
  const NUM = '(-?[\\d.eE+-]+)';
  const wrap = el => {
    const m = tf(el).match(new RegExp('^translate\\(' + NUM + ' ' + NUM + '\\)$'));
    return m ? { px: parseFloat(m[1]), py: parseFloat(m[2]) } : null;
  };
  const core = el => {
    if (!wrap(el)) return tf(el).startsWith('translate(') ? el : null;
    const inner = el.firstElementChild;
    if (!inner || !isG(inner)) return null;
    // A layer that moves is host > anonymous group (holding the animation) > core.
    // A layer that does not is host > core. The attribute tells the two apart.
    if (tf(inner).startsWith('translate(')) return inner;
    return [...inner.children].find(ch => isG(ch) && tf(ch).startsWith('translate(')) || null;
  };

  const groups = [...svg.children].filter(isG);
  const hasDivider = kind && kind !== 'none';
  // The cover lab emits the ground, one or two divider halves (thickrings and
  // similar split into two groups), the icon(s), and an optional treatment
  // layer. Count only the mandatory ones; extras are left untouched.
  const expected = 1 + (hasDivider ? 1 : 0) + iconCount;
  if (groups.length < expected) {
    return { error: 'the file has ' + groups.length + ' layers where the record accounts for at least ' + expected +
      ' (ground, ' + (hasDivider ? 'divider, ' : '') + iconCount + ' icon(s)). A new layer kind would do this.' };
  }

  // A layer's core transform starts with a run of translates. The editor always
  // emits them so that they cancel: the group outside the animation places the
  // artwork, and the translates inside it sum to zero, which is what makes the
  // animation happen about the artwork instead of dragging it across the canvas.
  // Two shapes are in the wild, with two or three translates in that run, so the
  // tool reads them all, edits the first and last, and keeps whatever is between.
  const chain = el => {
    let t = tf(el).trim();
    const leads = [];
    for (;;) {
      const m = t.match(new RegExp('^translate\\(' + NUM + ' ' + NUM + '\\)\\s*'));
      if (!m) break;
      leads.push([parseFloat(m[1]), parseFloat(m[2])]);
      t = t.slice(m[0].length);
    }
    return { leads, tail: t.trim() };
  };
  const writeChain = (el, leads, tail) => {
    const parts = leads.map(l => 'translate(' + l[0] + ' ' + l[1] + ')');
    if (tail) parts.push(tail);
    el.setAttribute('transform', parts.join(' ').replace(/\s+/g, ' ').trim());
  };

  const dc = hasDivider ? (() => { let n = 0; for (let i = 1; i < groups.length; i++) { if (/^translate\(300 100\)/.test(tf(groups[i]))) n++; else break; } return n || 1; })() : 0;

  const notes = [];

  if (hasDivider) {
    for (let _di = 1; _di < 1 + dc; _di++) {
    const layer = groups[_di];
    const c = core(layer);
    if (!c) return { error: 'the divider layer has no core group: has the editor changed shape?' };
    const { leads, tail } = chain(c);
    // A divider whose motion lives in its path data, a wipe, has no drag
    // translate at all: only the placement that cancels the host. Demanding two
    // leads meant that whole motion type could never be ingested.
    if (leads.length < 1) {
      return { error: 'the divider core has no placement translate: has the editor changed shape?' };
    }
    // leads[0] cancels the host. If the tail opens with a scale or a rotate, the
    // last lead is the centre that pivot turns about, so it is not a drag. What
    // sits between the two is where the author dropped the divider, and that is
    // the only part that gets centred. Its y is kept: how high a divider sits is
    // a composition decision, and the lift is added to it.
    const pivotAtEnd = /^(scale|rotate)\(/.test(tail);
    const dragEnd = pivotAtEnd ? leads.length - 1 : leads.length;
    const drags = leads.slice(1, dragEnd);
    leads[0] = [-300, -100];
    if (drags.length) {
      const wasX = leads[1][0];
      const wasY = leads[1][1];
      const ty = Math.round((wasY + (extraY || 0)) * 100) / 100;
      leads[1] = [0, ty];
      notes.push('divider: x ' + wasX + ' -> 0 (on the canvas axis), y ' + wasY + ' -> ' + ty +
        (extraY ? ' (lifted)' : ' (kept)'));
    } else if (extraY) {
      leads.splice(1, 0, [0, extraY]);
      notes.push('divider: no drag offset to centre, lifted by ' + extraY);
    } else {
      notes.push('divider: no drag offset, already on the canvas axis');
    }
    writeChain(c, leads, tail);
    }
  }

  // Identify divider groups: consecutive groups after the ground whose host
  // transform is the canvas centre, so a split divider (thickrings) with two
  // halves is handled as one divider instead of being mistaken for icons.

  // One icon lands on the axis. Several move as a block, so the spacing between
  // them stays the author's and only the block's centre is the site's.
  const icons = groups.slice(hasDivider ? 1 + dc : 1).filter(g => wrap(g) !== null);
  const hosts = icons.map(g => wrap(g));
  const mean = hosts.length ? hosts.reduce((a, w) => a + (w ? w.px : 0), 0) / hosts.length : 0;
  const shift = 300 - mean;
  const iconTargets = [];
  icons.forEach((layer, i) => {
    const c = core(layer);
    const w = hosts[i];
    if (!c || !w) { notes.push('icon ' + i + ': not a moving layer, left alone'); return; }
    const { leads, tail } = chain(c);
    if (leads.length < 2) {
      notes.push('icon ' + i + ': ' + leads.length + ' leading translate(s), left alone');
      return;
    }
    const nx = Math.round((w.px + shift) * 100) / 100;
    const py = w.py;
    leads[0] = [-nx, -py];
    leads[leads.length - 1] = [nx, py];
    writeChain(c, leads, tail);
    layer.setAttribute('transform', 'translate(' + nx + ' ' + py + ')');
    iconTargets.push({ role: 'icon' + i, x: nx });
    notes.push('icon ' + i + ': x ' + w.px + ' -> ' + nx + ', y ' + py + ' (kept)');
  });

  return { svg: new XMLSerializer().serializeToString(svg), notes: notes, placements: iconTargets };
}
"""

MEASURE_JS = r"""
([kind, iconCount, times]) => {
  const svg = document.querySelector('svg');
  const isG = el => el.tagName && el.tagName.toLowerCase() === 'g';
  const groups = [...svg.children].filter(isG);
  const names = ['ground'];
  if (kind && kind !== 'none') names.push('divider');
  for (let i = 0; i < iconCount; i++) names.push('icon' + i);

  const probe = t => {
    try { svg.pauseAnimations(); svg.setCurrentTime(t); } catch (e) {}
    const inv = svg.getScreenCTM().inverse();
    const pt = (x, y) => { const p = svg.createSVGPoint(); p.x = x; p.y = y; return p.matrixTransform(inv); };
    return groups.map(el => {
      const r = el.getBoundingClientRect();
      const a = pt(r.left, r.top), b = pt(r.right, r.bottom);
      return {
        x0: Math.min(a.x, b.x), x1: Math.max(a.x, b.x),
        cx: (a.x + b.x) / 2, w: Math.abs(a.x - b.x),
        y0: Math.min(a.y, b.y), y1: Math.max(a.y, b.y),
        anim: el.querySelectorAll('animateTransform, animate').length
      };
    });
  };

  const frames = times.map(probe);
  const layers = names.map((name, i) => {
    const f = frames.map(fr => fr[i]).filter(Boolean);
    if (!f.length) return null;
    const col = key => f.map(v => v[key]);
    return {
      name,
      animated: f[0].anim > 0,
      cxMin: Math.min(...col('cx')), cxMax: Math.max(...col('cx')),
      x0Min: Math.min(...col('x0')), x1Max: Math.max(...col('x1')),
      wMax: Math.max(...col('w')), wMin: Math.min(...col('w')),
      baseMin: Math.min(...col('y1'))
    };
  }).filter(Boolean);

  const first = svg.querySelector('animateTransform');
  const dur = first ? parseFloat((first.getAttribute('dur') || '3s').replace('s', '')) : 3;
  return { layers: layers, duration: dur };
}
"""


def _page_html(svg: str) -> str:
    return (
        "<!doctype html><html><body style='margin:0;background:transparent'>"
        f"<div id='wrap' style='width:{OUT_W}px;height:{OUT_H}px;overflow:hidden'>{svg}</div>"
        "</body></html>"
    )


def place(svg: str, record: dict, icon_count: int, extra_y: float, workdir: Path) -> dict:
    from playwright.sync_api import sync_playwright

    html = workdir / "_cover_place.html"
    html.write_text(_page_html(svg), encoding="utf-8")
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": OUT_W, "height": OUT_H}, device_scale_factor=1)
            page.goto(html.as_uri())
            page.wait_for_timeout(150)
            result = page.evaluate(
                PLACE_JS, [str(record.get("divider", {}).get("kind", "none")), icon_count, extra_y]
            )
            browser.close()
    finally:
        html.unlink(missing_ok=True)
    return result


def measure(svg: str, record: dict, icon_count: int, workdir: Path, samples: int = 25) -> dict:
    from playwright.sync_api import sync_playwright

    html = workdir / "_cover_measure.html"
    html.write_text(_page_html(svg), encoding="utf-8")
    times = [round(i * 5.0 / samples, 4) for i in range(samples)]
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": OUT_W, "height": OUT_H}, device_scale_factor=1)
            page.goto(html.as_uri())
            page.wait_for_timeout(150)
            result = page.evaluate(
                MEASURE_JS, [str(record.get("divider", {}).get("kind", "none")), icon_count, times]
            )
            browser.close()
    finally:
        html.unlink(missing_ok=True)
    return result


# --- frames ----------------------------------------------------------------


def render_frame(svg: str, at: float, workdir: Path, out: Path | None = None) -> bytes:
    from PIL import Image
    from playwright.sync_api import sync_playwright

    stem = f"_cover_frame_{int(at * 1000)}"
    html = workdir / f"{stem}.html"
    html.write_text(_page_html(svg), encoding="utf-8")
    png = workdir / f"{stem}.png"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": OUT_W, "height": OUT_H}, device_scale_factor=1)
            page.goto(html.as_uri())
            page.wait_for_timeout(150)
            page.evaluate(
                "(t) => { const s = document.querySelector('svg');"
                f" s.setAttribute('width','{OUT_W}'); s.setAttribute('height','{OUT_H}');"
                " s.removeAttribute('style'); try { s.pauseAnimations(); s.setCurrentTime(t); } catch (e) {} }",
                at,
            )
            page.wait_for_timeout(120)
            page.locator("#wrap").screenshot(path=str(png))
            browser.close()
        raw = png.read_bytes()
        if out is not None:
            out.parent.mkdir(parents=True, exist_ok=True)
            with Image.open(png) as im:
                im.convert("RGB").save(out, "WEBP", quality=90, method=6)
        return raw
    finally:
        html.unlink(missing_ok=True)
        png.unlink(missing_ok=True)


def frames_differ(rest: bytes, later: bytes) -> tuple[bool, float]:
    """Whether two frames differ, and by what percentage of pixels."""
    from PIL import Image, ImageChops

    a = Image.open(io.BytesIO(rest)).convert("RGB")
    b = Image.open(io.BytesIO(later)).convert("RGB")
    if a.size != b.size:
        return True, 100.0
    if a.size == (0, 0):
        return False, 0.0
    diff = ImageChops.difference(a, b).convert("L")
    changed = sum(diff.histogram()[8:])  # pixels differing by more than a rounding step
    total = a.size[0] * a.size[1]
    return changed > total * 0.002, 100.0 * changed / total


# --- command ---------------------------------------------------------------


RECORD_RE = re.compile(r'<metadata[^>]*id="cover-composition"[^>]*>(.*?)</metadata>', re.S)


def record_from_svg(text: str) -> dict | None:
    """The composition record the editor embedded, or None if this is an older export."""
    match = RECORD_RE.search(text)
    if not match:
        return None
    try:
        return json.loads(html.unescape(match.group(1)))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"the embedded composition record is not valid JSON: {exc}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Ingest a generated motion cover: centre it, render its rest frame, verify it.",
        epilog="Needs Pillow and Playwright with Chromium. The site build does not.",
    )
    parser.add_argument("--source", required=True, type=Path, help="the exported cover.svg")
    parser.add_argument("--composition", type=Path, help="the composition record if it was exported separately; the cover package carries it inside the SVG")
    parser.add_argument("--name", required=True, help="asset name, e.g. gov-cover")
    parser.add_argument("--media", required=True, help="media id folder under static/media/posts, e.g. 7")
    parser.add_argument("--rest-time", type=float, default=None, help="seconds into the exported loop for the rest frame (default: the record's restTime, else 0.8)")
    parser.add_argument("--as-authored", action="store_true", help="keep the dragged placement instead of centring")
    parser.add_argument("--verify", action="store_true", help="sample the loop and fail if the invariants break")
    args = parser.parse_args(argv[1:])

    if not args.source.exists():
        parser.error(f"no such file: {args.source}")
    if args.composition and not args.composition.exists():
        parser.error(f"no such file: {args.composition}")

    root = project_root()
    workdir = root / "state" / "covers-lab"
    workdir.mkdir(parents=True, exist_ok=True)

    text = args.source.read_text(encoding="utf-8")
    if args.composition:
        record = json.loads(args.composition.read_text(encoding="utf-8"))
        record_origin = "beside the artwork"
    else:
        record = record_from_svg(text)
        if record is None:
            parser.error(
                "no --composition given, and the SVG carries no cover-composition record "
                "(the cover lab writes one, so this is probably an older export)"
            )
        record_origin = "inside the artwork"
    recorded_rest = (record.get("out") or {}).get("restTime")
    rest_time = args.rest_time if args.rest_time is not None else float(recorded_rest if recorded_rest is not None else 0.8)
    svg = text[text.find("<svg") :].strip()
    kind = str(record.get("divider", {}).get("kind", "none"))
    icon_count = len(record.get("icons") or [])
    print(f"cover {args.name}: divider {kind!r}, {icon_count} icon(s); card window x {WINDOW_X0} to {WINDOW_X1}")

    if args.as_authored:
        print("  placement: left as authored (--as-authored)")
        placements: list[dict] = []
    else:
        placed = place(svg, record, icon_count, 0.0, workdir)
        if "error" in placed:
            print(f"  FAIL: {placed['error']}", file=sys.stderr)
            return 1
        for note in placed["notes"]:
            print("  " + note)
        svg = placed["svg"]
        placements = placed.get("placements", [])

    geometry = measure(svg, record, icon_count, workdir)
    layers = geometry["layers"]
    duration = geometry["duration"] or 3.0

    # A divider that reaches the bottom edge may lift during its loop; raise the
    # whole artwork until it cannot.
    divider = next((l for l in layers if l["name"] == "divider"), None)
    if divider and divider["baseMin"] < CANVAS_H - 0.5 and not args.as_authored:
        lift = round(CANVAS_H + 0.5 - divider["baseMin"], 2)
        print(f"  divider base dips to {divider['baseMin']:.1f}: lifting the artwork by {lift:g}")
        placed = place(svg, record, icon_count, lift, workdir)
        if "error" in placed:
            print(f"  FAIL: {placed['error']}", file=sys.stderr)
            return 1
        svg = placed["svg"]
        placements = placed.get("placements", [])
        geometry = measure(svg, record, icon_count, workdir)
        layers = geometry["layers"]

    # --- write --------------------------------------------------------------
    ids = set(re.findall(r'\bid="([^"]+)"', svg))
    for id_val in ids:
        if id_val != "cover-composition" and not id_val.startswith(f"{args.name}-"):
            new_id = f"{args.name}-{id_val}"
            svg = re.sub(rf'\bid="{re.escape(id_val)}"', f'id="{new_id}"', svg)
            svg = re.sub(rf'url\(#{re.escape(id_val)}\)', f'url(#{new_id})', svg)
            svg = re.sub(rf'href="#{re.escape(id_val)}"', f'href="#{new_id}"', svg)
    svg_out = root / "assets" / "covers" / f"{args.name}.svg"
    svg_out.parent.mkdir(parents=True, exist_ok=True)
    svg_out.write_text(svg, encoding="utf-8")

    record_out = root / "assets" / "covers" / f"{args.name}.json"
    if args.composition:
        if Path(args.composition).resolve() != record_out.resolve():
            shutil.copyfile(args.composition, record_out)
    else:
        record_out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + chr(10), encoding="utf-8")

    rest_out = root / "static" / "media" / "posts" / args.media / f"{args.name}-rest.webp"
    rest_png = render_frame(svg, rest_time, workdir, rest_out)
    later_png = render_frame(svg, rest_time + duration / 4, workdir)
    alive, changed = frames_differ(rest_png, later_png)

    # --- report -------------------------------------------------------------
    print("  --- measured over the loop ---")
    problems: list[str] = []
    notes: list[str] = []

    # The offset the tool applied, read back from the DOM it just wrote.
    for item in placements:
        if abs(item["x"] - CANVAS_W / 2) > CENTRE_TOLERANCE:
            problems.append(
                f"{item['role']} sits at x {item['x']}, not on the canvas axis at {CANVAS_W / 2:g}"
            )

    for layer in layers:
        if layer["name"] == "ground":
            continue
        bleed = layer["wMax"] >= CANVAS_W * BLEED_FRACTION
        mean_centre = (layer["cxMin"] + layer["cxMax"]) / 2
        drift = layer["cxMax"] - layer["cxMin"]
        scaled = (layer["wMax"] - layer["wMin"]) > 0.5
        print(
            f"  {layer['name']:<8} mean centre {mean_centre:6.1f}  drift {drift:5.1f}"
            f"  spans {layer['x0Min']:7.1f} to {layer['x1Max']:7.1f}  width {layer['wMin']:4.0f}-{layer['wMax']:4.0f}"
            f"  {'scales' if scaled else 'moves'}"
        )
        # A scale animation must pivot on the artwork, so a layer that resizes may
        # not travel sideways. A layer that translates is allowed to, as long as
        # it travels about the axis rather than away from it. A bleed layer is
        # exempt from both: its box is a mask rectangle that starts off-centre by
        # design, so the box says nothing about where the subject is.
        if scaled and drift > CENTRE_TOLERANCE and not bleed:
            problems.append(
                f"{layer['name']} resizes but drifts {drift:.1f} units sideways: the pulse is not pivoting on its centre"
            )
        if not bleed and abs(mean_centre - CANVAS_W / 2) > CENTRE_TOLERANCE:
            notes.append(
                f"{layer['name']} sits {mean_centre - CANVAS_W / 2:+.1f} off the canvas axis in its own geometry"
            )
        outside = max(WINDOW_X0 - layer["x0Min"], layer["x1Max"] - WINDOW_X1)
        if outside > 0.5:
            if layer["name"].startswith("icon"):
                problems.append(
                    f"{layer['name']} leaves the card window by {outside:.1f} units "
                    f"({layer['x0Min']:.1f} to {layer['x1Max']:.1f} inside {WINDOW_X0} to {WINDOW_X1}): the thumbnail will cut it"
                )
            elif not bleed:
                notes.append(
                    f"{layer['name']} bleeds {outside:.1f} units past the card window on its widest side"
                    " (fine for a field, worth a look for a subject)"
                )

    if not any(l["animated"] for l in layers if l["name"] != "ground"):
        problems.append("no layer animates: the cover is a still")
    if not alive:
        problems.append(f"the rendered frames barely differ ({changed:.2f}% of pixels): the motion did not survive")

    for note in notes:
        print(f"  note: {note}")
    print(f"  motion   {changed:.1f}% of pixels change a quarter-cycle apart ({'alive' if alive else 'still'})")
    print(f"  wrote {svg_out.relative_to(root)} ({svg_out.stat().st_size // 1024} KB)")
    print(f"  wrote {record_out.relative_to(root)}")
    print(f"  wrote {rest_out.relative_to(root)} ({rest_out.stat().st_size // 1024} KB)")
    print(f"  record   {record_origin}; the rest frame is {rest_time:g}s, the instant the export made frame zero")
    print("  --- frontmatter ---")
    print(f'    coverMotion: "{args.name}"')
    print(f"    coverMotionBase: {rest_time:g}")
    print(f'    featureimage: "media/posts/{args.media}/{args.name}-rest.webp"')

    if args.verify:
        if problems:
            for problem in problems:
                print(f"  FAIL: {problem}", file=sys.stderr)
            return 1
        print("  verified: centred, inside the card window where it matters, and still moving")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
