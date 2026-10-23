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
| `content/gallery.md` | The page that shows every figure |
| `layouts/` | The theme, ported from the Publii "simple" theme |
| `layouts/shortcodes/embed.html` | The shortcode that places a figure in a post |
| `static/` | The stylesheet, the script, the fonts, the media and the content manager |
| `assets/embeds/` | The twenty-three figures, as self-contained HTML |
| `data/site.json` | The settings the theme reads: title, hero, menu, comments |
| `data/media.json` | Every image with its responsive set and its size |
| `data/embeds.json` | The figures, with the title, the kind and the essay each one fits |
| `tools/` | The scripts that build the site and check it against the old build |

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

## What the reader gets

**A colour mode.** The site follows the operating system and the button in the
header overrides it, and the choice is remembered in the browser. The two token
sets live in `layouts/partials/custom-css.html`, and the figures in the essays
read the same tokens, so they change with the site.

**A table of contents** in the essays that have sections, a reading time, a
bar showing how far through the essay the reader is, and a click on any image
to open it larger.

**A gallery** at `/gallery/` with every figure, each one live in the page.

## Putting a figure in an essay

The figures are self-contained: their own CSS and their own JavaScript, no
external requests, no storage, nothing sent. A post places one with a single
line:

```
{{< embed "trade-off-frontier" >}}
```

The shortcode reads the file from `assets/embeds/` and inlines it, so the
figure is part of the document rather than a separate frame. It therefore
inherits the site's fonts, the site's colours and the site's colour mode,
which an embedded frame could never do.

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
colour mode, the table of contents, the reading time, the zoom, the progress
bar and the gallery) are not part of the comparison.

## Where the content came from

The essays were extracted from the Publii site with `tools/extract_publii.py`,
which reads the desktop app's database and writes Markdown. It is kept for the
record and for the next import; the site no longer depends on it. It also
writes the dark variant of the wordmark and removes the background colour the
old theme had compiled into its stylesheet, because that colour would have won
over any colour scheme.

The figures were built for the old site and live in the vault at
`vault/Areas/Blog/embeds/`. Their published copies are here, with their
colours repointed at the shared tokens.

One deliberate difference from the old build is worth knowing about. Headings
inside an essay are level two rather than level one, so the outline of each
page is correct. And a paragraph that sat in front of an image inside a figure
stays outside the figure, which means it is aligned with the rest of the text.
