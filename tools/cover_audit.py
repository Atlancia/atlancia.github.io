#!/usr/bin/env python3
"""Audit every option the cover editor offers against the exported artifact.

The editor's menu was written from its canvas engine, and the SVG export was
written underneath it afterwards. That let the menu offer options the exporter
never learned: ground pulse emits no animation, icon spin emits one that throws
the icon off the canvas, dither and bayer emit nothing at all. The canvas
preview cannot show any of it, because the canvas is the half that works.

So this checks the artifact, not the editor:

  motion   does the artwork actually move between frame zero and a quarter cycle?
  visual   does choosing this option change the render at all, against its
           family's baseline?

    python tools/cover_audit.py              # gate: exit 1 on a new inert option
    python tools/cover_audit.py --json out   # machine-readable rows
    python tools/cover_audit.py --all        # include the passing rows in the table

Exit codes: 0 every option does something (known defects aside), 1 a new inert
option, 2 usage or environment error.

Needs Pillow and Playwright with Chromium. The site build needs neither.
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
LAB = (ROOT / "tools" / "cover-lab.html").as_uri()
W, H = 600, 200

FILLS = ["solid", "vgrad", "hgrad", "dgrad", "radial", "conic"]
DIVIDERS = [
    "none", "vertical", "horizontal", "diagonal", "diagonal-rev", "wave", "wave-top",
    "arc-left", "arc-right", "circle", "circle-left", "circle-right", "diamond",
    "triangle", "triangle-top", "blob", "scatter", "thickbands", "thickhoriz", "thickrings",
]
GROUND_MOTIONS = ["none", "rotate", "sweep-x", "sweep-y", "pulse"]
ICON_MOTIONS = ["none", "spin", "float", "pulse", "orbit", "sway", "wobble"]
DIVIDER_MOTIONS = ["none", "wipe", "slide-x", "slide-y", "spin", "breathe", "iris", "sway", "drift", "pulse-outline"]
TREATMENTS = ["none", "grain-light", "grain-heavy", "vignette", "glow", "halftone", "dither", "bayer", "posterize", "duotone"]

# Verified inert on 2026-10-25. Each one is a real defect, kept here so the gate
# stays green while the fix is pending, and so forgetting them is not possible.
# If one of these starts working the run fails, which is the prompt to remove it.
KNOWN_INERT = {
    ("divider motion", "wipe on thickhoriz"): "wipe moves a split boundary, and a banded divider has none",
}

MOTION_FLOOR_PCT = 0.01   # below this a frame pair is the same picture


def build_cases() -> list[dict]:
    """Every option, plus the baseline the visual families are compared against.

    A baseline is not a candidate: `none` is correct at zero change, so scoring it
    would report five defects on every run and teach everyone to ignore the gate.
    """
    cases: list[dict] = []
    for v in GROUND_MOTIONS:
        cases.append({"family": "ground motion", "value": v, "kind": "motion",
                      "patch": {"anim.base": v}, "baseline": v == "none"})
    for v in ICON_MOTIONS:
        cases.append({"family": "icon motion", "value": v, "kind": "motion",
                      "patch": {"anim.icon": v, "icon": True}, "baseline": v == "none"})
    for v in DIVIDER_MOTIONS:
        for shape in ("vertical", "thickhoriz"):   # a motion can be wired to one kind
            cases.append({"family": "divider motion", "value": f"{v} on {shape}", "kind": "motion",
                          "patch": {"divider.kind": shape, "divider.motion": v}, "baseline": v == "none"})
    for v in FILLS:
        cases.append({"family": "fill", "value": v, "kind": "visual",
                      "patch": {"a.type": v}, "baseline": v == "solid"})
    for v in DIVIDERS:
        cases.append({"family": "divider kind", "value": v, "kind": "visual",
                      "patch": {"divider.kind": v}, "baseline": v == "none"})
    for v in TREATMENTS:
        cases.append({"family": "treatment", "value": v, "kind": "visual",
                      "patch": {"treat.type": v}, "baseline": v == "none"})
    return cases


BASELINE_PATCH = {"fill": {"a.type": "solid"},
                  "divider kind": {"divider.kind": "none"},
                  "treatment": {"treat.type": "none"}}

APPLY = """(patch) => {
  S = defaultState();
  selectedIconIdx = -1;
  S.anim.duration = 4;
  if (patch.icon) {
    const name = Object.keys(EMBEDDED_ICONS).sort()[0];
    S.icons = [{ name, x: 300, y: 100, size: 88, color: '#ffc074', alpha: 100 }];
    selectedIconIdx = 0;
  }
  for (const [k, v] of Object.entries(patch)) {
    if (k === 'icon') continue;
    const [head, tail] = k.split('.');
    if (tail) S[head][tail] = v; else S[head] = v;
  }
  const built = svgBuild(S, { animate: true, scale: 1 });
  return { svg: built.svg, duration: Number(S.anim.duration) || 3 };
}"""


def pct_diff(a: bytes, b: bytes) -> float:
    ia = Image.open(io.BytesIO(a)).convert("RGB")
    ib = Image.open(io.BytesIO(b)).convert("RGB")
    if ia.size != ib.size:
        ib = ib.resize(ia.size)
    pa = np.asarray(ia, dtype=np.int16)
    pb = np.asarray(ib, dtype=np.int16)
    differing = np.any(pa != pb, axis=2)
    return float(differing.mean() * 100)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Check that every option the cover editor offers changes the exported cover.",
        epilog="Exit 0 when nothing new is inert. Needs Pillow, numpy and Playwright with Chromium.",
    )
    parser.add_argument("--json", type=Path, help="write the full result rows here")
    parser.add_argument("--all", action="store_true", help="print passing rows as well as failures")
    args = parser.parse_args(argv[1:])

    if not (ROOT / "tools" / "cover-lab.html").exists():
        print(f"no cover-lab.html under {ROOT}", file=sys.stderr)
        return 2

    results: list[dict] = []
    cases = build_cases()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 700, "height": 300})
        editor = ctx.new_page()
        editor_errors: list[str] = []
        editor.on("pageerror", lambda e: editor_errors.append(str(e)[:140]))
        editor.goto(LAB)
        editor.wait_for_timeout(900)
        icon_count = editor.evaluate("() => Object.keys(EMBEDDED_ICONS).length")

        viewer = ctx.new_page()
        viewer.set_viewport_size({"width": W + 20, "height": H + 20})

        def shot(svg: str, t: float | None = None, play: float | bool = False) -> bytes:
            viewer.set_content("<body style='margin:0;background:#808080'>" + svg + "</body>")
            viewer.wait_for_timeout(250)
            if t is not None and not play:
                viewer.evaluate("""(t) => {
                    const s = document.querySelector('svg');
                    if (s && s.pauseAnimations) { s.pauseAnimations(); s.setCurrentTime(t); }
                }""", t)
                viewer.wait_for_timeout(150)
            if play:
                viewer.wait_for_timeout(int(play * 1000))
            return viewer.screenshot(clip={"x": 0, "y": 0, "width": W, "height": H})

        baseline: dict[str, bytes] = {}
        for family, patch in BASELINE_PATCH.items():
            baseline[family] = shot(editor.evaluate(APPLY, patch)["svg"])

        for case in cases:
            built = editor.evaluate(APPLY, case["patch"])
            svg, duration = built["svg"], built["duration"]
            row = {"family": case["family"], "value": case["value"], "kind": case["kind"],
                   "kb": round(len(svg) / 1024, 1), "baseline": case["baseline"]}
            if case["kind"] == "motion":
                # One document, two screenshots: a fresh document per frame hides
                # animations that need a moment to start.
                viewer.set_content("<body style='margin:0;background:#808080'>" + svg + "</body>")
                viewer.wait_for_timeout(400)
                a = viewer.screenshot(clip={"x": 0, "y": 0, "width": W, "height": H})
                viewer.wait_for_timeout(700)
                b = viewer.screenshot(clip={"x": 0, "y": 0, "width": W, "height": H})
                row["metric"] = round(pct_diff(a, b), 3)
                row["inert"] = row["metric"] < MOTION_FLOOR_PCT
                row["verdict"] = "moves" if not row["inert"] else "STILL"
            else:
                row["metric"] = 0.0 if case["baseline"] else round(pct_diff(baseline[case["family"]], shot(svg)), 3)
                row["inert"] = (not case["baseline"]) and row["metric"] <= 0.0
                row["verdict"] = "baseline" if case["baseline"] else ("changes" if not row["inert"] else "NO EFFECT")
            results.append(row)

        browser.close()

    if args.json:
        args.json.write_text(json.dumps(results, indent=1), encoding="utf-8")

    candidates = [r for r in results if not r["baseline"]]
    inert = [r for r in candidates if r["inert"]]
    unexpected: list[dict] = []
    fixed: list[tuple[str, str]] = []
    for row in inert:
        key = (row["family"], row["value"])
        if key not in KNOWN_INERT:
            unexpected.append(row)
    for key, reason in KNOWN_INERT.items():
        still_broken = any(r["family"] == key[0] and r["value"] == key[1] for r in inert)
        if not still_broken:
            fixed.append(key)

    print(f"cover audit: {len(candidates)} options across 6 families, {icon_count} embedded icons\n")
    if args.all:
        family = None
        for row in results:
            if row["family"] != family:
                family = row["family"]
                print(f"\n{family.upper()}")
                print(f"  {'option':<30} {'delta %':>8}  verdict")
            print(f"  {row['value']:<30} {row['metric']:>8}  {row['verdict']}")
        print()

    ok = len(candidates) - len(inert)
    print(f"{ok}/{len(candidates)} options change the exported cover")

    if inert:
        print(f"\n{len(inert)} inert:")
        for row in inert:
            key = (row["family"], row["value"])
            tag = "known" if key in KNOWN_INERT else "NEW"
            print(f"  [{tag}] {row['family']}: {row['value']} ({row['metric']}%)")
            reason = KNOWN_INERT.get(key)
            if reason:
                print(f"          {reason}")

    for key in fixed:
        print(f"\n  now works: {key[0]}: {key[1]}. Remove it from KNOWN_INERT.")

    if editor_errors:
        print(f"\neditor raised: {editor_errors[:5]}")
        return 2
    if unexpected or fixed:
        return 1
    print("\nno new inert options")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
