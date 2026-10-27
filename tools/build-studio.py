"""Regenerate tools/figure-studio.html from tools/studio-template.html.

Scans every post for pasted figure blocks (div.atlx.atlx-XXX), finds the
matching source file under tools/embeds/, and bakes the whole index
(source texts + post texts) into the studio page so it can list every
post and the figures inside it with no file hunting.

Usage:  python tools/build-studio.py
"""
import json
import re
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = sorted((ROOT / 'content' / 'posts').glob('*.md'))
EMBEDS = sorted((ROOT / 'tools' / 'embeds').glob('*.html'))
TEMPLATE = ROOT / 'tools' / 'studio-template.html'
OUT = ROOT / 'tools' / 'figure-studio.html'

CLASS_RE = re.compile(r'<div class="atlx (atlx-[a-z0-9-]+)"')


def main():
    # map figure class -> source file (first embed containing the class)
    src_by_class = {}
    src_text = {}
    for f in EMBEDS:
        t = f.read_text(encoding='utf-8')
        for cls in CLASS_RE.findall(t):
            src_by_class.setdefault(cls, f.name)
            src_text.setdefault(cls, t)

    entries = []
    for post in POSTS:
        md = post.read_text(encoding='utf-8')
        classes = []
        for cls in CLASS_RE.findall(md):
            if cls not in classes:
                classes.append(cls)
        if not classes:
            continue
        for cls in classes:
            entries.append({
                'post': post.name,
                'cls': cls,
                'srcFile': src_by_class.get(cls),
                'srcText': src_text.get(cls),
                'mdText': md,
            })

    missing = [e for e in entries if not e['srcFile']]
    index = {
        'built': time.strftime('%Y-%m-%d %H:%M'),
        'entries': entries,
    }
    tpl = TEMPLATE.read_text(encoding='utf-8')
    assert '/*__FIGURE_INDEX__*/' in tpl, 'template placeholder missing'
    payload = 'var FIGURE_INDEX = ' + json.dumps(index) + ';'
    # Figure sources contain their own <script> blocks: a literal </script>
    # inside the payload would close the index <script> tag early and break
    # the page. <\/ is a valid string escape and parses identically.
    payload = payload.replace('</', '<\\/')
    OUT.write_text(tpl.replace('/*__FIGURE_INDEX__*/', payload), encoding='utf-8')
    (ROOT / 'tools' / 'figure-studio-app.js').write_text(
        (ROOT / 'tools' / 'studio-app.js').read_text(encoding='utf-8'), encoding='utf-8')

    n_src = sum(1 for e in entries if e['srcText'])
    print(f'posts with figures: {len(set(e["post"] for e in entries))}')
    print(f'figure entries: {len(entries)} ({n_src} with source, {len(missing)} missing source)')
    for e in missing:
        print('  NO SOURCE:', e['post'], e['cls'])
    print(f'studio bytes: {OUT.stat().st_size}')
    print('wrote', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
