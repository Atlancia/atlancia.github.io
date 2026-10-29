---
title: 'From Shovels to Software: Why Difference Matters When Things Get Complex'
date: 2023-06-05T00:00:00-04:00
slug: diversity-complexity
featureimage: covers/shovel-cover.svg
authors:
  - liam
draft: false
coverMotion: shovel-cover
coverMotionBase: 0.8
lastmod: 2025-08-23T08:28:51-04:00
media_id: 4
meta_robots: index, follow
type: posts
url: /diversity-complexity.html
---

> In many creative activities the medium of execution is intractable. Lumber splits; paints smear; electrical circuits ring. These physical limitations of the medium constrain the ideas that may be expressed, and they also create unexpected difficulties in the implementation.
>
> Implementation, then, takes time and sweat both because of the physical media and because of the inadequacies of the underlying ideas. We tend to blame the physical media for most of our implementation difficulties; for the media are not “ours” in the way the ideas are, and our pride colors our judgment.
>
> - "The Mythical Man-Month" - Fred Brooks, 1975.

In the nearly half century since Fred Brooks articulated the idea of a “mythical man month,” the myth persists. He attributed the myth to optimism, that software development is a “modern sorcery that especially attracts those who believe in happy endings and fairy godmothers.”

The persistent mythology, that if we close our eyes, and think hard enough, that we can put together a perfectly tractable plan of what we want to build, how we can build it and who will need to pull it together, is an optimistic delusion. This optimism has real consequences, and I’ve witnessed language used by those concerned with diversity that reflects this as a foundation for some of their resistance to accepting diversity and inclusion not simply as a moral imperative, but as a benefit to improved performance.

Workplaces rarely suffer from a shortage of complicated problems but they stumble when the work turns complex. Complicated work can be mastered through repetition and expert analysis. Complex work cannot: its parts are tightly coupled, its outcomes variable, and its rules unwritten. Connecting complexity theory with team dynamics has helped me see with a clearer lens on why difference matters most where predictability ends.

## The Complicated and the Complex

<!-- Atlancia embed: Diversity and complexity - Stacey matrix zone explorer (interactive).
     Fits the post From Shovels to Software: Why Difference Matters When Things Get Complex.
     Click a zone to see what it means, with examples from the essay.
     slop-ok: exclamation marks are logical-not operators in inline script, not prose emphasis. -->
<div class="atlx atlx-div-stacey">
  <style>
    .atlx-div-stacey {
      --ds-ink: var(--atl-ink, #EEEDED);
      --ds-text: var(--atl-figure-text, #BFBFBF);
      --ds-dim: var(--atl-dim, #9D9D9D);
      --ds-line: var(--atl-line, #373737);
      --ds-surface: var(--atl-surface, #1e1e1e);
      --ds-blue: var(--atl-info, #5B9ED5);
      --ds-green: var(--atl-success, #54A468);
      --ds-amber: var(--atl-accent, #FFC074);
      --ds-purple: #a78bfa;
      font-family: "Cal Sans", ui-sans-serif, system-ui, sans-serif;
      background: var(--ds-surface);
      color: var(--ds-text);
      border: 1px solid var(--ds-line);
      border-radius: 6px;
      padding: 1.3rem 1.3rem 1.1rem;
      margin: 2.5rem 0;
      max-width: 100%;
      font-size: 1rem;
      line-height: 1.55;
    }
    .atlx-div-stacey * { box-sizing: border-box; }
    .atlx-div-stacey .atlx-ds-title {
      margin: 0 0 .2rem;
      font-family: "Young Serif", Georgia, serif;
      font-weight: 500;
      font-size: 1.25rem;
      line-height: 1.35;
      color: var(--ds-ink);
    }
    .atlx-div-stacey .atlx-ds-sub {
      margin: 0 0 .3rem;
      color: var(--ds-dim);
      font-size: .95rem;
    }
    .atlx-div-stacey svg { display: block; width: 100%; height: auto; margin: .6rem 0 .3rem; }
    .atlx-div-stacey .atlx-ds-zone { cursor: pointer; transition: opacity .25s ease; }
    .atlx-div-stacey .atlx-ds-zone:hover { opacity: .85; }
    .atlx-div-stacey .atlx-ds-zone:focus-visible { outline: 2px solid var(--ds-ink); outline-offset: 2px; }
    .atlx-div-stacey .atlx-ds-cards { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .6rem; margin: 1rem 0 0; }
    @media (max-width: 700px) { .atlx-div-stacey .atlx-ds-cards { grid-template-columns: 1fr; } }
    .atlx-div-stacey .atlx-ds-card {
      width: 100%;
      font: inherit;
      text-align: left;
      cursor: pointer;
      margin: 0;
      padding: .6rem .8rem;
      border: 1px solid var(--ds-line);
      border-left-width: 4px;
      border-radius: 6px;
      background: rgba(255,255,255,0.02);
      color: var(--ds-text);
      font-size: .9rem;
      line-height: 1.5;
      opacity: .55;
      transition: opacity .2s ease;
    }
    .atlx-div-stacey .atlx-ds-card[data-active="true"] { opacity: 1; }
    .atlx-div-stacey .atlx-ds-card[data-zone="simple"] { border-left-color: var(--ds-amber); }
    .atlx-div-stacey .atlx-ds-card[data-zone="complicated"] { border-left-color: var(--ds-blue); }
    .atlx-div-stacey .atlx-ds-card[data-zone="complex"] { border-left-color: var(--ds-green); }
    .atlx-div-stacey .atlx-ds-card[data-zone="chaotic"] { border-left-color: var(--ds-purple); }
    .atlx-div-stacey .atlx-ds-card[data-active="true"][data-zone="simple"] { background: rgba(255,192,116,0.07); }
    .atlx-div-stacey .atlx-ds-card[data-active="true"][data-zone="complicated"] { background: rgba(91,158,213,0.07); }
    .atlx-div-stacey .atlx-ds-card[data-active="true"][data-zone="complex"] { background: rgba(84,164,104,0.07); }
    .atlx-div-stacey .atlx-ds-card[data-active="true"][data-zone="chaotic"] { background: rgba(167,139,250,0.07); }
    .atlx-div-stacey .atlx-ds-card strong { color: var(--ds-ink); }
    .atlx-div-stacey .atlx-ds-card:focus-visible { outline: 2px solid var(--ds-amber); outline-offset: 3px; }
  </style>

  <h3 class="atlx-ds-title">The Stacey Matrix: How Certain Are You?</h3>
  <p class="atlx-ds-sub">Certainty about methods runs left to right. Certainty about outcomes runs bottom to top. Select a zone.</p>

  <noscript><p style="font-size:.9rem;">This figure needs JavaScript. The gist: simple work has one stable optimum, complicated work has an optimum experts can find, complex work has only temporary optimums, and chaotic work has none at all.</p></noscript>

  <svg id="dst-svg" viewBox="0 0 440 430" role="img" aria-label="Stacey matrix with four zones: simple, complicated, complex, chaotic"></svg>

  <div class="atlx-ds-cards">
    <button type="button" class="atlx-ds-card" data-zone="simple" data-active="true"><strong>Simple: one optimal peak.</strong> Example: the optimal weight of a shovel-full of coal. Once found, the answer stays the answer, and training reliably reproduces it.</button>
    <button type="button" class="atlx-ds-card" data-zone="complicated" data-active="false"><strong>Complicated: several good solutions, one optimum that holds.</strong> Example: watch repair. With enough experience a repairer finds a personal optimum, and it remains optimal.</button>
    <button type="button" class="atlx-ds-card" data-zone="complex" data-active="false"><strong>Complex: optimums are temporary.</strong> A peak today may not be a peak tomorrow. Example: financial markets, where a good strategy stops working once other parties copy it.</button>
    <button type="button" class="atlx-ds-card" data-zone="chaotic" data-active="false"><strong>Chaotic: no stable optimum at all.</strong> Peaks move while you search. Problem and solution co-evolve, so only rapid experimentation tells you anything.</button>
  </div>

  <script>
  (function(){
    var root = document.currentScript && document.currentScript.closest ? document.currentScript.closest('.atlx-div-stacey') : document.querySelector('.atlx-div-stacey');
    if(!root) return;
    var NS = 'http://www.w3.org/2000/svg';
    var svg = root.querySelector('#dst-svg');
    var cards = root.querySelectorAll('[data-zone]');
    var X0 = 46, X1 = 400, Y0 = 380, Y1 = 26;
    function el(name, attrs, parent){
      var n = document.createElementNS(NS, name);
      for(var k in attrs) n.setAttribute(k, attrs[k]);
      (parent || svg).appendChild(n);
      return n;
    }
    function T(x, y, s, anchor, fill, size, weight){
      var t = el('text', {x: x, y: y, 'text-anchor': anchor || 'middle', fill: fill || 'var(--ds-dim)', 'font-size': size || 12, 'font-family': '"Cal Sans", sans-serif'});
      if(weight) t.setAttribute('font-weight', weight);
      t.textContent = s;
      return t;
    }
    var grid = el('g', {stroke: 'var(--ds-line)', 'stroke-width': 1}, svg);
    for(var i = 0; i <= 4; i++){
      var gx = X0 + (i / 4) * (X1 - X0);
      var gy = Y0 - (i / 4) * (Y0 - Y1);
      el('line', {x1: gx, y1: Y1, x2: gx, y2: Y0}, grid);
      el('line', {x1: X0, y1: gy, x2: X1, y2: gy}, grid);
    }
    var zones = el('g', {}, svg);
    function zonePath(d, fill, edge, id){
      var p = el('path', {d: d, fill: fill, stroke: edge, 'stroke-width': 1.5, 'class': 'atlx-ds-zone', tabindex: '0', role: 'button', 'aria-pressed': 'false', id: id}, zones);
      return p;
    }
    var CX = X0, CY = Y0, KX = X1, KY = Y1;
    var zComplex = zonePath('M' + X0 + ',' + Y1 + 'L' + X1 + ',' + Y1 + 'L' + X1 + ',' + Y0 + 'L' + X0 + ',' + Y0 + 'Z', 'rgba(84,164,104,0.13)', 'rgba(84,164,104,0.7)', 'dst-z-complex');
    var carve = el('g', {style: 'fill:var(--ds-surface)', stroke: 'none'}, svg);
    el('path', {d: 'M' + CX + ',' + (CY - 250) + ' A250,250 0 0 1 ' + (CX + 250) + ',' + CY + ' L' + CX + ',' + CY + ' Z'}, carve);
    el('path', {d: 'M' + KX + ',' + (KY + 125) + ' L' + KX + ',' + KY + ' L' + (KX - 125) + ',' + KY + ' A125,125 0 0 0 ' + KX + ',' + (KY + 125) + ' Z'}, carve);
    svg.insertBefore(carve, zones);
    var zComp = zonePath('M' + CX + ',' + (CY - 250) + ' A250,250 0 0 1 ' + (CX + 250) + ',' + CY + ' L' + (CX + 125) + ',' + CY + ' A125,125 0 0 0 ' + CX + ',' + (CY - 125) + ' Z', 'rgba(91,158,213,0.55)', 'rgba(91,158,213,0.9)', 'dst-z-complicated');
    var zSimple = zonePath('M' + CX + ',' + CY + 'L' + CX + ',' + (CY - 125) + ' A125,125 0 0 1 ' + (CX + 125) + ',' + CY + ' Z', 'rgba(255,192,116,0.75)', 'rgba(255,192,116,0.9)', 'dst-z-simple');
    var zChaotic = zonePath('M' + KX + ',' + (KY + 125) + ' L' + KX + ',' + KY + ' L' + (KX - 125) + ',' + KY + ' A125,125 0 0 0 ' + KX + ',' + (KY + 125) + ' Z', 'rgba(167,139,250,0.7)', 'rgba(167,139,250,0.9)', 'dst-z-chaotic');
    var zl = el('g', {'font-family': '"Cal Sans", sans-serif', 'font-size': 15, 'font-weight': 600, 'text-anchor': 'middle', 'pointer-events': 'none'}, svg);
    function ZT(x, y, s, fill){
      var t = el('text', {x: x, y: y, fill: fill}, zl);
      t.textContent = s;
    }
    ZT(90, 336, 'Simple', 'var(--ds-ink)');
    ZT(179, 247, 'Complicated', 'var(--ds-ink)');
    ZT(250, 160, 'Complex', 'var(--ds-ink)');
    ZT(356, 70, 'Chaotic', 'var(--ds-ink)');
    T(X0, Y0 + 24, 'Methods: Known, Proven', 'start');
    T(X1, Y0 + 24, 'Unknown, Untested', 'end');
    var yl = el('text', {x: 14, y: (Y0 + Y1) / 2, fill: 'var(--ds-dim)', 'font-size': 12, 'font-family': '"Cal Sans", sans-serif', 'text-anchor': 'middle', transform: 'rotate(-90 14 ' + ((Y0 + Y1) / 2) + ')'}, svg);
    yl.textContent = 'Outcomes: Clear at bottom, Unclear at top';
    var paths = {simple: zSimple, complicated: zComp, complex: zComplex, chaotic: zChaotic};
    var FILLS = {
      simple: {base: 'rgba(255,192,116,0.75)', hot: 'rgba(255,192,116,0.95)'},
      complicated: {base: 'rgba(91,158,213,0.55)', hot: 'rgba(91,158,213,0.85)'},
      complex: {base: 'rgba(84,164,104,0.13)', hot: 'rgba(84,164,104,0.35)'},
      chaotic: {base: 'rgba(167,139,250,0.7)', hot: 'rgba(167,139,250,0.9)'}
    };
    function setZone(k){
      var dimOthers = k !== 'complex';
      Object.keys(paths).forEach(function(key){
        var on = key === k;
        paths[key].setAttribute('aria-pressed', String(on));
        paths[key].setAttribute('fill', on ? FILLS[key].hot : FILLS[key].base);
        paths[key].setAttribute('opacity', on ? '1' : (dimOthers ? '0.45' : '1'));
      });
      cards.forEach(function(c){ c.setAttribute('data-active', String(c.getAttribute('data-zone') === k)); });
    }
    Object.keys(paths).forEach(function(key){
      paths[key].addEventListener('click', function(){ setZone(key); });
      paths[key].addEventListener('keydown', function(ev){ if(ev.key === 'Enter' || ev.key === ' '){ ev.preventDefault(); setZone(key); } });
    });
    cards.forEach(function(c){ c.addEventListener('click', function(){ setZone(c.getAttribute('data-zone')); }); });
    setZone('simple');
  })();
  </script>
</div>

As a starting point for moving further, I have to start with a few definitions.

- We’ll take the idea of a “simple” problem as one in which there is a single optimal peak; the optimal weight of a shovel-full of coal to unload a cart in a 12 hour shift.
- A complicated problem where there may be multiple “good” solutions and one “optimal” solution but once they are discovered through training and experience, they remain optimal. Imagine watch repair, there are multiple strategies for diagnosis and repair, but with enough experience a repair-person can find at least a personal (local) optimum.
- And finally, the complex and chaotic environments of the dancing landscapes, in which optimums can only temporarily be discovered, a peak today may not be a peak tomorrow, an optimum may not be an optimum in a year, etc. An easy example would be financial markets, where any sufficiently good strategy, ceases to be a good strategy once other parties wise up to it (Adaptive Market Hypothesis).

<!-- Atlancia embed: Diversity and complexity - fitness landscapes explorer (interactive).
     Fits the post From Shovels to Software: Why Difference Matters When Things Get Complex.
     Three true isometric surface meshes; the dancing one morphs on its own until paused.
     slop-ok: exclamation marks are logical-not operators in inline script, not prose emphasis. -->
<div class="atlx atlx-div-land">
  <style>
    .atlx-div-land {
      --dl-ink: var(--atl-ink, #EEEDED);
      --dl-text: var(--atl-figure-text, #BFBFBF);
      --dl-dim: var(--atl-dim, #9D9D9D);
      --dl-line: var(--atl-line, #373737);
      --dl-surface: var(--atl-surface, #1e1e1e);
      --dl-blue: var(--atl-info, #5B9ED5);
      --dl-green: var(--atl-success, #54A468);
      --dl-amber: var(--atl-accent, #FFC074);
      --dl-purple: #a78bfa;
      font-family: "Cal Sans", ui-sans-serif, system-ui, sans-serif;
      background: var(--dl-surface);
      color: var(--dl-text);
      border: 1px solid var(--dl-line);
      border-radius: 6px;
      padding: 1.3rem 1.3rem 1.1rem;
      margin: 2.5rem 0;
      max-width: 100%;
      font-size: 1rem;
      line-height: 1.55;
    }
    .atlx-div-land * { box-sizing: border-box; }
    .atlx-div-land .atlx-dl-title {
      margin: 0 0 .2rem;
      font-family: "Young Serif", Georgia, serif;
      font-weight: 500;
      font-size: 1.25rem;
      line-height: 1.35;
      color: var(--dl-ink);
    }
    .atlx-div-land svg { display: block; width: 100%; height: auto; }
    .atlx-div-land .atlx-dl-panels { display: grid; grid-template-columns: 1fr; gap: .6rem; margin-top: .9rem; }
    .atlx-div-land .atlx-dl-panel { margin: 0 0 1rem; }
    .atlx-div-land .atlx-dl-panel:last-child { margin-bottom: 0; }
    .atlx-div-land .atlx-dl-cap { margin: 0 0 .45rem; font-size: .95rem; color: var(--dl-dim); }
    .atlx-div-land .atlx-dl-cap strong { color: var(--dl-ink); }
    .atlx-div-land .atlx-dl-cap .dot { display: inline-block; width: .62em; height: .62em; border-radius: 50%; margin-right: .45em; }
    .atlx-div-land .atlx-dl-rule { border: none; border-top: 1px solid var(--dl-line); margin: 0 0 .6rem; }
    .atlx-div-land .atlx-dl-slider { display: flex; align-items: center; gap: .6rem; margin-top: .3rem; font-size: .85rem; color: var(--dl-dim); }
    .atlx-div-land .atlx-dl-slider input[type="range"] {
      -webkit-appearance: none;
      appearance: none;
      flex: 1;
      height: 28px;
      background: transparent;
      cursor: pointer;
    }
    .atlx-div-land .atlx-dl-slider input[type="range"]::-webkit-slider-runnable-track { height: 6px; border-radius: 999px; background: var(--dl-line); }
    .atlx-div-land .atlx-dl-slider input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--dl-purple);
      border: 3px solid var(--dl-surface);
      margin-top: -8px;
    }
    .atlx-div-land .atlx-dl-slider input[type="range"]::-moz-range-track { height: 6px; border-radius: 999px; background: var(--dl-line); }
    .atlx-div-land .atlx-dl-slider input[type="range"]::-moz-range-thumb {
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--dl-purple);
      border: 3px solid var(--dl-surface);
    }
    .atlx-div-land .atlx-dl-play {
      font: inherit;
      font-size: .85rem;
      font-weight: 600;
      color: var(--dl-ink);
      background: rgba(255,255,255,0.05);
      border: 1px solid var(--dl-line);
      border-radius: 999px;
      padding: .25rem .9rem;
      cursor: pointer;
      white-space: nowrap;
    }
    .atlx-div-land .atlx-dl-play:hover { background: rgba(255,255,255,0.1); }
    .atlx-div-land .atlx-dl-play:focus-visible { outline: 2px solid var(--dl-purple); outline-offset: 2px; }
  </style>

  <h3 class="atlx-dl-title">Peaked, Rugged, Dancing</h3>

  <noscript><p style="font-size:.9rem;">This figure needs JavaScript. The gist: a peaked landscape has one optimum a simple search finds, a rugged one traps fixed searches on local peaks, and a dancing one moves its peaks while you search, so only continuous adaptation works.</p></noscript>

  <div class="atlx-dl-panels">
    <div class="atlx-dl-panel" data-panel="peaked">
      <div class="atlx-dl-rule"></div>
      <p class="atlx-dl-cap"><strong><span class="dot" style="background:var(--dl-green)"></span>Peaked: one optimum.</strong> Hill climbing always finds it. The textbook case.</p>
      <svg id="ddl-svg-p" viewBox="0 190 660 280" role="img" aria-label="Peaked 3D fitness landscape"></svg>
    </div>
    <div class="atlx-dl-panel" data-panel="rugged">
      <div class="atlx-dl-rule"></div>
      <p class="atlx-dl-cap"><strong><span class="dot" style="background:var(--dl-amber)"></span>Rugged: many local optima.</strong> The highest peak wins, but good enough is often good enough.</p>
      <svg id="ddl-svg-r" viewBox="0 190 660 280" role="img" aria-label="Rugged 3D fitness landscape with marked peaks"></svg>
    </div>
    <div class="atlx-dl-panel" data-panel="dancing">
      <div class="atlx-dl-rule"></div>
      <p class="atlx-dl-cap"><strong><span class="dot" style="background:var(--dl-purple)"></span>Dancing: optima move.</strong> Two points pinned: watch the valley rise above the peak while the peak falls and climbs back lower.</p>
      <svg id="ddl-svg-d" viewBox="0 190 660 280" role="img" aria-label="Dancing 3D fitness landscape"></svg>
      <div class="atlx-dl-slider">
        <button type="button" class="atlx-dl-play" data-role="play" aria-pressed="true">Pause</button>
        <label for="ddl-time">Time</label>
        <input id="ddl-time" type="range" min="0" max="100" value="15">
      </div>
    </div>
  </div>

  <script>
  (function(){
    var root = document.currentScript && document.currentScript.closest ? document.currentScript.closest('.atlx-div-land') : document.querySelector('.atlx-div-land');
    if(!root) return;
    var NS = 'http://www.w3.org/2000/svg';
    var AMP = [0.62, 0.85, 1.0, 0.9, 0.78];
    function el(name, attrs, parent){
      var n = document.createElementNS(NS, name);
      for(var k in attrs) n.setAttribute(k, attrs[k]);
      parent.appendChild(n);
      return n;
    }
    function gauss(x, c, w){ var z = (x - c) / w; return Math.exp(-z * z); }
    function peakedY(x, li){ return 240 - 190 * AMP[li] * gauss(x, 270 + (li - 2) * 22, 90 + li * 3); }
    function ruggedY(x, li){
      var ph = li * 16;
      return 240 - (34 * Math.sin((x + ph) / 26) + 22 * Math.sin((x + ph) / 11 + 1.3) + 64 * gauss(x, 150 + li * 8, 45) + 74 * gauss(x, 380 - li * 8, 55) + 52 * gauss(x, 505, 30));
    }
    function g2(x, j, cx, cj, wx, wj){
      var zx = (x - cx) / wx, zj = (j - cj) / wj;
      return Math.exp(-(zx * zx + zj * zj));
    }
    function smooth01(t){ return t * t * (3 - 2 * t); }
    function proj(x, j, h){
      return [200 + (x - j * 46) * 0.72, 352 + j * 14 + x * 0.06 - h * 0.9];
    }
    function surfH(hFn, x, j){ return Math.max(0, hFn(x, j)); }
    function buildIso(svg, hFn, hmax, low, high, edgeCss, dotCss, labels, n, pins){
      while(svg.firstChild) svg.removeChild(svg.firstChild);
      var J = 4, NX = 30, STEP = 540 / NX;
      var floor = el('g', {stroke: 'rgba(255,255,255,0.16)', 'stroke-width': 1, fill: 'none'}, svg);
      el('path', {d: 'M' + proj(0, 0, 0) + 'L' + proj(540, 0, 0) + 'L' + proj(540, J, 0) + 'L' + proj(0, J, 0) + 'Z'}, floor);
      for(var gx = 0; gx <= 540; gx += 54){
        var ga = proj(gx, 0, 0), gb = proj(gx, J, 0);
        el('line', {x1: ga[0], y1: ga[1], x2: gb[0], y2: gb[1]}, floor);
      }
      for(var gj = 0; gj <= J; gj++){
        var gc = proj(0, gj, 0), gd = proj(540, gj, 0);
        el('line', {x1: gc[0], y1: gc[1], x2: gd[0], y2: gd[1]}, floor);
      }
      var f0 = proj(0, J, 0), f1 = proj(540, J, 0), DEP = 24;
      el('path', {d: 'M' + f0[0] + ',' + f0[1] + ' L' + f1[0] + ',' + f1[1] + ' L' + f1[0] + ',' + (f1[1] + DEP) + ' L' + f0[0] + ',' + (f0[1] + DEP) + ' Z', fill: 'rgba(0,0,0,0.55)', stroke: 'var(--dl-line)', 'stroke-width': 1}, svg);
      for(var j = 0; j < J; j++){
        for(var i = 0; i < NX; i++){
          var x0 = i * STEP, x1 = x0 + STEP;
          var h00 = surfH(hFn, x0, j), h10 = surfH(hFn, x1, j);
          var h11 = surfH(hFn, x1, j + 1), h01 = surfH(hFn, x0, j + 1);
          var p00 = proj(x0, j, h00), p10 = proj(x1, j, h10);
          var p11 = proj(x1, j + 1, h11), p01 = proj(x0, j + 1, h01);
          var st = Math.min(1, (h00 + h10 + h11 + h01) / 4 / hmax);
          var sR = Math.round(low[0] + (high[0] - low[0]) * st);
          var sG = Math.round(low[1] + (high[1] - low[1]) * st);
          var sB = Math.round(low[2] + (high[2] - low[2]) * st);
          el('path', {d: 'M' + p00 + 'L' + p10 + 'L' + p11 + 'L' + p01 + 'Z', fill: 'rgb(' + sR + ',' + sG + ',' + sB + ')', stroke: edgeCss, 'stroke-width': 0.5}, svg);
        }
      }
      var cands = [];
      for(var jj = 0; jj <= J; jj++){
        var bx = 0, bh = -1;
        for(var x = 0; x <= 540; x += 6){ var h = surfH(hFn, x, jj); if(h > bh){ bh = h; bx = x; } }
        cands.push({x: bx, j: jj, h: bh});
      }
      var tops = [];
      if(pins){
        pins.forEach(function(c){ tops.push({x: c.x, j: c.j, h: surfH(hFn, c.x, c.j)}); });
      } else {
        cands.sort(function(p, q){ return q.h - p.h; });
        cands.forEach(function(c){ if(tops.length < n && tops.every(function(t){ return Math.abs(t.x - c.x) > 70; })) tops.push(c); });
      }
      var G = el('g', {'font-family': '"Cal Sans", sans-serif', 'font-size': 17, 'font-weight': 600, 'text-anchor': 'middle'}, svg);
      tops.forEach(function(c, i){
        var p = proj(c.x, c.j, c.h);
        el('circle', {cx: p[0], cy: p[1], r: 7, fill: '#ffffff', stroke: dotCss, 'stroke-width': 2}, G);
        var t = el('text', {x: p[0], y: p[1] - 12, fill: 'var(--dl-ink)', 'paint-order': 'stroke', stroke: 'var(--dl-surface)', 'stroke-width': 3}, G);
        t.textContent = labels[Math.min(i, labels.length - 1)];
      });
    }
    var svgP = root.querySelector('#ddl-svg-p');
    var svgR = root.querySelector('#ddl-svg-r');
    var svgD = root.querySelector('#ddl-svg-d');
    function peakedH(x, j){ return Math.max(0, 240 - peakedY(x, j)); }
    function ruggedH(x, j){ return Math.max(0, 240 - ruggedY(x, j)); }
    buildIso(svgP, peakedH, 200, [34, 62, 40], [84, 164, 104], 'rgba(84,164,104,0.3)', 'var(--dl-green)', ['the peak'], 1);
    buildIso(svgR, ruggedH, 270, [110, 70, 36], [255, 192, 116], 'rgba(255,192,116,0.3)', 'var(--dl-amber)', ['highest', 'good enough'], 2);
    var slider = root.querySelector('#ddl-time');
    var playBtn = root.querySelector('[data-role="play"]');
    var dance = {t: 0.15, dir: 1, playing: true, raf: 0, last: 0};
    if(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) dance.playing = false;
    function danceH(x, j){
      var t = dance.t;
      var env1 = 0.55 + 0.45 * Math.cos(t * 2 * Math.PI) - 0.25 * t;
      var env2 = 0.06 + smooth01(t);
      var h = 100 * g2(x, j, 300, 2, 110, 2.0) * env1
            + 130 * g2(x, j, 150, 3, 100, 2.0) * env2
            + 20 * Math.sin(x / 24 + t * 2.5 + j * j * 0.4 + j * 0.3)
            + 12 * Math.sin(x / 11 + 1.1 - t * 3.4 + j * 1.9);
      return Math.max(0, h);
    }
    function drawDancing(){
      buildIso(svgD, danceH, 240, [52, 44, 86], [167, 139, 250], 'rgba(167,139,250,0.3)', 'var(--dl-purple)', ['peak', 'valley'], 2, [{x: 300, j: 2}, {x: 150, j: 3}]);
      slider.value = String(Math.round(dance.t * 100));
    }
    function tick(now){
      if(!dance.playing) return;
      var dt = dance.last ? (now - dance.last) / 1000 : 0.05;
      dance.last = now;
      dance.t += dance.dir * dt * 0.12;
      if(dance.t >= 1){ dance.t = 1; dance.dir = -1; }
      if(dance.t <= 0){ dance.t = 0; dance.dir = 1; }
      drawDancing();
      dance.raf = window.requestAnimationFrame(tick);
    }
    function setPlaying(on){
      dance.playing = on;
      dance.last = 0;
      playBtn.textContent = on ? 'Pause' : 'Play';
      playBtn.setAttribute('aria-pressed', String(on));
      if(on) dance.raf = window.requestAnimationFrame(tick);
      else if(dance.raf) window.cancelAnimationFrame(dance.raf);
    }
    playBtn.addEventListener('click', function(){ setPlaying(!dance.playing); });
    slider.addEventListener('input', function(){
      dance.t = (parseInt(slider.value, 10) || 0) / 100;
      setPlaying(false);
      drawDancing();
    });
    drawDancing();
    setPlaying(dance.playing);
    playBtn.textContent = dance.playing ? 'Pause' : 'Play';
    playBtn.setAttribute('aria-pressed', String(dance.playing));
  })();
  </script>
</div>

## Kicking and Screaming Into Complexity

Regardless of how we choose to encode the ideas of complexity, either the above, or other common models like Cynefin, the key idea is that there is a point in complexity where we leave the world of the predictable, stable and solvable and enter a different domain.

<!-- Atlancia embed: Diversity and complexity - knowledge boundary explorer (interactive).
     Fits the post From Shovels to Software: Why Difference Matters When Things Get Complex.
     Least complex on the left, most on the right; each domain card carries its own callout.
     slop-ok: exclamation marks are logical-not operators in inline script, not prose emphasis. -->
<div class="atlx atlx-div-boundary">
  <style>
    .atlx-div-boundary {
      --db-ink: var(--atl-ink, #EEEDED);
      --db-text: var(--atl-figure-text, #BFBFBF);
      --db-dim: var(--atl-dim, #9D9D9D);
      --db-line: var(--atl-line, #373737);
      --db-surface: var(--atl-surface, #1e1e1e);
      --db-blue: var(--atl-info, #5B9ED5);
      --db-green: var(--atl-success, #54A468);
      --db-amber: var(--atl-accent, #FFC074);
      --db-purple: #a78bfa;
      font-family: "Cal Sans", ui-sans-serif, system-ui, sans-serif;
      background: var(--db-surface);
      color: var(--db-text);
      border: 1px solid var(--db-line);
      border-radius: 6px;
      padding: 1.3rem 1.3rem 1.1rem;
      margin: 2.5rem 0;
      max-width: 100%;
      font-size: 1rem;
      line-height: 1.55;
    }
    .atlx-div-boundary * { box-sizing: border-box; }
    .atlx-div-boundary .atlx-db-title {
      margin: 0 0 .2rem;
      font-family: "Young Serif", Georgia, serif;
      font-weight: 500;
      font-size: 1.25rem;
      line-height: 1.35;
      color: var(--db-ink);
    }
    .atlx-div-boundary .atlx-db-sub { margin: 0 0 .3rem; color: var(--db-dim); font-size: .95rem; }
    .atlx-div-boundary .atlx-db-flow { display: grid; gap: .6rem; margin-top: .9rem; }
    .atlx-div-boundary .atlx-db-side {
      font-size: .75rem;
      font-weight: 600;
      letter-spacing: .12em;
      text-transform: uppercase;
      color: var(--db-dim);
      margin: .3rem 0 0;
    }
    .atlx-div-boundary .atlx-db-card {
      width: 100%;
      margin: 0;
      padding: .7rem .9rem;
      border: 1px solid var(--db-line);
      border-top-width: 4px;
      border-radius: 6px;
      background: rgba(255,255,255,0.02);
      color: var(--db-text);
      font-size: .9rem;
      line-height: 1.5;
    }
    .atlx-div-boundary .atlx-db-card[data-domain="simple"] { border-top-color: var(--db-amber); }
    .atlx-div-boundary .atlx-db-card[data-domain="complicated"] { border-top-color: var(--db-blue); }
    .atlx-div-boundary .atlx-db-card[data-domain="complex"] { border-top-color: var(--db-green); }
    .atlx-div-boundary .atlx-db-card[data-domain="chaotic"] { border-top-color: var(--db-purple); }
    .atlx-div-boundary .atlx-db-card .name { display: flex; align-items: center; gap: .5rem; font-weight: 600; font-size: 1.05rem; line-height: 1.3; color: var(--db-ink); min-height: 1.4em; }
    .atlx-div-boundary .atlx-db-card .dot { width: 12px; height: 12px; border-radius: 50%; flex: 0 0 auto; }
    .atlx-div-boundary .atlx-db-card .know { display: block; font-size: .85rem; color: var(--db-dim); font-weight: 500; margin: .1rem 0 .45rem; min-height: 1.4em; }
    .atlx-div-boundary .atlx-db-card .body strong { color: var(--db-ink); }
    .atlx-div-boundary .atlx-db-card .body span { display: block; margin-top: .25rem; }
    .atlx-div-boundary .atlx-db-divline { display: flex; align-items: center; gap: .6rem; margin: .2rem 0; }
    .atlx-div-boundary .atlx-db-divline .rule { flex: 1; height: 0; border-top: 4px dashed var(--db-dim); }
    .atlx-div-boundary .atlx-db-divline .tag {
      font-size: .78rem;
      font-weight: 600;
      letter-spacing: .12em;
      text-transform: uppercase;
      color: var(--db-dim);
      white-space: nowrap;
      border: 1px solid var(--db-dim);
      border-radius: 999px;
      padding: .2rem .9rem;
    }
  </style>

  <h3 class="atlx-db-title">The Knowledge Boundary</h3>
  <p class="atlx-db-sub">Most complex at the top, least at the bottom. The boundary sits between Complex and Complicated.</p>

  <noscript><p style="font-size:.9rem;">The gist: below the Knowledge Boundary work is predictable with a stable optimum where quality means conformance, while beyond it information is created through work where quality needs experimentation and new perspectives.</p></noscript>

  <div class="atlx-db-flow">
    <p class="atlx-db-side">Beyond the boundary</p>
    <div class="atlx-db-card" data-domain="chaotic">
      <span class="name"><span class="dot" style="background:var(--db-purple)"></span>Chaotic</span>
      <span class="know">Unknown</span>
      <span class="body"><strong>No cause and effect to find in the moment.</strong><span>No stable solution exists, so rapid experimentation is the quality system.</span></span>
    </div>
    <div class="atlx-db-card" data-domain="complex">
      <span class="name"><span class="dot" style="background:var(--db-green)"></span>Complex</span>
      <span class="know">Unknowable</span>
      <span class="body"><strong>Information is created through work.</strong><span>No optimum holds still, so experimentation and new perspectives are the method.</span></span>
    </div>
    <div class="atlx-db-divline" aria-hidden="true"><span class="rule"></span><span class="tag">Knowledge Boundary</span><span class="rule"></span></div>
    <p class="atlx-db-side">Below the boundary</p>
    <div class="atlx-db-card" data-domain="complicated">
      <span class="name"><span class="dot" style="background:var(--db-blue)"></span>Complicated</span>
      <span class="know">Knowable</span>
      <span class="body"><strong>Knowable by experts through analysis.</strong><span>Several good solutions, one optimum that holds: apply good practice.</span></span>
    </div>
    <div class="atlx-db-card" data-domain="simple">
      <span class="name"><span class="dot" style="background:var(--db-amber)"></span>Simple</span>
      <span class="know">Known</span>
      <span class="body"><strong>Cause and effect are clear.</strong><span>Apply best practice and check conformance: training reliably reproduces the result.</span></span>
    </div>
  </div>

</div>

Crossing that boundary requires discarding assumptions that only held true in predictable environments. Best practices become merely good practices; assuming a single practice remains best is a fool's errand. Rigid processes turn into anchors slowing down needed change. Staying still becomes as risky as changing and adaptability is a necessary dimension of resilience (see BS 65000:2022, Organizational Resilience).

> _All models are wrong, some are useful._ - George Box, 1976.

No model captures the full mess of a real project. The useful distinction is the tipping point where predictability breaks down. Where work is no longer defined by the comfort of predictability, but by the challenges of unpredictability.

## Sensing Complexity

A diagram makes the boundary look clean, but real-world problems do not arrive with labels. Some challenges look deceptively simple yet resist straightforward answers. The moving sofa problem (finding the largest two-dimensional shape that can maneuver through an L-shaped hallway) has occupied mathematicians for decades without a complete proof.

In _Antifragile_, Nassim Nicholas Taleb highlights non-linearity as a hallmark of complex systems. Doubling an input does not yield a tidy doubling of the result; effects are either amplified or reduced through a crosshatch of interdependencies. Simple cause-and-effect relationships do not hold, and understanding the functioning of individual parts alone is insufficient.

And so, we go full circle. The opening quote of this writing from the _Mythical Man-Month_, exemplifies this non-linearity. The observation that adding developers to a late software project tends to make it later is a darn good indicator that knowledge work is complex rather than simply complicated. The rest of the writing will use software development and knowledge work generally, as marquee examples in comparison to other clearly simple or complicated types of work.

## Diversity as a Tool in Knowledge Work

> _Knowledge workers are persons who understand their job better than their boss._ - Peter Drucker.

If we are to accept that:

- Knowledge work is complex and requires teams of skilled people working together.
- Complex work is unpredictable, interconnected and non-linear.
- The tools or expertise required to achieve good outcomes cannot be predicted far in advance.

Then surely the natural response would be to avoid building a team of identical individuals who fit the same mold. Instead, an approach could be to optimize for the broadest germane skills and tools, prioritizing diversity of thought over convergence to a mean.

Below is a simplified model illustrating key differences between making the complicated workings of a watch and the complex development of a novel software product.

<!-- Atlancia embed: Diversity and complexity - input diversity comparison (interactive).
     Fits the post From Shovels to Software: Why Difference Matters When Things Get Complex.
     Faithful rebuild of the original two-column figure: watchmakers 1-to-1 to Consistent Product,
     software roles many-to-1 to Novel Product/Outcome. Toggle halves, hover or focus a row to isolate its path.
     Pictograms: Iconoir (MIT) inlined as symbols.
     slop-ok: exclamation marks are logical-not operators in inline script, not prose emphasis. -->
<div class="atlx atlx-div-panels" data-view="both">
  <style>
    .atlx-div-panels {
      --dp-ink: var(--atl-ink, #EEEDED);
      --dp-text: var(--atl-figure-text, #BFBFBF);
      --dp-dim: var(--atl-dim, #9D9D9D);
      --dp-line: var(--atl-line, #373737);
      --dp-surface: var(--atl-surface, #1e1e1e);
      --dp-purple: #a78bfa;
      --dp-amber: var(--atl-accent, #FFC074);
      --dp-arrow: #9D9D9D;
      font-family: "Cal Sans", ui-sans-serif, system-ui, sans-serif;
      background: var(--dp-surface);
      color: var(--dp-text);
      border: 1px solid var(--dp-line);
      border-radius: 6px;
      padding: 1.3rem 1.3rem 1.1rem;
      margin: 2.5rem 0;
      max-width: 100%;
      font-size: 1rem;
      line-height: 1.55;
    }
    .atlx-div-panels * { box-sizing: border-box; }
    .atlx-div-panels .atlx-dp-title {
      margin: 0 0 .2rem;
      font-family: "Young Serif", Georgia, serif;
      font-weight: 500;
      font-size: 1.25rem;
      line-height: 1.35;
      color: var(--dp-ink);
    }
    .atlx-div-panels .atlx-dp-sub { margin: 0 0 .3rem; color: var(--dp-dim); font-size: .95rem; }
    .atlx-div-panels .atlx-dp-legend { display: flex; flex-wrap: wrap; gap: .4rem 1.1rem; margin: .55rem 0 0; font-size: .88rem; color: var(--dp-dim); }
    .atlx-div-panels .atlx-dp-legend .sw { display: inline-block; width: .68em; height: .68em; border-radius: 3px; margin-right: .45em; }
    .atlx-div-panels .atlx-dp-view { display: inline-flex; gap: .25rem; margin: .9rem 0 0; padding: .25rem; border: 1px solid var(--dp-line); border-radius: 999px; }
    .atlx-div-panels .atlx-dp-view button {
      font: inherit;
      font-size: .85rem;
      font-weight: 600;
      color: var(--dp-dim);
      background: transparent;
      border: none;
      border-radius: 999px;
      padding: .3rem .95rem;
      cursor: pointer;
    }
    .atlx-div-panels .atlx-dp-view button[aria-pressed="true"] { background: rgba(255,255,255,0.09); color: var(--dp-ink); }
    .atlx-div-panels .atlx-dp-view button:focus-visible { outline: 2px solid var(--dp-amber); outline-offset: 2px; }
    .atlx-div-panels .atlx-dp-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; margin-top: .9rem; }
    .atlx-div-panels[data-view="watch"] .atlx-dp-grid, .atlx-div-panels[data-view="soft"] .atlx-dp-grid { grid-template-columns: 1fr; }
    .atlx-div-panels[data-view="watch"] .side-soft { display: none; }
    .atlx-div-panels[data-view="soft"] .side-watch { display: none; }
    @media (max-width: 760px) { .atlx-div-panels .atlx-dp-grid { grid-template-columns: 1fr; } }
    .atlx-div-panels .atlx-dp-side { margin: 0; }
    .atlx-div-panels .atlx-dp-side-label { font-weight: 600; color: var(--dp-ink); font-size: .95rem; margin: 0 0 .4rem; }
    .atlx-div-panels svg.fig { display: block; width: 100%; height: auto; }
    .atlx-div-panels .atlx-dp-ic { fill: none; stroke: currentColor; stroke-linecap: round; stroke-linejoin: round; }
    .atlx-div-panels .atlx-dp-row { cursor: default; transition: opacity .2s ease; }
    .atlx-div-panels .atlx-dp-row:focus { outline: none; }
    .atlx-div-panels .atlx-dp-row:focus-visible { outline: 2px solid var(--dp-amber); outline-offset: 2px; }
  </style>

  <h3 class="atlx-dp-title">Same Inputs In, Same Product Out? Not Always</h3>
  <p class="atlx-dp-sub">Left: three watchmakers, same kit, same watch. Right: four different roles, one novel product. Trace a row, or view one half at a time.</p>
  <div class="atlx-dp-legend">
    <span><i class="sw" style="background:var(--dp-purple)"></i>Backgrounds: what each person arrived with</span>
    <span><i class="sw" style="background:var(--dp-amber)"></i>Tools and training: what the work itself provides</span>
  </div>

  <noscript><p style="font-size:.9rem;">The gist: watchmakers share near-identical backgrounds and tools, so apprentice or experienced, each produces a Consistent Product; the software team brings wildly different backgrounds and tools that combine into one Novel Product/Outcome.</p></noscript>

  <div class="atlx-dl-view-row">
    <div class="atlx-dp-view" role="group" aria-label="Choose which half to show">
      <button type="button" data-view="both" aria-pressed="true">Both</button>
      <button type="button" data-view="watch" aria-pressed="false">Watchmaking</button>
      <button type="button" data-view="soft" aria-pressed="false">Software team</button>
    </div>
  </div>

  <div class="atlx-dp-grid">
    <div class="atlx-dp-side side-watch">
      <p class="atlx-dp-side-label">Watchmaking</p>
      <svg class="fig" id="ddp-svg-w" role="img" aria-label="Watchmaking: three roles with similar inputs each produce a Consistent Product"></svg>
    </div>
    <div class="atlx-dp-side side-soft">
      <p class="atlx-dp-side-label">Software team</p>
      <svg class="fig" id="ddp-svg-s" role="img" aria-label="Software team: four different roles converge on one Novel Product Outcome"></svg>
    </div>
  </div>

  <svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <symbol id="ii-user" viewBox="0 0 24 24"><path d="M5 20V19C5 15.134 8.13401 12 12 12V12C15.866 12 19 15.134 19 19V20"/><path d="M12 12C14.2091 12 16 10.2091 16 8C16 5.79086 14.2091 4 12 4C9.79086 4 8 5.79086 8 8C8 10.2091 9.79086 12 12 12Z"/></symbol>
  <symbol id="ii-clock" viewBox="0 0 24 24"><path d="M12 6L12 12L18 12"/><path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"/></symbol>
  <symbol id="ii-wristwatch" viewBox="0 0 24 24"><path d="M16 16.4722V20C16 21.1045 15.1046 22 14 22H10C8.89543 22 8 20V16.4722"/><path d="M8 7.52779V4C8 2.89543 8.89543 2 10 2H14C15.1046 2 16 2.89543 16 4V7.52779"/><path d="M18 12C18 8.68629 15.3137 6 12 6C8.68629 6 6 8.68629 6 12C6 15.3137 8.68629 18 12 18C15.3137 18 18 15.3137 18 12Z"/><path d="M14 12H12V10"/></symbol>
  <symbol id="ii-mac-os-window" viewBox="0 0 24 24"><path d="M2 17.7143V6.28571C2 5.02335 2.99492 4 4.22222 4H19.7778C21.0051 4 22 5.02335 22 6.28571V17.7143C22 18.9767 21.0051 20 19.7778 20H4.22222C2.99492 20 2 18.9767 2 17.7143Z"/><path d="M5 7.01013L5.01 6.99902"/><path d="M7 7.01013L7.01 6.99902"/><path d="M9 7.01013L9.01 6.99902"/></symbol>
  <symbol id="ii-calendar" viewBox="0 0 24 24"><path d="M15 4V2M15 4V6M15 4H10.5M3 10V19C3 20.1046 3.89543 21 5 21H19C20.1046 21 21 20.1046 21 19V10H3Z"/><path d="M3 10V6C3 4.89543 3.89543 4 5 4H7"/><path d="M7 2V6"/><path d="M21 10V6C21 4.89543 20.1046 4 19 4H18.5"/></symbol>
  <symbol id="ii-graduation-cap" viewBox="0 0 24 24"><path d="M2.57331 8.46334L11.2317 4.13416C11.4006 4.04971 11.5994 4.04971 11.7683 4.13416L20.4267 8.46334C20.8689 8.68446 20.8689 9.31554 20.4267 9.53666L11.7683 13.8658C11.5994 13.9503 11.4006 13.9503 11.2317 13.8658L2.57331 9.53666C2.13108 9.31554 2.13108 8.68446 2.57331 8.46334Z"/><path d="M22.5 13L22.5 9.5L20.5 8.5"/><path d="M4.5 10.5V15.9121C4.5 16.6843 4.94459 17.3876 5.6422 17.7188L10.6422 20.0928C11.185 20.3505 11.815 20.3505 12.3578 20.0928L17.3578 17.7188C18.0554 17.3876 18.5 16.6843 18.5 15.9121V10.5"/></symbol>
  <symbol id="ii-database" viewBox="0 0 24 24"><path d="M5 12V18C5 18 5 21 12 21C19 21 19 18 19 18V12"/><path d="M5 6V12C5 12 5 15 12 15C19 15 19 12 19 12V6"/><path d="M12 3C19 3 19 6 19 6C19 6 19 9 12 9C5 9 5 6 5 6C5 6 5 3 12 3Z"/></symbol>
  <symbol id="ii-open-book" viewBox="0 0 24 24"><path d="M12 21V7C12 5.89543 12.8954 5 14 5H21.4C21.7314 5 22 5.26863 22 5.6V18.7143"/><path d="M12 21V7C12 5.89543 11.1046 5 10 5H2.6C2.26863 5 2 5.26863 2 5.6V18.7143"/><path d="M14 19L22 19"/><path d="M10 19L2 19"/><path d="M12 21C12 19.8954 12.8954 19 14 19"/><path d="M12 21C12 19.8954 11.1046 19 10 19"/></symbol>
  <symbol id="ii-pen-tablet" viewBox="0 0 24 24"><path d="M22 5V19C22 20.1046 21.1046 21 20 21H4C2.89543 21 2 20.1046 2 19V5C2 3.89543 2.89543 3 4 3H20C21.1046 3 22 3.89543 22 5Z"/><path d="M2 12H6"/><path d="M6 3V21"/><path d="M15.5 11.5L12 14.5"/><path d="M17 10.01L17.01 9.99889"/></symbol>
  <symbol id="ii-building" viewBox="0 0 24 24"><path d="M10 9.01L10.01 8.99889"/><path d="M14 9.01L14.01 8.99889"/><path d="M10 13.01L10.01 12.9989"/><path d="M14 13.01L14.01 12.9989"/><path d="M10 17.01L10.01 16.9989"/><path d="M14 17.01L14.01 16.9989"/><path d="M6 20.4V5.6C6 5.26863 6.26863 5 6.6 5H12V3.6C12 3.26863 12.2686 3 12.6 3H17.4C17.7314 3 18 3.26863 18 3.6V20.4C18 20.7314 17.7314 21 17.4 21H6.6C6.26863 21 6 20.7314 6 20.4Z"/></symbol>
  <symbol id="ii-network" viewBox="0 0 24 24"><rect x="3" y="2" width="7" height="5" rx="0.6"/><rect x="8.5" y="17" width="7" height="5" rx="0.6"/><rect x="14" y="2" width="7" height="5" rx="0.6"/><path d="M6.5 7V10.5C6.5 11.6046 7.39543 12.5 8.5 12.5H15.5C16.6046 12.5 17.5 11.6046 17.5 10.5V7"/><path d="M12 12.5V17"/></symbol>
  <symbol id="ii-light-bulb" viewBox="0 0 24 24"><path d="M9 18H15"/><path d="M10 21H14"/><path d="M9.00082 15C9.00098 13 8.50098 12.5 7.50082 11.5C6.50067 10.5 6.02422 9.48689 6.00082 8C5.95284 4.95029 8.00067 3 12.0008 3C16.001 3 18.0488 4.95029 18.0008 8C17.9774 9.48689 17.5007 10.5 16.5008 11.5C15.501 12.5 15.001 13 15.0008 15"/></symbol>
  <symbol id="ii-people-tag" viewBox="0 0 24 24"><path d="M3 16V8C3 5.23858 5.23858 3 8 3H16C18.7614 3 21 5.23858 21 8V16C21 18.7614 18.7614 21 16 21H8C5.23858 21 3 18.7614 3 16Z"/><path d="M16.5 14.5C16.5 14.5 15 16.5 12 16.5C9 16.5 7.5 14.5 7.5 14.5"/><path d="M8.5 10C8.22386 10 8 9.77614 8 9.5C8 9.22386 8.22386 9 8.5 9C8.77614 9 9 9.22386 9 9.5C9 9.77614 8.77614 10 8.5 10Z"/><path d="M15.5 10C15.2239 10 15 9.77614 15 9.5C15 9.22386 15.2239 9 15.5 9C15.7761 9 16 9.22386 16 9.5C16 9.77614 15.7761 10 15.5 10Z"/></symbol>
  <symbol id="ii-precision-tool" viewBox="0 0 24 24"><path d="M12 6L12 8"/><path d="M12 16L12 18"/><path d="M8 12H6"/><path d="M18 12H16"/><path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"/></symbol>
  <symbol id="ii-database-script" viewBox="0 0 24 24"><path d="M22 14V6C22 4.34315 20.6569 3 19 3H9C7.34315 3 6 4.34315 6 6V13"/><path d="M12 21H6C3.79086 21 2 19.2091 2 17C2 14.7909 3.79086 13 6 13H17H18C15.7909 13 14 14.7909 14 17C14 19.2091 15.7909 21 18 21C20.2091 21 22 19.2091 22 17V14"/></symbol>
  <symbol id="ii-message-text" viewBox="0 0 24 24"><path d="M7 12L17 12"/><path d="M7 8L13 8"/><path d="M3 20.2895V5C3 3.89543 3.89543 3 5 3H19C20.1046 3 21 3.89543 21 5V15C21 16.1046 20.1046 17 19 17H7.96125C7.35368 17 6.77906 17.2762 6.39951 17.7506L4.06852 20.6643C3.71421 21.1072 3 20.8567 3 20.2895Z"/></symbol>
  <symbol id="ii-code" viewBox="0 0 24 24"><path d="M13.5 6L10 18.5"/><path d="M6.5 8.5L3 12L6.5 15.5"/><path d="M17.5 8.5L21 12L17.5 15.5"/></symbol>
  <symbol id="ii-flask" viewBox="0 0 24 24"><path d="M18.5 15L5.5 15"/><path d="M16 4L8 4"/><path d="M9 4.5L9 10.2602C9 10.7376 8.82922 11.1992 8.51851 11.5617L3.48149 17.4383C3.17078 17.8008 3 18.2624 3 18.7398V19C3 20.1046 3.89543 21 5 21L19 21C20.1046 21 21 20.1046 21 19V18.7398C21 18.2624 20.8292 17.8008 20.5185 17.4383L15.4815 11.5617C15.1708 11.1992 15 10.7376 15 10.2602L15 4.5"/><path d="M12 9.01L12.01 8.99889"/><path d="M11 2.01L11.01 1.99889"/></symbol>
  <symbol id="ii-database-stats" viewBox="0 0 24 24"><path d="M4 6V12C4 12 4 15 11 15C18 15 18 12 18 12V6"/><path d="M11 3C18 3 18 6 18 6C18 6 18 9 11 9C4 9 4 6 4 6C4 6 4 3 11 3Z"/><path d="M11 21C4 21 4 18 4 18V12"/><path d="M15 21V19"/><path d="M18 21V17"/><path d="M21 21V15"/></symbol>
  <symbol id="ii-cursor-pointer" viewBox="0 0 24 24"><path d="M19.5027 9.96958C20.7073 10.4588 20.6154 12.1941 19.3658 12.5533L13.0605 14.3658L10.1807 20.2606C9.60996 21.4288 7.88499 21.218 7.6124 19.9468L4.67677 6.25646C4.44638 5.18204 5.5121 4.2878 6.53019 4.70126L19.5027 9.96958Z"/></symbol>
  <symbol id="ii-map" viewBox="0 0 24 24"><path d="M9 19L3.78974 20.7368C3.40122 20.8663 3 20.5771 3 20.1675L3 5.43246C3 5.1742 3.16526 4.94491 3.41026 4.86325L9 3M9 19L15 21M9 19L9 3M15 21L20.5897 19.1368C20.8347 19.0551 21 18.8258 21 18.5675L21 3.83246C21 3.42292 20.5988 3.13374 20.2103 3.26325L15 5M15 21L15 5M15 5L9 3"/></symbol>
  <symbol id="ii-filter" viewBox="0 0 24 24"><path d="M3.99961 3H19.9997C20.552 3 20.9997 3.44764 20.9997 3.99987L20.9999 5.58569C21 5.85097 20.8946 6.10538 20.707 6.29295L14.2925 12.7071C14.105 12.8946 13.9996 13.149 13.9996 13.4142L13.9996 19.7192C13.9996 20.3698 13.3882 20.8472 12.7571 20.6894L10.7571 20.1894C10.3119 20.0781 9.99961 19.6781 9.99961 19.2192L9.99961 13.4142C9.99961 13.149 9.89425 12.8946 9.70672 12.7071L3.2925 6.29289C3.10496 6.10536 2.99961 5.851 2.99961 5.58579V4C2.99961 3.44772 3.44732 3 3.99961 3Z"/></symbol>
  </defs></svg>

  <script>
  (function(){
    var root = document.currentScript && document.currentScript.closest ? document.currentScript.closest('.atlx-div-panels') : document.querySelector('.atlx-div-panels');
    if(!root) return;
    var NS = 'http://www.w3.org/2000/svg';
    var INK = 'var(--dp-ink)', ARROW = 'var(--dp-arrow)', LINE = 'var(--dp-line)';
    var PURPLE = 'var(--dp-purple)', AMBER = 'var(--dp-amber)';
    var PENCIL = '#141414';
    var CH = 21, CFONT = 11, GAP = 62;
    function el(name, attrs, parent){
      var n = document.createElementNS(NS, name);
      for(var k in attrs) n.setAttribute(k, attrs[k]);
      parent.appendChild(n);
      return n;
    }
    function txt(parent, x, y, s, size, weight, fill){
      var t = el('text', {x: x, y: y, 'font-size': size, 'font-weight': weight || 400, fill: fill || INK, 'text-anchor': 'middle', 'font-family': '"Cal Sans", sans-serif'}, parent);
      t.textContent = s;
      return t;
    }
    function icon(parent, id, x, y, s, color, w){
      var u = el('use', {href: '#' + id, x: x, y: y, width: s, height: s}, parent);
      u.setAttribute('class', 'atlx-dp-ic');
      u.setAttribute('stroke-width', w || 2);
      u.style.color = color;
      return u;
    }
    function ribbon(g, x0, y0, x1, y1){
      var dx = Math.max(24, (x1 - x0) / 2);
      el('path', {d: 'M' + x0 + ',' + y0 + ' C' + (x0 + dx) + ',' + y0 + ' ' + (x1 - dx) + ',' + y1 + ' ' + x1 + ',' + y1, fill: 'none', stroke: ARROW, 'stroke-width': 5, 'stroke-linecap': 'butt', opacity: 1}, g);
    }
    function chipBox(g, x, y, w, title, chips, stroke){
      var h = 31 + chips.length * CH;
      el('rect', {x: x, y: y, width: w, height: h, rx: 3, fill: 'rgba(255,255,255,0.02)', stroke: stroke, 'stroke-width': 1.5}, g);
      txt(g, x + w / 2, y + 19, title, 12, 700, INK);
      el('line', {x1: x + 8, y1: y + 26, x2: x + w - 8, y2: y + 26, stroke: stroke, 'stroke-width': 1, opacity: 0.35}, g);
      chips.forEach(function(c, i){
        if(i) el('line', {x1: x + 8, y1: y + 26 + i * CH, x2: x + w - 8, y2: y + 26 + i * CH, stroke: stroke, 'stroke-width': 1, opacity: 0.35}, g);
        icon(g, c[0], x + 8, y + 26 + i * CH + (CH - 13) / 2, 13, c[2], 2);
        var ct = el('text', {x: x + 28, y: y + 40 + i * CH, 'font-size': CFONT, fill: INK, 'font-family': '"Cal Sans", sans-serif'}, g);
        ct.textContent = c[1];
      });
      return h;
    }
    function person(g, cx, cy, r){
      el('circle', {cx: cx, cy: cy, r: r + 6, fill: '#ffffff', 'fill-opacity': 0}, g);
      el('circle', {cx: cx, cy: cy, r: r, fill: 'none', stroke: INK, 'stroke-width': 2.5}, g);
      icon(g, 'ii-user', cx - 15, cy - 13, 30, INK, 2);
    }
    function watchGlyph(g, cx, cy){
      var s = 26 / 24;
      var wg = el('g', {transform: 'translate(' + (cx - 13) + ',' + (cy - 13) + ') scale(' + s + ')'}, g);
      ['M16 16.4722V20C16 21.1045 15.1046 22 14 22H10C8.89543 22 8 21.1045 8 20V16.4722', 'M8 7.52779V4C8 2.89543 8.89543 2 10 2H14C15.1046 2 16 2.89543 16 4V7.52779', 'M18 12C18 8.68629 15.3137 6 12 6C8.68629 6 6 8.68629 6 12C6 15.3137 8.68629 18 12 18C15.3137 18 18 15.3137 18 12Z'].forEach(function(d){
        el('path', {d: d, fill: 'none', stroke: INK, 'stroke-width': 2, 'stroke-linecap': 'round', 'stroke-linejoin': 'round'}, wg);
      });
      el('path', {d: 'M14 12H12V10', fill: 'none', stroke: AMBER, 'stroke-width': 2, 'stroke-linecap': 'round', 'stroke-linejoin': 'round'}, wg);
    }
    function hexPath(cx, cy, r){
      var p = [];
      for(var i = 0; i < 6; i++){
        var a = Math.PI / 3 * i;
        p.push((cx + r * Math.cos(a)).toFixed(1) + ',' + (cy + r * Math.sin(a)).toFixed(1));
      }
      return 'M' + p.join('L') + 'Z';
    }
    function browserGlyph(g, cx, cy){
      icon(g, 'ii-mac-os-window', cx - 16, cy - 14, 32, INK, 1.8);
      el('line', {x1: cx - 10, y1: cy + 2, x2: cx + 2, y2: cy + 2, stroke: '#54A468', 'stroke-width': 2}, g);
      el('line', {x1: cx - 10, y1: cy + 6, x2: cx - 2, y2: cy + 6, stroke: '#FFC074', 'stroke-width': 2}, g);
      el('circle', {cx: cx + 14, cy: cy + 10, r: 7, fill: AMBER}, g);
      txt(g, cx + 14, cy + 13.5, '?', 11, 700, '#141414');
    }
    var W = 360, BOXX = 4, BOXW = 176, PERX = 198, HEXX = 305;
    var ROWS_W = [
      {title: 'Watchmaker Apprentice', bg: [['ii-graduation-cap', 'Education / Cert.']], tools: [['ii-precision-tool', 'Watch Assembly Kit']]},
      {title: 'Experienced Watchmaker', bg: [['ii-calendar', 'Years Experience'], ['ii-graduation-cap', 'Education / Cert.']], tools: [['ii-precision-tool', 'Watch Assembly Kit']]},
      {title: 'Experienced Watchmaker', bg: [['ii-calendar', 'Years Experience'], ['ii-graduation-cap', 'Education / Cert.'], ['ii-building', 'External Org. Exp.']], tools: [['ii-precision-tool', 'Watch Assembly Kit']]}
    ];
    var ROWS_S = [
      {title: 'Senior Developer', bg: [['ii-calendar', 'Years Experience'], ['ii-database', 'DBA Background'], ['ii-open-book', 'English Lit. Degree']], tools: [['ii-database-script', 'SQL'], ['ii-message-text', 'Writing & Feedback'], ['ii-code', 'Programming']]},
      {title: 'Testing Analyst', bg: [['ii-calendar', 'Years Experience'], ['ii-database', 'DBA Background'], ['ii-pen-tablet', 'Tech Writer Past']], tools: [['ii-flask', 'Test Automation'], ['ii-database-stats', 'Data Analysis'], ['ii-cursor-pointer', 'Manual Testing']]},
      {title: 'UI/UX Analyst', bg: [['ii-graduation-cap', 'Education / Cert.'], ['ii-light-bulb', 'Design Thinking'], ['ii-people-tag', 'Persona Development']], tools: [['ii-code', 'Programming'], ['ii-light-bulb', 'Design Thinking'], ['ii-map', 'Cust. Journey Mapping']]},
      {title: 'Product Owner', bg: [['ii-network', 'Personal Connections'], ['ii-graduation-cap', 'Education / Cert.'], ['ii-clock', 'Watchmaking Past']], tools: [['ii-flask', 'Test Automation'], ['ii-database-stats', 'Data Analysis'], ['ii-filter', 'Value Stream Mapping']]}
    ];
    function rowBlock(row){ return 31 + (row.bg.length + row.tools.length) * CH; }
    function buildSide(svg, rows, shared, slotH, forceH){
      var bgG = el('g', {}, svg);
      var y = 8, groups = [], cys = [], bot = 8;
      rows.forEach(function(row){
        var block = rowBlock(row);
        var y0 = slotH ? y + (slotH - (block + GAP)) / 2 : y;
        var g = el('g', {'class': 'atlx-dp-row', tabindex: '0', role: 'button', 'aria-label': 'Trace ' + row.title}, svg);
        var chips = row.bg.map(function(c){ return [c[0], c[1], PURPLE]; }).concat(row.tools.map(function(c){ return [c[0], c[1], AMBER]; }));
        var bh = chipBox(g, BOXX, y0, BOXW, row.title, chips, LINE);
        var blockBot = y0 + bh, pcy = y0 + (blockBot - y0) / 2;
        person(g, PERX, pcy, 24);
        groups.push(g);
        cys.push(pcy);
        row._pcy = pcy;
        bot = Math.max(bot, blockBot);
        y += slotH || (block + GAP);
      });
      var hexY = shared ? (cys[0] + cys[cys.length - 1]) / 2 : null;
      rows.forEach(function(row, ri){
        var g = groups[ri], hy = shared ? hexY : row._pcy;
        if(!shared){
          el('path', {d: hexPath(HEXX, hy, 29), fill: 'var(--dp-surface)', stroke: INK, 'stroke-width': 2.5}, g);
          watchGlyph(g, HEXX, hy);
          el('rect', {x: HEXX - 48, y: hy + 32, width: 96, height: 40, rx: 10, fill: 'var(--dp-surface)', stroke: LINE, 'stroke-width': 1.5}, g);
          txt(g, HEXX, hy + 47, 'Consistent', 12, 700, INK);
          txt(g, HEXX, hy + 62, 'Product', 12, 700, INK);
          bot = Math.max(bot, hy + 80);
        }
      });
      if(shared){
        var hg = el('g', {'class': 'atlx-dp-row', tabindex: '0', role: 'button', 'aria-label': 'Novel product outcome shared by all roles'}, svg);
        el('path', {d: hexPath(HEXX, hexY, 30), fill: 'var(--dp-surface)', stroke: INK, 'stroke-width': 2.5}, hg);
        browserGlyph(hg, HEXX, hexY);
        el('rect', {x: HEXX - 54, y: hexY + 32, width: 108, height: 40, rx: 10, fill: 'var(--dp-surface)', stroke: LINE, 'stroke-width': 1.5}, hg);
        txt(hg, HEXX, hexY + 47, 'Novel Product', 12, 700, INK);
        txt(hg, HEXX, hexY + 62, 'Outcome', 12, 700, INK);
        groups.push(hg);
        bot = Math.max(bot, hexY + 80);
      }
      rows.forEach(function(row, ri){
        var hx = HEXX - (shared ? 23 : 22);
        var hyy = shared ? hexY + [-27, -9, 9, 27][ri] : row._pcy;
        ribbon(bgG, PERX + 24, row._pcy, hx, hyy);
      });
      var total = forceH || (bot + 8);
      svg.setAttribute('viewBox', '0 0 ' + W + ' ' + Math.ceil(total));
      groups.forEach(function(g){
        function on(){ groups.forEach(function(o){ o.setAttribute('opacity', o === g ? '1' : '0.3'); }); }
        function off(){ groups.forEach(function(o){ o.setAttribute('opacity', '1'); }); }
        g.addEventListener('mouseenter', on);
        g.addEventListener('mouseleave', off);
        g.addEventListener('focus', on);
        g.addEventListener('blur', off);
      });
      return Math.ceil(total);
    }
    var svgS = root.querySelector('#ddp-svg-s');
    var svgW = root.querySelector('#ddp-svg-w');
    function renderAll(){
      svgS.innerHTML = '';
      svgW.innerHTML = '';
      var hS = buildSide(svgS, ROWS_S, true, null, null);
      buildSide(svgW, ROWS_W, false, hS / ROWS_W.length, hS);
    }
    renderAll();
    if(document.fonts && document.fonts.ready) document.fonts.ready.then(renderAll);
    var viewBtns = root.querySelectorAll('.atlx-dp-view button');
    viewBtns.forEach(function(b){
      b.addEventListener('click', function(){
        root.setAttribute('data-view', b.getAttribute('data-view'));
        viewBtns.forEach(function(o){ o.setAttribute('aria-pressed', String(o === b)); });
      });
    });
  })();
  </script>
</div>

<!-- Atlancia embed: Diversity and complexity - watchmaking vs software team table (interactive).
     Fits the post From Shovels to Software: Why Difference Matters When Things Get Complex.
     The full comparison as a readable table; select an aspect to see why it matters.
     slop-ok: exclamation marks are logical-not operators in inline script, not prose emphasis. -->
<div class="atlx atlx-div-table">
  <style>
    .atlx-div-table {
      --dt-ink: var(--atl-ink, #EEEDED);
      --dt-text: var(--atl-figure-text, #BFBFBF);
      --dt-dim: var(--atl-dim, #9D9D9D);
      --dt-line: var(--atl-line, #373737);
      --dt-surface: var(--atl-surface, #1e1e1e);
      --dt-blue: var(--atl-info, #5B9ED5);
      --dt-green: var(--atl-success, #54A468);
      --dt-amber: var(--atl-accent, #FFC074);
      font-family: "Cal Sans", ui-sans-serif, system-ui, sans-serif;
      background: var(--dt-surface);
      color: var(--dt-text);
      border: 1px solid var(--dt-line);
      border-radius: 6px;
      padding: 1.3rem 1.3rem 1.1rem;
      margin: 2.5rem 0;
      max-width: 100%;
      font-size: 1rem;
      line-height: 1.55;
    }
    .atlx-div-table * { box-sizing: border-box; }
    .atlx-div-table .atlx-dt-title {
      margin: 0 0 .2rem;
      font-family: "Young Serif", Georgia, serif;
      font-weight: 500;
      font-size: 1.25rem;
      line-height: 1.35;
      color: var(--dt-ink);
    }
    .atlx-div-table .atlx-dt-sub { margin: 0 0 .3rem; color: var(--dt-dim); font-size: .95rem; }
    .atlx-div-table table { width: 100%; border-collapse: collapse; font-size: .95rem; margin-top: .9rem; }
    .atlx-div-table th, .atlx-div-table td {
      text-align: left;
      vertical-align: top;
      padding: .6rem .7rem;
      border: 1px solid var(--dt-line);
      color: var(--dt-text);
      background: transparent;
    }
    .atlx-div-table thead th { color: var(--dt-ink); background: rgba(255,255,255,0.03); }
    .atlx-div-table .atlx-dt-rowbtn {
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: .6rem .7rem;
      font: inherit;
      font-weight: 500;
      color: inherit;
      background: transparent;
      border: none;
      border-radius: 0;
      cursor: pointer;
    }
    .atlx-div-table .atlx-dt-rowbtn:hover { background: rgba(255,255,255,0.04); }
    .atlx-div-table .atlx-dt-rowbtn[aria-pressed="true"] { background: rgba(255,192,116,0.12); color: var(--dt-ink); }
    .atlx-div-table .atlx-dt-rowbtn:focus-visible { outline: 2px solid var(--dt-amber); outline-offset: 3px; }
    .atlx-div-table tbody th { position: relative; padding: 0; width: 11rem; min-width: 11rem; color: var(--dt-ink); font-weight: 500; background: rgba(255,255,255,0.05); }
    .atlx-div-table tbody tr[data-active="true"] td,
    .atlx-div-table tbody tr[data-active="true"] th { background: rgba(255,192,116,0.06); }
    .atlx-div-table tbody tr[data-active="true"] th { background: rgba(255,192,116,0.14); }
    .atlx-div-table .atlx-dt-callout {
      margin: 1rem 0 0;
      padding: .7rem .9rem;
      border: 1px solid rgba(255,192,116,0.75);
      border-radius: 6px;
      background: rgba(255,192,116,0.07);
      color: var(--dt-text);
      font-size: .92rem;
    }
    .atlx-div-table .atlx-dt-callout strong { color: var(--dt-ink); }
  </style>

  <h3 class="atlx-dt-title">Watchmaking vs Software Team</h3>
  <p class="atlx-dt-sub">The same five aspects, two different worlds. Select an aspect in the first column.</p>

  <noscript><p style="font-size:.9rem;">This figure needs JavaScript only for row highlighting. The gist: watchmaking is consistent, single-role, one-way work with restricted tools, while software is novel, multi-role, bi-directional work with evolving tools.</p></noscript>

  <table>
    <thead>
      <tr><th scope="col"></th><th scope="col">Watchmaking</th><th scope="col">Software Team</th></tr>
    </thead>
    <tbody>
      <tr data-row="product">
        <th scope="row"><button class="atlx-dt-rowbtn" data-aspect="product" aria-pressed="true">Product</button></th>
        <td>Consistency with design, single product, completed by a single individual.</td>
        <td>Novel, no direct comparison to use as quality check, cannot be completed individually.</td>
      </tr>
      <tr data-row="team">
        <th scope="row"><button class="atlx-dt-rowbtn" data-aspect="team" aria-pressed="false">Team Composition</button></th>
        <td>Individuals on the same task at different skill levels, one role, limited benefit to cross-skilling.</td>
        <td>Significantly different roles working together; cross-skilling benefits emerge and reduce delivery pressure.</td>
      </tr>
      <tr data-row="systems">
        <th scope="row"><button class="atlx-dt-rowbtn" data-aspect="systems" aria-pressed="false">Work Systems</button></th>
        <td>Limited relationship between individuals and team; shipping is one-way, with no updates and limited fixes.</td>
        <td>Deeply relevant team relationships; shipping is bi-directional, with bugs, feature requests and support flowing back.</td>
      </tr>
      <tr data-row="perspectives">
        <th scope="row"><button class="atlx-dt-rowbtn" data-aspect="perspectives" aria-pressed="false">Perspectives</button></th>
        <td>Similar perspectives within a predictable range: years of experience and qualifications.</td>
        <td>Very different perspectives with unpredictable relevance: an English literature background can unexpectedly help.</td>
      </tr>
      <tr data-row="tools">
        <th scope="row"><button class="atlx-dt-rowbtn" data-aspect="tools" aria-pressed="false">Tools and Heuristics</button></th>
        <td>Tools restricted by design to ensure consistency and encourage mastery.</td>
        <td>Wide variety discovered through daily work; combining tools produces new ones, like design thinking with value stream mapping.</td>
      </tr>
    </tbody>
  </table>

  <div class="atlx-dt-callout" data-role="callout" aria-live="polite"></div>

  <script>
  (function(){
    var root = document.currentScript && document.currentScript.closest ? document.currentScript.closest('.atlx-div-table') : document.querySelector('.atlx-div-table');
    if(!root) return;
    var call = root.querySelector('[data-role="callout"]');
    var btns = root.querySelectorAll('[data-aspect]');
    var rows = root.querySelectorAll('[data-row]');
    var WHY = {
      product: '<strong>Product: reproduce the known versus invent the new.</strong> A watch is checked against its design; novel software has no perfect template, so management must match the work.',
      team: '<strong>Team Composition: one role at many levels versus many roles at one table.</strong> Juniors become masters on the same task; software needs dev, test, design and product together.',
      systems: '<strong>Work Systems: one-way delivery versus a running conversation.</strong> A sold watch is done; a shipped release starts a feedback loop of bugs, requests and support.',
      perspectives: '<strong>Perspectives: predictable range versus unpredictable relevance.</strong> Watchmaking rewards deeper sameness; software is saved by the unexpected background.',
      tools: '<strong>Tools and Heuristics: restricted for mastery versus discovered daily.</strong> The watchmaker masters fewer tools; the team routinely combines them into new ones.'
    };
    function setAspect(a){
      btns.forEach(function(b){ b.setAttribute('aria-pressed', String(b.getAttribute('data-aspect') === a)); });
      rows.forEach(function(r){ r.setAttribute('data-active', String(r.getAttribute('data-row') === a)); });
      call.innerHTML = WHY[a];
    }
    btns.forEach(function(b){ b.addEventListener('click', function(){ setAspect(b.getAttribute('data-aspect')); }); });
    setAspect('product');
  })();
  </script>
</div>

The table above almost certainly sells the incredible skills of watchmaking short, but as a model, the key ideas hopefully hold up. The key concepts that we can tease out though are:

- The outcome of work (the product) requires collaboration across multiple skills where individual contributions alone cannot produce value.
- The skills needed to complete work usually require a breadth of skills and knowledge beyond a single individual's capacity; a typical flow of requirements, design, implement, test and deploy may require all of the roles in the diagram to work together.
- The relationship between the team and the work is not predictable: some work may require a large amount of design, while other work may require in-depth knowledge of development or a new business domain.

Unpredictability in the work and the tight coupling between teammates mean that strengthening a team requires more than deepening existing capabilities; it requires adding diverse perspectives and problem-solving heuristics. Instead of matching resumes to fixed task lists, teams could look at upcoming challenges and ask which perspectives are currently missing.

<!-- Atlancia embed: Diversity and complexity - team answers two pieces of work (interactive).
     Fits the post From Shovels to Software: Why Difference Matters When Things Get Complex.
     Select a piece of work to see which roles engage and which overlapping skills carry it.
     slop-ok: exclamation marks are logical-not operators in inline script, not prose emphasis. -->
<!-- Atlancia embed: Diversity and complexity - who answers the work (interactive).
     Fits the post From Shovels to Software: Why Difference Matters When Things Get Complex.
     Two pieces of work list what they require; chips show answered, gap, or stretch, and hovering traces who covers what.
     slop-ok: exclamation marks are logical-not operators in inline script, not prose emphasis. -->
<div class="atlx atlx-div-team">
  <style>
    .atlx-div-team {
      --dt-ink: var(--atl-ink, #EEEDED);
      --dt-text: var(--atl-figure-text, #BFBFBF);
      --dt-dim: var(--atl-dim, #9D9D9D);
      --dt-line: var(--atl-line, #373737);
      --dt-surface: var(--atl-surface, #1e1e1e);
      --dt-amber: var(--atl-accent, #FFC074);
      --dt-purple: #a78bfa;
      --dt-arrow: #9D9D9D;
      font-family: "Cal Sans", ui-sans-serif, system-ui, sans-serif;
      background: var(--dt-surface);
      color: var(--dt-text);
      border: 1px solid var(--dt-line);
      border-radius: 6px;
      padding: 1.3rem 1.3rem 1.1rem;
      margin: 2.5rem 0;
      max-width: 100%;
      font-size: 1rem;
      line-height: 1.55;
    }
    .atlx-div-team * { box-sizing: border-box; }
    .atlx-div-team .atlx-dt-title {
      margin: 0 0 .2rem;
      font-family: "Young Serif", Georgia, serif;
      font-weight: 500;
      font-size: 1.25rem;
      line-height: 1.35;
      color: var(--dt-ink);
    }
    .atlx-div-team .atlx-dt-sub { margin: 0 0 .3rem; color: var(--dt-dim); font-size: .95rem; }
    .atlx-div-team .atlx-dt-legend { display: flex; gap: 1rem; flex-wrap: wrap; margin: .55rem 0 .2rem; font-size: .85rem; color: var(--dt-dim); }
    .atlx-div-team .atlx-dt-legend i { display: inline-block; width: .7em; height: .7em; border-radius: 2px; margin-right: .35em; vertical-align: baseline; }
    .atlx-div-team .atlx-dt-view { display: flex; gap: .5rem; flex-wrap: wrap; margin: .9rem 0 1rem; }
    .atlx-div-team .atlx-dt-view button {
      font: inherit;
      font-size: .88rem;
      font-weight: 600;
      background: transparent;
      color: var(--dt-text);
      border: 1px solid var(--dt-line);
      border-radius: 999px;
      padding: .35rem .8rem;
      cursor: pointer;
    }
    .atlx-div-team .atlx-dt-view button[aria-pressed="true"] { color: var(--dt-ink); border-color: var(--dt-dim); }
    .atlx-div-team .atlx-dt-view button:focus-visible { outline: 2px solid var(--dt-amber); outline-offset: 3px; }
    .atlx-div-team svg { display: block; width: 100%; height: auto; }
    .atlx-div-team .atlx-dt-req { cursor: default; }
  </style>

  <h3 class="atlx-dt-title">Who Answers the Work?</h3>
  <p class="atlx-dt-sub">Two pieces of work land at once. Each lists what it needs; hover a requirement to see who covers it, or hover a person to see what they carry.</p>
  <div class="atlx-dt-legend"><span><i style="background:var(--dt-purple)"></i>Background they arrived with</span><span><i style="background:var(--dt-amber)"></i>Tool the work needs</span><span><i style="border:1px dashed var(--dt-dim)"></i>Gap, nobody has it</span></div>

  <noscript><p style="font-size:.9rem;">This figure needs JavaScript only for highlighting. The gist: a security bug fix is answered except for threat modeling, which nobody on the team has, while a priority feature is fully answered with writing and English literature as stretch that makes it better.</p></noscript>

  <div class="atlx-dt-view" role="group" aria-label="Pieces of work">
    <button data-view="both" aria-pressed="true">Both</button>
    <button data-view="sec" aria-pressed="false">Security fix</button>
    <button data-view="feat" aria-pressed="false">Feature</button>
  </div>

  <svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <symbol id="ii-user" viewBox="0 0 24 24"><path d="M5 20V19C5 15.134 8.13401 12 12 12V12C15.866 12 19 15.134 19 19V20"/><path d="M12 12C14.2091 12 16 10.2091 16 8C16 5.79086 14.2091 4 12 4C9.79086 4 8 5.79086 8 8C8 10.2091 9.79086 12 12 12Z"/></symbol>
  <symbol id="ii-database-script" viewBox="0 0 24 24"><path d="M22 14V6C22 4.34315 20.6569 3 19 3H9C7.34315 3 6 4.34315 6 6V13"/><path d="M12 21H6C3.79086 21 2 19.2091 2 17C2 14.7909 3.79086 13 6 13H17H18C15.7909 13 14 14.7909 14 17C14 19.2091 15.7909 21 18 21C20.2091 21 22 19.2091 22 17V14"/></symbol>
  <symbol id="ii-code" viewBox="0 0 24 24"><path d="M13.5 6L10 18.5"/><path d="M6.5 8.5L3 12L6.5 15.5"/><path d="M17.5 8.5L21 12L17.5 15.5"/></symbol>
  <symbol id="ii-flask" viewBox="0 0 24 24"><path d="M18.5 15L5.5 15"/><path d="M16 4L8 4"/><path d="M9 4.5L9 10.2602C9 10.7376 8.82922 11.1992 8.51851 11.5617L3.48149 17.4383C3.17078 17.8008 3 18.2624 3 18.7398V19C3 20.1046 3.89543 21 5 21L19 21C20.1046 21 21 20.1046 21 19V18.7398C21 18.2624 20.8292 17.8008 20.5185 17.4383L15.4815 11.5617C15.1708 11.1992 15 10.7376 15 10.2602L15 4.5"/><path d="M12 9.01L12.01 8.99889"/><path d="M11 2.01L11.01 1.99889"/></symbol>
  <symbol id="ii-database-stats" viewBox="0 0 24 24"><path d="M4 6V12C4 12 4 15 11 15C18 15 18 12 18 12V6"/><path d="M11 3C18 3 18 6 18 6C18 6 18 9 11 9C4 9 4 6 4 6C4 6 4 3 11 3Z"/><path d="M11 21C4 21 4 18 4 18V12"/><path d="M15 21V19"/><path d="M18 21V17"/><path d="M21 21V15"/></symbol>
  <symbol id="ii-cursor-pointer" viewBox="0 0 24 24"><path d="M19.5027 9.96958C20.7073 10.4588 20.6154 12.1941 19.3658 12.5533L13.0605 14.3658L10.1807 20.2606C9.60996 21.4288 7.88499 21.218 7.6124 19.9468L4.67677 6.25646C4.44638 5.18204 5.5121 4.2878 6.53019 4.70126L19.5027 9.96958Z"/></symbol>
  <symbol id="ii-message-text" viewBox="0 0 24 24"><path d="M7 12L17 12"/><path d="M7 8L13 8"/><path d="M3 20.2895V5C3 3.89543 3.89543 3 5 3H19C20.1046 3 21 3.89543 21 5V15C21 16.1046 20.1046 17 19 17H7.96125C7.35368 17 6.77906 17.2762 6.39951 17.7506L4.06852 20.6643C3.71421 21.1072 3 20.8567 3 20.2895Z"/></symbol>
  <symbol id="ii-map" viewBox="0 0 24 24"><path d="M9 19L3.78974 20.7368C3.40122 20.8663 3 20.5771 3 20.1675L3 5.43246C3 5.1742 3.16526 4.94491 3.41026 4.86325L9 3M9 19L15 21M9 19L9 3M15 21L20.5897 19.1368C20.8347 19.0551 21 18.8258 21 18.5675L21 3.83246C21 3.42292 20.5988 3.13374 20.2103 3.26325L15 5M15 21L15 5M15 5L9 3"/></symbol>
  <symbol id="ii-light-bulb" viewBox="0 0 24 24"><path d="M9 18H15"/><path d="M10 21H14"/><path d="M9.00082 15C9.00098 13 8.50098 12.5 7.50082 11.5C6.50067 10.5 6.02422 9.48689 6.00082 8C5.95284 4.95029 8.00067 3 12.0008 3C16.001 3 18.0488 4.95029 18.0008 8C17.9774 9.48689 17.5007 10.5 16.5008 11.5C15.501 12.5 15.001 13 15.0008 15"/></symbol>
  <symbol id="ii-open-book" viewBox="0 0 24 24"><path d="M12 21V7C12 5.89543 12.8954 5 14 5H21.4C21.7314 5 22 5.26863 22 5.6V18.7143"/><path d="M12 21V7C12 5.89543 11.1046 5 10 5H2.6C2.26863 5 2 5.26863 2 5.6V18.7143"/><path d="M14 19L22 19"/><path d="M10 19L2 19"/><path d="M12 21C12 19.8954 12.8954 19 14 19"/><path d="M12 21C12 19.8954 11.1046 19 10 19"/></symbol>
  <symbol id="ii-bug" viewBox="0 0 24 24"><path d="M12 21C8.13401 21 5 16.9706 5 12C5 7.02944 8.13401 3 12 3C15.866 3 19 7.02944 19 12C19 16.9706 15.866 21 12 21Z"/><path d="M18 17.5L20 19.5"/><path d="M19 9.5L21 8.5"/><path d="M5 9.5L3 8.5"/><path d="M18 8C18 8 15 9 12 9M6 8C6 8 9 9 12 9M12 9V21"/><path d="M5 14H2"/><path d="M22 14H19"/><path d="M6 17.5L4 19.5"/></symbol>
  <symbol id="ii-rocket" viewBox="0 0 24 24"><path d="M16.0614 10.4037L14 17L10 17L7.93865 10.4037C7.35085 8.52273 7.72417 6.47307 8.93738 4.92015L11.5272 1.6052C11.7674 1.29772 12.2326 1.29772 12.4728 1.6052L15.0626 4.92015C16.2758 6.47307 16.6491 8.52273 16.0614 10.4037Z"/><path d="M10 20C10 22 12 23 12 23C12 23 14 22 14 20"/><path d="M8.5 12.5C5 15 7 19 7 19L10 17"/><path d="M15.9312 12.5C19.4312 15 17.4312 19 17.4312 19L14.4312 17"/><path d="M12 11C10.8954 11 10 10.1046 10 9C10 7.89543 10.8954 7 12 7C13.1046 7 14 7.89543 14 9C14 10.1046 13.1046 11 12 11Z"/></symbol>
  <symbol id="ii-shield" viewBox="0 0 24 24"><path d="M5 18L3.13036 4.91253C3.05646 4.39524 3.39389 3.91247 3.90398 3.79912L11.5661 2.09641C11.8519 2.03291 12.1481 2.03291 12.4339 2.09641L20.096 3.79912C20.6061 3.91247 20.9435 4.39524 20.8696 4.91252L19 18C18.9293 18.495 18.5 21.5 12 21.5C5.5 21.5 5.07071 18.495 5 18Z"/></symbol>
  </defs></svg>

  <svg id="ddt-svg" role="img" aria-label="Two pieces of work mapped to the skills they require and the team members who cover them"></svg>

  <script>
  (function(){
    var root = document.currentScript && document.currentScript.closest ? document.currentScript.closest('.atlx-div-team') : document.querySelector('.atlx-div-team');
    if(!root) return;
    var NS = 'http://www.w3.org/2000/svg';
    var INK = 'var(--dt-ink)', DIM = 'var(--dt-dim)', LINE = 'var(--dt-line)', AMBER = 'var(--dt-amber)', ARROW = 'var(--dt-arrow)';
    var PURPLE = 'var(--dt-purple)';
    var CH = 21, CFONT = 11;
    function el(name, attrs, parent){
      var n = document.createElementNS(NS, name);
      for(var k in attrs) n.setAttribute(k, attrs[k]);
      parent.appendChild(n);
      return n;
    }
    function txt(parent, x, y, s, size, weight, fill, anchor){
      var t = el('text', {x: x, y: y, 'font-size': size, 'font-weight': weight || 400, fill: fill || INK, 'text-anchor': anchor || 'middle', 'font-family': '"Cal Sans", sans-serif'}, parent);
      t.textContent = s;
      return t;
    }
    function icon(parent, id, x, y, s, color, w){
      var u = el('use', {href: '#' + id, x: x, y: y, width: s, height: s}, parent);
      u.setAttribute('class', 'atlx-dt-ic');
      u.setAttribute('fill', 'none');
      u.setAttribute('stroke', color);
      u.setAttribute('stroke-width', w);
      u.setAttribute('stroke-linecap', 'round');
      u.setAttribute('stroke-linejoin', 'round');
      return u;
    }
    function ribbon(g, x0, y0, x1, y1){
      var dx = Math.max(24, (x1 - x0) / 2);
      el('path', {d: 'M' + x0 + ',' + y0 + ' C' + (x0 + dx) + ',' + y0 + ' ' + (x1 - dx) + ',' + y1 + ' ' + x1 + ',' + y1, fill: 'none', stroke: ARROW, 'stroke-width': 4, 'stroke-linecap': 'butt', opacity: 1}, g);
    }
    var MEMBERS = [
      {id: 'dev', name: 'Senior Developer', sig: 'SQL · Programming · Writing'},
      {id: 'test', name: 'Testing Analyst', sig: 'Test Automation · Data Analysis'},
      {id: 'ux', name: 'UI/UX Analyst', sig: 'Design · Journey Mapping'},
      {id: 'po', name: 'Product Owner', sig: 'Test Automation · Value Stream'}
    ];
    var WORKS = {
      sec: {title: 'Security Bug Fix', icon: 'ii-bug', reqs: [
        {label: 'SQL', icon: 'ii-database-script', by: ['dev']},
        {label: 'Programming', icon: 'ii-code', by: ['dev']},
        {label: 'Test Automation', icon: 'ii-flask', by: ['test', 'po']},
        {label: 'Data Analysis', icon: 'ii-database-stats', by: ['test', 'po']},
        {label: 'Manual Testing', icon: 'ii-cursor-pointer', by: ['test']},
        {label: 'Incident Writing', icon: 'ii-message-text', by: ['dev']},
        {label: 'Threat Modeling', icon: 'ii-shield', by: [], gap: true}
      ]},
      feat: {title: 'Priority Feature', icon: 'ii-rocket', reqs: [
        {label: 'Programming', icon: 'ii-code', by: ['dev', 'ux']},
        {label: 'Test Automation', icon: 'ii-flask', by: ['test', 'po']},
        {label: 'Manual Testing', icon: 'ii-cursor-pointer', by: ['test']},
        {label: 'Cust. Journey Mapping', icon: 'ii-map', by: ['ux']},
        {label: 'Design Thinking', icon: 'ii-light-bulb', by: ['ux']},
        {label: 'SQL', icon: 'ii-database-script', by: ['dev']},
        {label: 'Writing & Feedback', icon: 'ii-message-text', by: ['dev'], stretch: true},
        {label: 'English Lit. Degree', icon: 'ii-open-book', by: ['dev'], stretch: true, bg: true}
      ]}
    };
    var W = 720, BOXX = 4, BOXW = 300, MEMX = 384, MEMW = 332;
    var svg = root.querySelector('#ddt-svg');
    function scoreLine(w){
      var gaps = [], stretch = 0, base = 0;
      w.reqs.forEach(function(r){ if(r.gap) gaps.push(r.label); else if(r.stretch) stretch++; else base++; });
      var s = base + ' of ' + (base + gaps.length) + ' answered';
      if(gaps.length) s += ' · Gap: ' + gaps.join(', ');
      if(stretch) s += ' + ' + stretch + ' stretch';
      return s;
    }
    function reqRow(g, x, y, w, r, key){
      var rg = el('g', {'class': 'atlx-dt-req', tabindex: '0', 'data-by': r.by.join(' '), 'data-work': key}, g);
      el('rect', {x: x, y: y, width: w, height: CH, fill: '#ffffff', 'fill-opacity': 0}, rg);
      if(r.gap){
        el('rect', {x: x, y: y + 2, width: w, height: CH - 4, rx: 4, fill: 'none', stroke: DIM, 'stroke-width': 1, 'stroke-dasharray': '4 3'}, rg);
        icon(rg, r.icon, x + 8, y + (CH - 13) / 2, 13, DIM, 2);
        var t = el('text', {x: x + 28, y: y + 14, 'font-size': CFONT, fill: DIM, 'font-family': '"Cal Sans", sans-serif'}, rg);
        t.textContent = r.label;
        txt(rg, x + w - 10, y + 14, 'Gap', 10, 700, DIM, 'end');
      } else {
        icon(rg, r.icon, x + 8, y + (CH - 13) / 2, 13, r.bg ? PURPLE : AMBER, 2);
        var t2 = el('text', {x: x + 28, y: y + 14, 'font-size': CFONT, fill: INK, 'font-family': '"Cal Sans", sans-serif'}, rg);
        t2.textContent = r.label;
        if(r.stretch) txt(rg, x + w - 10, y + 14, 'Stretch', 10, 700, AMBER, 'end');
      }
      return rg;
    }
    function workCard(g, x, y, w, key){
      var wk = WORKS[key];
      var h = CH + wk.reqs.length * CH + 24;
      var cg = el('g', {}, g);
      el('rect', {x: x, y: y, width: w, height: h, rx: 3, fill: 'rgba(255,255,255,0.02)', stroke: LINE, 'stroke-width': 1.5}, cg);
      icon(cg, wk.icon, x + 10, y + 4, 15, INK, 2);
      var tt = el('text', {x: x + 32, y: y + 16, 'font-size': 12.5, 'font-weight': 700, fill: INK, 'font-family': '"Cal Sans", sans-serif'}, cg);
      tt.textContent = wk.title;
      el('line', {x1: x + 8, y1: y + CH, x2: x + w - 8, y2: y + CH, stroke: LINE, 'stroke-width': 1, opacity: 0.35}, cg);
      var reqGs = [];
      wk.reqs.forEach(function(r, i){
        reqGs.push(reqRow(cg, x, y + CH + i * CH, w, r, key));
      });
      var st = el('text', {x: x + 12, y: y + h - 8, 'font-size': 10.5, fill: DIM, 'font-family': '"Cal Sans", sans-serif'}, cg);
      st.textContent = scoreLine(wk);
      return {g: cg, h: h, reqGs: reqGs};
    }
    function memberRow(g, x, y, w, m){
      var mg = el('g', {'class': 'atlx-dt-mem', tabindex: '0', 'data-m': m.id}, g);
      el('circle', {cx: x + 22, cy: y + 24, r: 24, fill: '#ffffff', 'fill-opacity': 0}, mg);
      el('circle', {cx: x + 22, cy: y + 24, r: 17, fill: 'none', stroke: INK, 'stroke-width': 2.5}, mg);
      icon(mg, 'ii-user', x + 22 - 11, y + 24 - 10, 22, INK, 2);
      var nt = el('text', {x: x + 48, y: y + 21, 'font-size': 12.5, 'font-weight': 700, fill: INK, 'font-family': '"Cal Sans", sans-serif'}, mg);
      nt.textContent = m.name;
      var st = el('text', {x: x + 48, y: y + 37, 'font-size': 10.5, fill: DIM, 'font-family': '"Cal Sans", sans-serif'}, mg);
      st.textContent = m.sig;
      return mg;
    }
    function dimOthers(reqGs, memGs, keepMembers, keepReqs){
      memGs.forEach(function(mg){
        mg.setAttribute('opacity', !keepMembers || keepMembers.indexOf(mg.getAttribute('data-m')) !== -1 ? '1' : '0.25');
      });
      reqGs.forEach(function(rg){
        if(!keepReqs){ rg.setAttribute('opacity', '1'); return; }
        var by = (rg.getAttribute('data-by') || '').split(' ').filter(Boolean);
        var keep = by.some(function(b){ return keepReqs.indexOf(b) !== -1; });
        rg.setAttribute('opacity', keep ? '1' : '0.25');
      });
    }
    function soloDim(view, memGs){
      var sb = {};
      WORKS[view].reqs.forEach(function(r){ r.by.forEach(function(b){ sb[b] = 1; }); });
      memGs.forEach(function(mg){ if(!sb[mg.getAttribute('data-m')]) mg.setAttribute('opacity', '0.3'); });
    }
    function build(view){
      svg.innerHTML = '';
      var bgG = el('g', {}, svg);
      var keys = view === 'both' ? ['sec', 'feat'] : [view];
      var cards = [], y = 8;
      keys.forEach(function(k, i){
        if(i){ y += 40; }
        var c = workCard(svg, BOXX, y, BOXW, k);
        cards.push({key: k, top: y, h: c.h, reqGs: c.reqGs});
        y += c.h;
      });
      var leftTotal = y;
      var memH = MEMBERS.length * 56 + (MEMBERS.length - 1) * 24;
      var my = Math.max(8, (leftTotal - memH) / 2);
      var memGs = [], memY = {};
      MEMBERS.forEach(function(m, i){
        var yy = my + i * 80;
        memGs.push(memberRow(svg, MEMX, yy, MEMW, m));
        memY[m.id] = yy + 24;
      });
      keys.forEach(function(k){
        var card = cards.filter(function(c){ return c.key === k; })[0];
        var mid = card.top + (CH + 8) / 2 + (WORKS[k].reqs.length * CH) / 4;
        var targets = {};
        WORKS[k].reqs.forEach(function(r){ r.by.forEach(function(b){ targets[b] = 1; }); });
        Object.keys(targets).forEach(function(b){
          ribbon(bgG, BOXX + BOXW, mid, MEMX + 5, memY[b]);
        });
      });
      if(view !== 'both') soloDim(view, memGs);
      var allReq = [];
      cards.forEach(function(c){ allReq = allReq.concat(c.reqGs); });
      allReq.forEach(function(rg){
        var by = (rg.getAttribute('data-by') || '').split(' ').filter(Boolean);
        function on(){ dimOthers(allReq, memGs, by.length ? by : null, null); }
        function off(){ dimOthers(allReq, memGs, null, null); if(view !== 'both') soloDim(view, memGs); }
        rg.addEventListener('mouseenter', on);
        rg.addEventListener('mouseleave', off);
        rg.addEventListener('focus', on);
        rg.addEventListener('blur', off);
      });
      memGs.forEach(function(mg){
        var m = mg.getAttribute('data-m');
        function on(){ dimOthers(allReq, memGs, [m], [m]); }
        function off(){ dimOthers(allReq, memGs, null, null); if(view !== 'both') soloDim(view, memGs); }
        mg.addEventListener('mouseenter', on);
        mg.addEventListener('mouseleave', off);
        mg.addEventListener('focus', on);
        mg.addEventListener('blur', off);
      });
      var total = Math.max(y, my + memH) + 8;
      svg.setAttribute('viewBox', '0 0 ' + W + ' ' + Math.ceil(total));
    }
    var btns = root.querySelectorAll('[data-view]');
    btns.forEach(function(b){
      b.addEventListener('click', function(){
        btns.forEach(function(o){ o.setAttribute('aria-pressed', String(o === b)); });
        build(b.getAttribute('data-view'));
      });
    });
    build('both');
    if(document.fonts && document.fonts.ready) document.fonts.ready.then(function(){ var v = root.querySelector('[data-view][aria-pressed="true"]'); build(v ? v.getAttribute('data-view') : 'both'); });
  })();
  </script>
</div>

Say this team had to balance two very big pieces of work in their system: a large security issue and a challenging high priority feature request. What could they do as a first step? Look at the new work and ask themselves, what they might be missing to address them, and seek out adding that to the team. It is only the team though who could assess this as it is based on their collective skills.

If a team realizes they need fresh capability, recruiting someone with an identical background offers little advantage. When future problems are unpredictable, the strongest move is to hire for cognitive difference, bringing in people whose perspectives and mental models diverge from the existing group.

Cognitive diversity builds their capacity to address the problems of today and better position themselves to address problems in the future.

## Sympathy for the Devil

If a worker shovels coal all day and notices the person next to them shoveled half as much for the same pay, frustration is natural. The output is physical, uniform, and easily measured. The same applies to a watchmaker producing twice the volume of a peer at identical quality.

However, when looking at knowledge work, where complexity is the norm, how can we justify that same sentiment? I’d argue that we simply can’t. The volatility, uncertainty, complexity, and ambiguity of the work environment ought to compel teams to add skills different from their own as a route to making themselves and their teams better. Clinging to rigid qualification checklists only limits the pool of perspectives a team can draw upon. Core competence matters, but when problems demand wide-ranging judgment, we cannot expect to solve new challenges by hiring people who think and work identically to ourselves.
