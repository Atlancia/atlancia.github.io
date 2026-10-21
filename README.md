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
| `content/authors/`, `content/tags/` | The author and tag pages |
| `layouts/` | The theme, ported from the Publii "simple" theme |
| `static/` | The stylesheet, the script, the fonts, the media and the content manager |
| `data/site.json` | The settings the theme reads: title, hero, menu, comments |
| `data/media.json` | Every image with its responsive set and its size |
| `tools/` | The scripts that build the site and check it against the old build |

## Building

```
python tools/build.py
```

That regenerates the media registry, then renders the site into `public/`.
Hugo is needed on the path, version 0.148 or later with the extended build.

## Editing in the browser

The content manager lives at `/admin/`. Signing in uses an access token: create
a fine-grained token with **Contents: read and write** for this repository
only, then paste it into the sign-in dialog. The token is kept in the browser
and never written to the repository.

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

## Where the content came from

The essays were extracted from the Publii site with `tools/extract_publii.py`,
which reads the desktop app's database and writes Markdown. It is kept for the
record and for the next import; the site no longer depends on it.

Two deliberate differences from the old build are worth knowing about. Headings
inside an essay are level two rather than level one, so the outline of each
page is correct. And a paragraph that sat in front of an image inside a figure
stays outside it, which means it is aligned with the rest of the text rather
than centred.
