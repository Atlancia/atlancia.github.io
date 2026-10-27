# Atlancia

The source of [atlancia.com](https://atlancia.com).

The essays live here as Markdown. The site is built with Hugo, and the content
is edited either in a text editor or in the browser through Sveltia CMS at
`/admin/`, which commits to this repository and lets the build publish the
result.

## Layout

| Path | What it holds |
|---|---|
| `content/posts/` | The essays, one Markdown file each |
| `layouts/` | The theme, ported from the Publii "simple" theme |
| `static/` | The stylesheet, the script, the fonts, the media and the content manager |
| `data/site.json` | The settings the theme reads: title, hero, menu, comments |
| `data/media.json` | Every image with its responsive set and its size |
| `tools/` | The scripts that build the site and check it against the old build |
| `tools/embeds/` | The figures, parked. Not published, not referenced, awaiting a rebuild |

## Building

```
python tools/build.py
```

That regenerates the media registry, then renders the site into `public/`.
Hugo ships with the repository, at
`tools/bin/hugo-0.167.0-extended-windows-amd64.exe`. It is version 0.167
extended, nothing has to be installed, and nothing has to be on the path, so
the build travels with the clone. Blowfish v3.9.0 needs at least 0.162 and the
0.148 build fails on it. To serve the site while writing:

```
tools\bin\hugo-0.167.0-extended-windows-amd64.exe server -D
```

`tools/build.py` uses `HUGO` from the environment when it is set, then the
binary in `tools/bin`, then `~/bin`, then `hugo` on the path.

For a copy that loads its own assets, which is what a local server needs:

```
python tools/build.py public_local http://localhost:8765/
```

## A cover that moves

A cover can be an animation that waits for the reader. The essay opts in with
two frontmatter keys, and the feature image points at the resting frame:

```
featureimage: "media/posts/7/gov-cover-rest.webp"
coverMotion: "gov-cover"
coverMotionBase: 0
```

`coverMotion` names a file in `assets/covers`. The SVG is inlined into the page
rather than pointed at with an `<img>`, because an image cannot be paused. It
holds still on the frame named by `coverMotionBase`, runs on hover, focus or
tap, and stays still for a reader who asks for reduced motion. The resting frame
also feeds the RSS feed, the sitemap and the list thumbnails.

The editor asks for an export point: the instant of the loop whose pose you want
as the still. The export rotates the loop so that instant becomes frame zero,
which is why `coverMotionBase` is 0. The animation therefore starts on exactly
the pose the poster shows instead of jumping into it a moment later, and the
icons start their own motion from the same place. Covers exported before the
editor did this rest at 0.8; their records carry no hold time, so the tool keeps
defaulting to 0.8 for them.

Ingest a cover with:

```
python tools/cover_motion.py --source <cover.svg> --name gov-cover --media 7 --verify
```

The editor's Cover package button writes one file: the animated SVG with its
composition record inside a `<metadata>` element, so the artwork and the intent
cannot be separated or mismatched on the way here. The tool reads the record out
of it and prints the frontmatter to paste. Passing `--composition` still works,
for an export that came as a pair.

It writes three things: `assets/covers/<name>.svg`, the composition record beside
it as `assets/covers/<name>.json` so any cover can be reloaded into the editor
and edited again, and `static/media/posts/<media>/<name>-rest.webp`, the resting
frame.

The artwork is 3:1 and the site uses it at two shapes. The hero shows it whole.
The list thumbnail is 300 by 180 and holds it with `slice`, so only the middle
three fifths of the canvas survives, which is `x` 133 to 467. Anything that has
to be read belongs in that window; a field of colour or a spotlight is welcome
to bleed off the sides. The tool measures where the artwork actually sits over
its whole loop and fails if an icon leaves the window, and it names how far a
divider bleeds so the crop is a decision rather than a surprise.

Placement is not the author's to get wrong: every cover is centred, and every
motion happens about that centre. The editor works in drag offsets, so a cover
composed by eye drifts off axis, and an off-axis subject is exactly what a card
crop cuts in half. The tool anchors the divider on the canvas axis, keeps its
height, and moves the icons onto the same axis as a block. That also re-pivots
any pulse that the export scaled about the canvas corner.

Finally it checks the one thing numbers cannot show: it renders the resting
frame and a frame a quarter of a cycle later and fails unless they differ. A
cover that is centred and still is a cover that broke.

`--as-authored` keeps the dragged placement instead.

The tool needs Pillow and Playwright. `tools/build.py` needs neither.

The editor itself is `tools/cover-lab.html`. Open it in a browser, nothing to
install. Each icon carries its own motion, speed, direction and phase, so two
icons can counter-rotate.

Scrub to the pose you want as the still, press Export point, then Cover package.
That is the whole round trip: one SVG, record inside, straight into the ingest
above. WebP still is there for looking at the poster on its own, at the same
instant. The PNG, PNG sequence and WebM exports are gone, because no part of the
site ever consumed them.

## What the reader gets

**A colour mode.** The site follows the operating system and the button in the
header overrides it, and the choice is remembered in the browser. The two token
sets live in `layouts/partials/custom-css.html`. When the figures come back they
will read those same tokens, so that they change with the site.

**A table of contents** in the essays that have sections, a reading time, a
bar showing how far through the essay the reader is, and a click on any image
to open it larger.


## The figures are parked

The twenty-four interactive figures are no longer part of the site. They were
built against an earlier visual language, most of them draw their insides in
literal dark greys that a light mode cannot follow, and the decision was to
rebuild them rather than patch them. Keeping them published while that happens
would have meant shipping pages the author had already judged unfinished.

They now live in `tools/embeds/`, beside the cover editor and for the same
reason: `tools/` is not built, not served and not linked. Nothing in the site
references them. The gallery page, its template, the `embed` shortcode, the
figures index and the stylesheet block that framed them were removed in the same
change, so there is no half-wired surface left behind.

Before one comes back it needs three things: a rendering that follows the site's
colour tokens instead of literal greys, the `atlx` wrapper class on its root
element (which is what gives it a maximum width and its own sideways scroll), and
a decision about which essay paragraph earns it.

## Editing in the browser

The content manager lives at `/admin/`. Signing in uses an access token:
create a fine-grained token with **Contents: read and write** for this
repository only, then paste it into the sign-in dialog. The token is kept in
the browser and never written to the repository.

Sveltia CMS signs its commits, so every change to the content is attributable.

## Publishing

A push to `main` runs `.github/workflows/deploy.yml`, which builds the site and
pushes it to `Atlancia/atlancia.github.io` on the `master` branch, the
repository GitHub Pages serves. The workflow needs a `DEPLOY_TOKEN` secret: a
fine-grained token with **Contents: read and write** for
`Atlancia/atlancia.github.io` only.

Nothing else about the hosting changes. The addresses, the feeds, the sitemap
and the files behind Cloudflare stay as they were.

## Checking the port

`tools/compare_build.py` compares a build against the HTML the previous Publii
site published, element by element, and reports anything that differs. It was
written for the move, and it is the fastest way to see whether a change to the
theme has moved anything on the page.

```
python tools/compare_build.py <the old build folder> public
```

The differences it folds away are the ones the port made on purpose: body
headings are level two, the editor's utility classes are gone, a figure is no
longer wrapped in a second figure, and the parts the new build added (the
colour mode, the table of contents, the reading time, the zoom and the progress
bar) are not part of the comparison.

## Where the content came from

The essays were extracted from the Publii site with `tools/extract_publii.py`,
which reads the desktop app's database and writes Markdown. It is kept for the
record and for the next import; the site no longer depends on it. It also
writes the dark variant of the wordmark and removes the background colour the
old theme had compiled into its stylesheet, because that colour would have won
over any colour scheme.

The figures were built for the old site and live in the vault at
`vault/Areas/Blog/embeds/`. Their parked copies are in `tools/embeds/`, with their
colours repointed at the shared tokens.

One deliberate difference from the old build is worth knowing about. Headings
inside an essay are level two rather than level one, so the outline of each
page is correct. And a paragraph that sat in front of an image inside a figure
stays outside the figure, which means it is aligned with the rest of the text.
