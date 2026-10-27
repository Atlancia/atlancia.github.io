(function(){
  "use strict";
  var srcText = '', srcName = 'figure.html', figClass = '';
  var fields = []; // {orig, cur, ctx, count}
  var mdText = '', mdName = 'post.md', mdSpan = null; // {start, end} char offsets of figure block

  var $ = function(id){ return document.getElementById(id); };

  function esc(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

  function isCodeString(s){
    if (s.length < 1) return true;
    if (/[#{};\/<>=]/.test(s)) return true;
    if (/^(--|\.|#[0-9a-fA-F])/.test(s)) return true;
    if (/^(none|true|false|null|undefined|\d+(\.\d+)?%?)$/.test(s)) return true;
    if (/^(px|em|rem|deg|ms|s|rect|circle|path|line|text|div|span|svg|button|input|output|table|middle|start|end|round|butt|inline|block|flex|none)$/.test(s)) return true;
    return false;
  }

  function extract(text){
    var map = new Map(); // orig -> {ctx}
    var doc;
    try { doc = new DOMParser().parseFromString(text, 'text/html'); }
    catch(e){ return []; }
    var fig = doc.querySelector('div.atlx');
    var root = fig || doc.body;
    var walker = doc.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function(n){
        var p = n.parentElement;
        if (!p) return NodeFilter.FILTER_REJECT;
        var tag = p.tagName;
        if (tag === 'STYLE' || tag === 'SCRIPT') return NodeFilter.FILTER_REJECT;
        if (!n.nodeValue || !n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function(n){
      var s = n.nodeValue.replace(/\s+/g, ' ').trim();
      if (s.length < 2 || isCodeString(s)) return;
      var p = n.parentElement;
      var ctx = p.tagName.toLowerCase() + (p.className && typeof p.className === 'string' ? '.' + p.className.split(' ')[0] : '');
      if (!map.has(s)) map.set(s, {ctx: 'text: ' + ctx});
    });
    // JS string literals that look like display copy: contain a space or long, no code chars
    var scripts = text.match(/<script>([\s\S]*?)<\/script>/g) || [];
    scripts.forEach(function(block){
      var lit = /'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)"/g, m;
      while ((m = lit.exec(block))){
        var s = (m[1] !== undefined ? m[1] : m[2]).replace(/\\'/g, "'").replace(/\\"/g, '"');
        if (s.indexOf(' ') === -1 && s.length < 12) continue;
        if (isCodeString(s)) continue;
        if (!map.has(s)) map.set(s, {ctx: 'script string'});
      }
    });
    var out = [];
    map.forEach(function(v, k){
      var count = text.split(k).length - 1;
      out.push({orig: k, cur: k, ctx: v.ctx, count: count});
    });
    out.sort(function(a, b){ return b.orig.length - a.orig.length; });
    return out;
  }

  function rebuild(text){
    var t = text;
    var ordered = fields.slice().sort(function(a, b){ return b.orig.length - a.orig.length; });
    ordered.forEach(function(f){
      if (f.cur !== f.orig && f.cur !== '') t = t.split(f.orig).join(f.cur);
    });
    return t;
  }

  function renderFields(){
    var box = $('fields');
    box.innerHTML = '';
    fields.forEach(function(f, i){
      var d = document.createElement('div');
      d.className = 'field' + (f.cur !== f.orig ? ' changed' : '');
      var ctx = document.createElement('div');
      ctx.className = 'ctx';
      ctx.innerHTML = esc(f.ctx) + '<span class="n">' + f.count + '×</span>';
      var ta = document.createElement('textarea');
      ta.value = f.cur;
      ta.rows = f.orig.length > 90 ? 3 : 1;
      ta.addEventListener('input', function(){
        f.cur = ta.value;
        d.classList.toggle('changed', f.cur !== f.orig);
        var o = d.querySelector('.orig');
        if (o) o.textContent = 'was: ' + f.orig;
        update();
      });
      var o = document.createElement('div');
      o.className = 'orig';
      o.textContent = 'was: ' + f.orig;
      d.appendChild(ctx); d.appendChild(ta); d.appendChild(o);
      box.appendChild(d);
    });
  }

  var timer = null;
  function update(){
    clearTimeout(timer);
    timer = setTimeout(function(){
      var built = rebuild(srcText);
      built += '<scr' + 'ipt>document.addEventListener("click",function(e){var t=(e.target.textContent||"").replace(/\\s+/g," ").trim();if(t.length>1){parent.postMessage({studioPick:t},"*");}});</scr' + 'ipt>';
      $('prev').srcdoc = built;
      var dirty = fields.some(function(f){ return f.cur !== f.orig; });
      $('dlSrc').disabled = !dirty;
      var n = fields.filter(function(f){ return f.cur !== f.orig; }).length;
      $('status').innerHTML = dirty ? ('<b>' + n + '</b> edited string' + (n === 1 ? '' : 's') + ' in <b>' + esc(figClass || srcName) + '</b>') : 'No edits yet.';
      var canMd = dirty && mdSpan !== null;
      $('dlMd').disabled = !canMd;
    }, 250);
  }

  function findSpan(text, cls){
    // balanced-div span starting at the figure comment or div
    var lines = text.split('\n');
    var divIdx = -1;
    for (var i = 0; i < lines.length; i++){
      if (lines[i].indexOf(cls) !== -1 && lines[i].indexOf('<div') !== -1){ divIdx = i; break; }
    }
    if (divIdx === -1) return null;
    var start = divIdx;
    while (start > 0 && lines[start].trim().indexOf('<!--') !== 0) start--;
    var depth = 0, end = -1;
    for (var j = divIdx; j < lines.length; j++){
      var opens = (lines[j].match(/<div[\s>]/g) || []).length;
      var closes = (lines[j].match(/<\/div>/g) || []).length;
      depth += opens - closes;
      if (depth <= 0){ end = j; break; }
    }
    if (end === -1) return null;
    var before = lines.slice(0, start).join('\n').length + (start > 0 ? 1 : 0);
    var spanText = lines.slice(start, end + 1).join('\n');
    return {start: before, end: before + spanText.length};
  }

  function loadSource(text, name){
    srcText = text; srcName = name || 'figure.html';
    var m = text.match(/<div class="atlx (atlx-[a-z0-9-]+)"/);
    figClass = m ? m[1] : '';
    fields = extract(text);
    renderFields();
    update();
    if (mdText) locateMd();
  }

  function locateMd(){
    mdSpan = figClass ? findSpan(mdText, figClass) : null;
    var w = $('spanWarn');
    if (mdText && !mdSpan){
      w.classList.remove('hidden');
      w.textContent = 'Post loaded but no .' + figClass + ' figure block found in it. Check the figure is pasted in that post.';
    } else {
      w.classList.add('hidden');
    }
    update();
  }

  function readFile(file, cb){
    var r = new FileReader();
    r.onload = function(){ cb(String(r.result || '')); };
    r.readAsText(file);
  }

  $('pickSrc').addEventListener('change', function(e){
    var f = e.target.files[0];
    if (!f) return;
    readFile(f, function(t){ loadSource(t, f.name); });
  });
  $('loadPaste').addEventListener('click', function(){
    var t = $('paste').value;
    if (!t.trim()) return;
    loadSource(t, 'pasted.html');
  });
  $('pickMd').addEventListener('change', function(e){
    var f = e.target.files[0];
    if (!f) return;
    readFile(f, function(t){ mdText = t; mdName = f.name; locateMd(); });
  });

  function download(name, text){
    var b = new Blob([text], {type: 'text/plain;charset=utf-8'});
    var a = document.createElement('a');
    a.href = URL.createObjectURL(b);
    a.download = name;
    document.body.appendChild(a);
    a.click();
    setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }

  $('dlSrc').addEventListener('click', function(){
    download(srcName, rebuild(srcText));
  });
  $('dlMd').addEventListener('click', function(){
    if (mdSpan === null) return;
    var before = mdText.slice(0, mdSpan.start);
    var span = mdText.slice(mdSpan.start, mdSpan.end);
    var after = mdText.slice(mdSpan.end);
    download(mdName, before + rebuild(span) + after);
    locateMd();
  });

  var HOSTED = false;
  var pickSeq = 0;
  function apiToken(){
    var m = document.querySelector('meta[name="ab-token"]');
    return m ? m.getAttribute('content') : '';
  }
  function apiGet(path, cb){
    fetch(path, {headers: {'Accept': 'application/json'}}).then(function(r){
      if (!r.ok) throw new Error('http ' + r.status);
      return r.json();
    }).then(function(j){ cb(null, j); }, function(e){ cb(e); });
  }
  function wirePublish(){
    var b = $('dlSrc');
    b.textContent = 'Publish';
    b.classList.add('primary');
    $('dlMd').style.display = 'none';
    b.addEventListener('click', function(){
      if (mdSpan === null){ $('status').textContent = 'No figure block located in post.'; return; }
      var oldSpan = mdText.slice(mdSpan.start, mdSpan.end);
      var payload = {
        post: mdName, cls: figClass, srcFile: srcName,
        srcText: rebuild(srcText), spanText: rebuild(oldSpan)
      };
      b.disabled = true;
      $('status').textContent = 'Publishing...';
      fetch('/api/studio/save', {
        method: 'POST',
        headers: {'Content-Type': 'application/json', 'X-AntiBrain-Request': apiToken()},
        body: JSON.stringify(payload)
      }).then(function(r){ return r.json().then(function(j){ return {ok: r.ok, j: j}; }); }).then(function(res){
        b.disabled = false;
        if (res.ok && res.j.success){
          srcText = payload.srcText;
          mdText = mdText.slice(0, mdSpan.start) + payload.spanText + mdText.slice(mdSpan.end);
          fields.forEach(function(f){ f.orig = f.cur; });
          renderFields();
          locateMd();
          $('status').innerHTML = 'Published <b>' + res.j.srcBytes + '</b> + <b>' + res.j.mdBytes + '</b> bytes.';
        } else {
          $('status').textContent = 'Publish failed: ' + ((res.j && res.j.error) || 'unknown');
        }
      }, function(e){
        b.disabled = false;
        $('status').textContent = 'Publish failed: ' + e;
      });
    }, {once: true});
  }
  window.addEventListener('message', function(ev){
    var t = ev.data && ev.data.studioPick;
    if (!t) return;
    var norm = function(s){ return s.replace(/\s+/g, ' ').trim(); };
    t = norm(t);
    var idx = -1;
    fields.forEach(function(f, i){
      if (idx !== -1) return;
      var c = norm(f.cur);
      if (c === t || c.indexOf(t) !== -1 || (t.length > 12 && t.indexOf(c) !== -1)) idx = i;
    });
    if (idx === -1) return;
    var card = document.querySelectorAll('.field')[idx];
    var ta = card.querySelector('textarea');
    card.scrollIntoView({block: 'nearest', behavior: 'smooth'});
    ta.focus();
    card.classList.remove('picked');
    void card.offsetWidth;
    card.classList.add('picked');
  });

  (function initIndex(){
    function fromEntries(entries, remote){
      var wrap = document.createElement('div');
      wrap.className = 'bar';
      var html = '<div><label>Post</label><select id="idxPost"></select></div>' +
        '<div><label>Figure in post</label><select id="idxFig"></select></div>' +
        '<div><label>&nbsp;</label><span class="status">' + (remote ? 'Live index from dashboard' : 'Index built ' + FIGURE_INDEX.built + ' (' + entries.length + ' figures)') + '</span></div>';
      wrap.innerHTML = html;
      var bar = document.querySelector('.bar');
      bar.parentNode.insertBefore(wrap, bar.nextSibling);
      var posts = [];
      entries.forEach(function(e){ if (posts.indexOf(e.post) === -1) posts.push(e.post); });
      var ps = document.getElementById('idxPost');
      posts.forEach(function(p){
        var o = document.createElement('option'); o.value = p; o.textContent = p; ps.appendChild(o);
      });
      var fs = document.getElementById('idxFig');
      function fillFigs(){
        fs.innerHTML = '';
        entries.filter(function(e){ return e.post === ps.value; }).forEach(function(e){
          var o = document.createElement('option'); o.value = e.cls;
          o.textContent = e.cls + ((e.srcText || e.srcFile) ? '' : ' (no source found)');
          fs.appendChild(o);
        });
        pickFig();
      }
      function pickFig(){
        var cls = fs.value;
        var found = entries.filter(function(x){ return x.post === ps.value && x.cls === cls; })[0];
        if (!found) return;
        if (remote && !(found.srcText && found.mdText)){
          var seq = ++pickSeq;
          apiGet('/api/studio/figure?post=' + encodeURIComponent(found.post) + '&cls=' + encodeURIComponent(found.cls), function(err, j){
            if (seq !== pickSeq) return;
            if (err || !j || !j.srcText){ $('status').textContent = 'Could not load figure.'; return; }
            found.srcText = j.srcText; found.mdText = j.mdText; found.srcFile = j.srcFile;
            loadSource(found.srcText, found.srcFile || (cls + '.html'));
            mdText = found.mdText; mdName = found.post; locateMd();
          });
          return;
        }
        if (found.srcText) loadSource(found.srcText, found.srcFile || (cls + '.html'));
        else if (found.mdText) {
          var sp = findSpan(found.mdText, found.cls);
          if (sp) loadSource(found.mdText.slice(sp.start, sp.end), (cls + '.html'));
        }
        if (found.mdText){ mdText = found.mdText; mdName = found.post; locateMd(); }
      }
      ps.addEventListener('change', fillFigs);
      fs.addEventListener('change', pickFig);
      fillFigs();
    }
    apiGet('/api/studio/index', function(err, j){
      if (!err && j && j.entries && j.entries.length){
        HOSTED = true;
        wirePublish();
        fromEntries(j.entries, true);
      } else if (typeof FIGURE_INDEX !== 'undefined' && FIGURE_INDEX.entries && FIGURE_INDEX.entries.length){
        fromEntries(FIGURE_INDEX.entries, false);
      }
    });
  })();
})();
