---
title: "Building a Trade-off Mentality"
date: "2023-05-06T00:00:00-04:00"
lastmod: "2026-09-30T17:06:42-04:00"
slug: "trade-off-mentality"
url: "/trade-off-mentality.html"
type: posts
media_id: 3
authors: ["liam"]
meta_robots: "index, follow"
featureimage: "media/posts/3/tradem-cover-rest.webp"
coverMotion: "tradem-cover"
coverMotionBase: 0.8
---
> *If you wish to make an apple pie from scratch, you must first invent the universe.  
> – Carl Sagan*

Carl Sagan’s famous quote inspires deeper thought of how connected our universe is, that to “make an apple pie from scratch” you can keep going one step backwards until one has to “invent the universe.” What struck me was that somewhere between the start of the universe and baking the pie, we had to draw a line for what we consider "from scratch." Why would buying pre-made pie crust feel like “cheating,” yet buying pre-ground flour would not? What lines have we drawn without much thought of how we choose them?

Let’s imagine a manager asking someone to take on a new task. Consider the assumptions that may be at play: the manager assumes the employee can do the task, will listen, will understand, and could do the work without sacrificing their current efforts. What trade-offs are involved? What work might suffer to focus on this new task? How would the manager or the employee differ in their views of what could be dropped to accommodate the new work and what might those different opinions tell us about what each of them values?

I’ve found it useful to ask myself what assumptions I’m making when I make a statement. This approach helps me identify what trade-offs and assumed truths may need to be evaluated to see if they’re still true. However, within my head, I can take a far more confrontational approach to my thoughts than I may with others. I developed a more inquisitive approach: a "trade-off mentality" designed to surface premises collaboratively and open up honest discussion about why we choose one path over another.

While I do believe this is a general toolkit that has helped me think better across multiple domains, the focus in the text below will be largely on software development and teams.

This mental toolkit is based on four core ideas:

- First, there ain't no such thing as a free lunch: we cannot get something without giving something up.
- Second, trade-offs allow us to question what we value.
- Third, trade-offs offer an opportunity for us to discuss ways of splitting or breaking down things we bundle together or associate.
- Finally, when we evaluate decisions and assumptions, we can gain additional insight by asking ourselves who is being served by balancing and weighing valuations.

## Idea 1: There ain’t no such thing as a free lunch

Central to the first idea is recognizing that every endeavor carries a cost and works within constraints; no lunch is truly free. Choosing to stay up late for another episode of *Succession* means accepting that tomorrow morning will suck. We are constrained by time, energy, money, and many other limits.

For instance, we can look at even subtle constraints to a team’s productivity. My favourite to consider is the cognitive load incurred by increasing work complexity (or simply using the idea of mental energy). Such complexity may hinder growth, or necessitate trade-offs in terms of longer learning, more challenging onboarding, or higher rates of incidents. Surfacing impacts from complexity could help identify future challenges and uncover risks we might not be willing to accept.

Indicator statements such as: “We should make time for training,” “I would like you to deliver this as well,” or “The team must assume accountability for this new system” may serve as potential triggers for conversations on underlying assumptions and required trade-offs. The figure below shows a hypothetical model of transition for a team taking on a new application, in which a new idea surfaces: the hidden cost of assuming new operational accountabilities.

<!-- Atlancia embed: Trade-off mentality - team capacity allocation (interactive).
     Fits the post Building a Trade-off Mentality.
     Compare steady state vs transition, or use slider to explore tradeoffs.
     slop-ok: exclamation marks are logical-not operators in inline script, not prose emphasis. -->
<div class="atlx atlx-trade-capacity">
  <style>
    .atlx-trade-capacity {
      --tc-ink: var(--atl-ink, #EEEDED);
      --tc-text: var(--atl-figure-text, #BFBFBF);
      --tc-dim: var(--atl-dim, #9D9D9D);
      --tc-line: var(--atl-line, #373737);
      --tc-surface: var(--atl-surface, #1e1e1e);
      --tc-blue: var(--atl-info, #5B9ED5);
      --tc-green: var(--atl-success, #54A468);
      --tc-amber: var(--atl-accent, #FFC074);
      --tc-pink: #f43f5e;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--tc-surface);
      color: var(--tc-text);
      border: 1px solid var(--tc-line);
      border-radius: 6px;
      padding: 1.3rem 1.3rem 1.1rem;
      margin: 2.5rem 0;
      max-width: 100%;
      font-size: 1rem;
      line-height: 1.55;
    }
    .atlx-trade-capacity * { box-sizing: border-box; }
    .atlx-trade-capacity .atlx-tc-title {
      margin: 0 0 .2rem;
      font-family: "Young Serif", Georgia, serif;
      font-weight: 500;
      font-size: 1.25rem;
      line-height: 1.35;
      color: var(--tc-ink);
    }
    .atlx-trade-capacity .atlx-tc-sub {
      margin: 0 0 .3rem;
      color: var(--tc-dim);
      font-size: .95rem;
    }
    .atlx-trade-capacity .atlx-tc-btns {
      display: flex;
      gap: .5rem;
      flex-wrap: wrap;
      margin: .9rem 0 1rem;
    }
    .atlx-trade-capacity .atlx-tc-btns button {
      font: inherit;
      font-size: .88rem;
      font-weight: 600;
      background: transparent;
      color: var(--tc-text);
      border: 1px solid var(--tc-line);
      border-radius: 999px;
      padding: .35rem .8rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: .45rem;
    }
    .atlx-trade-capacity .atlx-tc-btns button[aria-pressed="true"] {
      color: var(--tc-ink);
      border-color: var(--tc-dim);
    }
    .atlx-trade-capacity .atlx-tc-btns button:focus-visible {
      outline: 2px solid var(--tc-amber);
      outline-offset: 3px;
    }
    .atlx-trade-capacity .atlx-tc-slider {
      display: none;
      align-items: center;
      gap: .8rem;
      flex-wrap: wrap;
      margin: -.4rem 0 1rem;
      color: var(--tc-text);
      font-size: .9rem;
    }
    .atlx-trade-capacity .atlx-tc-slider.active {
      display: flex;
    }
    .atlx-trade-capacity .atlx-tc-slider label {
      color: var(--tc-dim);
    }
    .atlx-trade-capacity .atlx-tc-slider input[type="range"] {
      -webkit-appearance: none;
      appearance: none;
      width: min(320px, 100%);
      height: 28px;
      background: transparent;
      cursor: pointer;
    }
    .atlx-trade-capacity .atlx-tc-slider input[type="range"]::-webkit-slider-runnable-track {
      height: 6px;
      border-radius: 999px;
      background: var(--tc-line);
    }
    .atlx-trade-capacity .atlx-tc-slider input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--tc-amber);
      border: 3px solid var(--tc-surface);
      margin-top: -8px;
    }
    .atlx-trade-capacity .atlx-tc-slider input[type="range"]::-moz-range-track {
      height: 6px;
      border-radius: 999px;
      background: var(--tc-line);
    }
    .atlx-trade-capacity .atlx-tc-slider input[type="range"]::-moz-range-thumb {
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--tc-amber);
      border: 3px solid var(--tc-surface);
    }
    .atlx-trade-capacity .atlx-tc-slider output {
      font-variant-numeric: tabular-nums;
      color: var(--tc-amber);
      font-weight: 600;
      min-width: 3ch;
      text-align: right;
    }
    .atlx-trade-capacity .atlx-tc-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1rem;
    }
    .atlx-trade-capacity .atlx-tc-panel {
      border: 1px solid var(--tc-line);
      border-radius: 6px;
      background: transparent;
      overflow: hidden;
    }
    .atlx-trade-capacity .atlx-tc-panel.single {
      grid-column: 1 / -1;
    }
    .atlx-trade-capacity .atlx-tc-panel.is-before {
      border-style: dashed;
    }
    .atlx-trade-capacity .atlx-tc-panel.is-before .atlx-tc-panel-header {
      background: rgba(255,255,255,0.02);
    }
    .atlx-trade-capacity .atlx-tc-panel.is-after {
      border-color: var(--tc-amber);
      border-width: 1px;
    }
    .atlx-trade-capacity .atlx-tc-panel.is-after .atlx-tc-panel-header {
      background: rgba(255,192,116,0.08);
      border-bottom-color: var(--tc-amber);
    }
    .atlx-trade-capacity .atlx-tc-tag {
      margin-left: auto;
      font-size: .72rem;
      font-weight: 600;
      letter-spacing: .1em;
      text-transform: uppercase;
      color: var(--tc-dim);
    }
    .atlx-trade-capacity .atlx-tc-panel.is-after .atlx-tc-tag { color: var(--tc-amber); }
    .atlx-trade-capacity .atlx-tc-panel-header {
      display: flex;
      align-items: center;
      gap: .7rem;
      padding: .7rem 1rem;
      border-bottom: 1px solid var(--tc-line);
    }
    .atlx-trade-capacity .atlx-tc-panel-title {
      font-weight: 600;
      color: var(--tc-ink);
    }
    .atlx-trade-capacity .atlx-tc-team {
      width: 32px;
      height: 32px;
      border-radius: 6px;
      border: 1px solid var(--tc-line);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--tc-dim);
    }
    .atlx-trade-capacity .atlx-tc-body {
      display: grid;
      gap: .7rem;
      padding: .9rem 1rem 1rem;
    }
    .atlx-trade-capacity .atlx-tc-row {
      display: grid;
      grid-template-columns: minmax(210px, auto) 1fr auto;
      align-items: center;
      gap: 1rem;
    }
    @media (max-width: 560px) {
      .atlx-trade-capacity .atlx-tc-row {
        grid-template-columns: 1fr;
        gap: .4rem;
      }
      .atlx-trade-capacity .atlx-tc-percent {
        justify-self: start;
      }
    }
    .atlx-trade-capacity .atlx-tc-label {
      color: var(--tc-text);
      font-size: .85rem;
      white-space: nowrap;
    }
    .atlx-trade-capacity .atlx-tc-track {
      position: relative;
      height: 10px;
      border-radius: 999px;
      background: transparent;
      border: 1px solid var(--tc-line);
      overflow: hidden;
    }
    .atlx-trade-capacity .atlx-tc-bar {
      position: absolute;
      inset: 0 auto 0 0;
      border-radius: 999px;
      transition: width .4s ease;
    }
    .atlx-trade-capacity .atlx-tc-bar.critical { background: var(--tc-pink); }
    .atlx-trade-capacity .atlx-tc-bar.new { background: var(--tc-amber); }
    .atlx-trade-capacity .atlx-tc-bar.growth { background: var(--tc-green); }
    .atlx-trade-capacity .atlx-tc-percent {
      font-variant-numeric: tabular-nums;
      color: var(--tc-ink);
      font-size: .85rem;
      min-width: 3ch;
      text-align: right;
    }
    .atlx-trade-capacity .atlx-tc-inline {
      position: relative;
      margin: .5rem 0 0;
      padding: .6rem .9rem;
      border: 1px solid rgba(255,192,116,0.75);
      border-radius: 6px;
      background: rgba(255,192,116,0.07);
      color: var(--tc-text);
      font-size: .9rem;
      line-height: 1.5;
    }
    .atlx-trade-capacity .atlx-tc-inline::before {
      content: "";
      position: absolute;
      top: -8px;
      left: 2.2rem;
      width: 0;
      height: 0;
      border-left: 8px solid transparent;
      border-right: 8px solid transparent;
      border-bottom: 8px solid rgba(255,192,116,0.75);
    }
    .atlx-trade-capacity .atlx-tc-inline strong { color: var(--tc-ink); }
    .atlx-trade-capacity .atlx-tc-inline.up {
      border-color: rgba(244,63,94,0.8);
      background: rgba(244,63,94,0.07);
    }
    .atlx-trade-capacity .atlx-tc-inline.up::before { border-bottom-color: rgba(244,63,94,0.8); }
    .atlx-trade-capacity .atlx-tc-inline.down {
      border-color: rgba(84,164,104,0.8);
      background: rgba(84,164,104,0.07);
    }
    .atlx-trade-capacity .atlx-tc-inline.down::before { border-bottom-color: rgba(84,164,104,0.8); }
    .atlx-trade-capacity [data-view="slider"] { display: none; }
    .atlx-trade-capacity[data-mode="slider"] [data-view="compare"] { display: none; }
    .atlx-trade-capacity[data-mode="slider"] [data-view="slider"] { display: grid; }
  </style>

  <h3 class="atlx-tc-title">Team Capacity During a Transition</h3>
  <p class="atlx-tc-sub">There ain't no such thing as a free lunch. Adding work means something else gets less capacity.</p>

  <noscript><p style="font-size:.9rem;">This figure needs JavaScript. The gist: before a transition the team spends most capacity on the critical system with room for training, while in the first year of transition a new application takes half of capacity and both core work and training shrink.</p></noscript>

  <div class="atlx-tc-btns">
    <button data-action="mode" data-mode="compare" aria-pressed="true">Compare states</button>
    <button data-action="mode" data-mode="slider" aria-pressed="false">Transition slider</button>
  </div>

  <div class="atlx-tc-slider" data-role="slider">
    <label for="tc-intensity">Transition intensity</label>
    <input id="tc-intensity" type="range" min="0" max="100" value="0">
    <output for="tc-intensity">0%</output>
  </div>

  <div class="atlx-tc-grid" data-view="compare">
    <article class="atlx-tc-panel is-before">
      <header class="atlx-tc-panel-header">
        <div class="atlx-tc-team">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
            <circle cx="9" cy="7" r="4"></circle>
            <path d="M22 21v-2a4 4 0 0 0-3-3.87"></path>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
          </svg>
        </div>
        <div class="atlx-tc-panel-title">Before Transition</div>
        <span class="atlx-tc-tag">Before</span>
      </header>
      <div class="atlx-tc-body">
        <div class="atlx-tc-row">
          <div class="atlx-tc-label">Critical System</div>
          <div class="atlx-tc-track"><div class="atlx-tc-bar critical" style="width: 80%"></div></div>
          <div class="atlx-tc-percent">80%</div>
        </div>
        <div class="atlx-tc-row">
          <div class="atlx-tc-label">Training &amp; Development</div>
          <div class="atlx-tc-track"><div class="atlx-tc-bar growth" style="width: 20%"></div></div>
          <div class="atlx-tc-percent">20%</div>
        </div>
      </div>
    </article>
    <article class="atlx-tc-panel is-after">
      <header class="atlx-tc-panel-header">
        <div class="atlx-tc-team">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
            <circle cx="9" cy="7" r="4"></circle>
            <path d="M22 21v-2a4 4 0 0 0-3-3.87"></path>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
          </svg>
        </div>
        <div class="atlx-tc-panel-title">First Year of Transition</div>
        <span class="atlx-tc-tag">After</span>
      </header>
      <div class="atlx-tc-body">
        <div class="atlx-tc-row">
          <div class="atlx-tc-label">Critical System</div>
          <div class="atlx-tc-track"><div class="atlx-tc-bar critical" style="width: 40%"></div></div>
          <div class="atlx-tc-percent">40%</div>
        </div>
        <p class="atlx-tc-inline up"><strong>Pushes out core work.</strong> Down from 80% to 40% to make room for the new system.</p>
        <div class="atlx-tc-row">
          <div class="atlx-tc-label">New Low Availability Application</div>
          <div class="atlx-tc-track"><div class="atlx-tc-bar new" style="width: 50%"></div></div>
          <div class="atlx-tc-percent">50%</div>
        </div>
        <p class="atlx-tc-inline"><strong>This new load is the tradeoff.</strong> It takes half of capacity, squeezing out development of people and product.</p>
        <div class="atlx-tc-row">
          <div class="atlx-tc-label">Training &amp; Development</div>
          <div class="atlx-tc-track"><div class="atlx-tc-bar growth" style="width: 10%"></div></div>
          <div class="atlx-tc-percent">10%</div>
        </div>
        <p class="atlx-tc-inline down"><strong>Less room to improve.</strong> Halved from 20% to 10%, so the team has less capacity to develop its people and its product over the long run.</p>
      </div>
    </article>
  </div>

  <div class="atlx-tc-grid" data-view="slider">
    <article class="atlx-tc-panel single">
      <header class="atlx-tc-panel-header">
        <div class="atlx-tc-team">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
            <circle cx="9" cy="7" r="4"></circle>
            <path d="M22 21v-2a4 4 0 0 0-3-3.87"></path>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
          </svg>
        </div>
        <div class="atlx-tc-panel-title">Team Capacity Allocation</div>
      </header>
      <div class="atlx-tc-body">
        <div class="atlx-tc-row">
          <div class="atlx-tc-label">Critical System</div>
          <div class="atlx-tc-track"><div class="atlx-tc-bar critical" data-bar="critical"></div></div>
          <div class="atlx-tc-percent" data-pct="critical">80%</div>
        </div>
        <div class="atlx-tc-row">
          <div class="atlx-tc-label">New Low Availability Application</div>
          <div class="atlx-tc-track"><div class="atlx-tc-bar new" data-bar="new"></div></div>
          <div class="atlx-tc-percent" data-pct="new">0%</div>
        </div>
        <div class="atlx-tc-row">
          <div class="atlx-tc-label">Training &amp; Development</div>
          <div class="atlx-tc-track"><div class="atlx-tc-bar growth" data-bar="growth"></div></div>
          <div class="atlx-tc-percent" data-pct="growth">20%</div>
        </div>
      </div>
    </article>
  </div>

  <script>
  (function(){
    var root = document.currentScript && document.currentScript.closest ? document.currentScript.closest('.atlx-trade-capacity') : document.querySelector('.atlx-trade-capacity');
    if(!root) return;
    var modeBtns = root.querySelectorAll('[data-action="mode"]');
    var slider = root.querySelector('[data-role="slider"]');
    var range = root.querySelector('#tc-intensity');
    var out = root.querySelector('output[for="tc-intensity"]');
    var barC = root.querySelector('[data-bar="critical"]');
    var barN = root.querySelector('[data-bar="new"]');
    var barG = root.querySelector('[data-bar="growth"]');
    var pctC = root.querySelector('[data-pct="critical"]');
    var pctN = root.querySelector('[data-pct="new"]');
    var pctG = root.querySelector('[data-pct="growth"]');
    function setMode(m){
      root.setAttribute('data-mode', m);
      modeBtns.forEach(function(b){ b.setAttribute('aria-pressed', String(b.getAttribute('data-mode') === m)); });
      if(m === 'slider'){ slider.classList.add('active'); update(); }
      else { slider.classList.remove('active'); }
    }
    modeBtns.forEach(function(b){ b.addEventListener('click', function(){ setMode(b.getAttribute('data-mode')); }); });
    function update(){
      var t = parseInt(range.value, 10) || 0;
      out.textContent = t + '%';
      var c = Math.round(80 - (40 * t / 100));
      var g = Math.round(20 - (10 * t / 100));
      var n = Math.round(50 * t / 100);
      barC.style.width = c + '%';
      barN.style.width = n + '%';
      barG.style.width = g + '%';
      pctC.textContent = c + '%';
      pctN.textContent = n + '%';
      pctG.textContent = g + '%';
    }
    range.addEventListener('input', update);
    barC.style.width = '80%'; barN.style.width = '0%'; barG.style.width = '20%';
    setMode('compare');
  })();
  </script>
</div>


A classic trade-off in systems development, for example, is the balance between investing in new features versus reducing technical debt. A team’s ability to discuss and evaluate these classic trade-offs can have a significant impact on their long-term success. Investments in technical debt reduction, while not as glamorous as new features, can often lead to more sustainable development and increased capacity for future innovation.

By carefully examining statements, especially those that indicate a “more X” is possible, we can surface implicit assumptions and trade-offs, while individuals and teams can better understand the consequences of their decisions and align their actions with their values and goals.

## Idea 2: Trade-off decisions offer a space to inspect values

When confronted with a potential trade-off, we have a space to ask ourselves, “Why did I choose X over Y?” Is that choice consistent with my values? With a team’s values? With an organization’s goals?

The act of questioning myself has helped me gain insight into my own beliefs and assumptions. When considering whether to speak up in a group setting, for instance, I consider if I am preventing someone else from contributing or if simply presenting an opinion may discourage dissenting viewpoints. Even the subtle act of supporting an idea may make dissenting viewpoints harder to bring forward.

When faced with a difficult decision, individuals may engage in a process of introspection, carefully evaluating the relative importance of the available options and the factors that inform those values. This process can be particularly valuable in group settings where individuals with different skill sets and viewpoints must navigate trade-offs to achieve a common goal.

But, evaluating trade-offs is not just an individual activity. Teams and organizations can also benefit from examining the trade-offs they make in pursuit of their goals. By holding up a mirror to themselves and asking if they are truly living up to their values, teams can identify areas for improvement and develop strategies to better align their actions with their goals. For example, a team tasked with reporting weekly on their progress may be trading off valuable development time and energy for the sake of reporting. By examining this trade-off, the team could question which benefits of reporting outweigh the costs and adjust their approach accordingly.

This particular idea may be more difficult to have an open dialogue about because it may challenge deeply held assumptions. Two areas I have had difficult discussions about have been the topics of reporting and options analysis. If we believe our value is to deliver work and support clients/customers/users, both would be “wastes” from a Lean perspective. Options analysis embeds a guarantee of waste; that if N+1 options are presented and 1 option is selected the development of N was largely waste. Softer language, of relative value and checking against objectives, helps serve a less aggressive proposition.

Similarly, organizations with a mission to be inclusive may need to examine the trade-offs between objective hiring criteria and the desire to attract a more diverse pool of candidates. Organizations could dig deeper into whether they are truly living up to their values and identify ways to make their processes more equitable and inclusive. Perhaps recognizing that adhering to a strict process may reduce the impact of individual biases while amplifying the impact of structural ones. *e.g. a hiring process that takes 3 months to complete, requires a masters degree and 10 years previous experience excludes the population of people who can’t wait 3 months for a new career and don’t have equitable access to the educational and experience requirements.*

Ultimately, by carefully evaluating the trade-offs we can support, individuals, organizations and teams have more informed decisions and work towards achieving their goals with greater clarity and purpose.

## Idea 3: Try to unwrap packages

One other technique that has been useful when evaluating trade-offs is to do what I have called unwrapping packages. The idea behind this is to unwrap, unbundle and uncouple to make more honest decisions about trade-offs. In the rest of this section, I’ll focus on particular patterns I have found useful to key in on common “bundlings.”

One pattern is *association*: examining implicit links we draw between separate concepts. During remote work debates, for example, many assumed in-office presence was the only route to team cohesion, overlooking other ways to build strong working relationships. By breaking down implicit associations, we can see that in-person requirements carry their own distinct trade-offs, such as a narrower hiring pool and substantial facility costs.

In this example, we change the discussion from “work from home” vs “connect with new colleagues,” to “work from home and have a more difficult time connecting with new colleagues” vs “go to the office where the friction between meeting new people is lower.” This can support a more nuanced decision, where we can open up dialogue on, for example:

- How to support remote colleagues to form new connections?
- Why does being in the office encourage more connections and if moving around the building is an important factor, how can we offer that same benefit to less mobile colleagues?

In the world of project management, the concept of a “work package” is all about bundling tasks together into work packages or projects themselves. This approach can be useful in certain situations, particularly when it comes to managing large-scale investments. After all, the bigger the package, the greater the economies of scale that can be achieved (investment governance tends to be roughly equal effort regardless of project sizes).

However, there are also cases where this approach might be detrimental. In situations where a team is stable, and tools and solutions are already in place, breaking down tasks into smaller packages can be more effective. This allows for greater flexibility in addressing high-priority items, regardless of where they might fit into a larger package.

<!-- Atlancia embed: Trade-off mentality - bundling vs unbundling work (interactive).
     Fits the post Building a Trade-off Mentality.
     Toggle between bundled and unbundled to see how critical work can jump to the front.
     slop-ok: exclamation marks are logical-not operators in inline script, not prose emphasis. -->
<div class="atlx atlx-trade-bundle">
  <style>
    .atlx-trade-bundle {
      --tb-ink: var(--atl-ink, #EEEDED);
      --tb-text: var(--atl-figure-text, #BFBFBF);
      --tb-dim: var(--atl-dim, #9D9D9D);
      --tb-line: var(--atl-line, #373737);
      --tb-surface: var(--atl-surface, #1e1e1e);
      --tb-blue: var(--atl-info, #5B9ED5);
      --tb-green: var(--atl-success, #54A468);
      --tb-amber: var(--atl-accent, #FFC074);
      --tb-pink: #f43f5e;
      --tb-purple: #a78bfa;
      --tb-gray: #9ca3af;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--tb-surface);
      color: var(--tb-text);
      border: 1px solid var(--tb-line);
      border-radius: 6px;
      padding: 1.3rem 1.3rem 1.1rem;
      margin: 2.5rem 0;
      max-width: 100%;
      font-size: 1rem;
      line-height: 1.55;
    }
    .atlx-trade-bundle * { box-sizing: border-box; }
    .atlx-trade-bundle .atlx-tb-title {
      margin: 0 0 .2rem;
      font-family: "Young Serif", Georgia, serif;
      font-weight: 500;
      font-size: 1.25rem;
      line-height: 1.35;
      color: var(--tb-ink);
    }
    .atlx-trade-bundle .atlx-tb-sub {
      margin: 0 0 .3rem;
      color: var(--tb-dim);
      font-size: .95rem;
    }
    .atlx-trade-bundle .atlx-tb-btns {
      display: flex;
      gap: .5rem;
      flex-wrap: wrap;
      margin: .9rem 0 1rem;
      align-items: center;
    }
    .atlx-trade-bundle .atlx-tb-btns button {
      font: inherit;
      font-size: .88rem;
      font-weight: 600;
      background: transparent;
      color: var(--tb-text);
      border: 1px solid var(--tb-line);
      border-radius: 999px;
      padding: .35rem .8rem;
      cursor: pointer;
    }
    .atlx-trade-bundle .atlx-tb-btns button[aria-pressed="true"] {
      color: var(--tb-ink);
      border-color: var(--tb-dim);
    }
    .atlx-trade-bundle .atlx-tb-btns button:focus-visible {
      outline: 2px solid var(--tb-amber);
      outline-offset: 3px;
    }
    .atlx-trade-bundle .atlx-tb-legend {
      display: flex;
      flex-wrap: wrap;
      gap: .8rem 1.2rem;
      margin-left: auto;
      font-size: .88rem;
      color: var(--tb-dim);
    }
    .atlx-trade-bundle .atlx-tb-legend-item {
      display: flex;
      align-items: center;
      gap: .5rem;
    }
    .atlx-trade-bundle .atlx-tb-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
    }
    .atlx-trade-bundle .atlx-tb-dot.critical { background: var(--tb-pink); }
    .atlx-trade-bundle .atlx-tb-dot.high { background: var(--tb-green); }
    .atlx-trade-bundle .atlx-tb-dot.medium { background: var(--tb-purple); }
    .atlx-trade-bundle .atlx-tb-dot.low { background: var(--tb-gray); }
    .atlx-trade-bundle .atlx-tb-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 0.6rem;
    }
    @media (max-width: 900px) {
      .atlx-trade-bundle .atlx-tb-grid { grid-template-columns: 1fr; }
      .atlx-trade-bundle .atlx-tb-legend { margin-left: 0; width: 100%; }
    }
    .atlx-trade-bundle .atlx-tb-project {
      border: 1px solid var(--tb-line);
      border-radius: 6px;
      overflow: hidden;
    }
    .atlx-trade-bundle .atlx-tb-project.critical-border {
      border-color: var(--tb-pink);
    }
    .atlx-trade-bundle .atlx-tb-project-header {
      display: flex;
      flex-direction: column;
      padding: .6rem .75rem;
      border-bottom: 1px solid var(--tb-line);
      color: var(--tb-ink);
    }
    .atlx-trade-bundle .atlx-tb-project-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
    }
    .atlx-trade-bundle .atlx-tb-project-title {
      font-weight: 600;
      font-size: .92rem;
      color: var(--tb-ink);
    }
    .atlx-trade-bundle .atlx-tb-project-sub {
      font-size: .78rem;
      color: var(--tb-dim);
      font-weight: 500;
      margin-top: .2rem;
      line-height: 1.25;
    }
    .atlx-trade-bundle .atlx-tb-project-body {
      display: grid;
      gap: .35rem;
      padding: .5rem .5rem;
      min-height: auto;
    }
    .atlx-trade-bundle .atlx-tb-item {
      display: flex;
      align-items: center;
      gap: .4rem;
      padding: .4rem .5rem;
      border-radius: 6px;
      font-size: .75rem;
      line-height: 1.25;
      white-space: normal;
      color: var(--tb-ink);
      border: 1px solid var(--tb-line);
      background: rgba(255,255,255,0.01);
      transition: all .25s ease;
    }
    .atlx-trade-bundle .atlx-tb-item svg {
      width: 14px;
      height: 14px;
      flex-shrink: 0;
    }
    .atlx-trade-bundle .atlx-tb-item.critical {
      background: rgba(244,63,94,0.18);
      border-color: rgba(244,63,94,0.9);
    }
    .atlx-trade-bundle .atlx-tb-item.high {
      background: rgba(84,164,104,0.18);
      border-color: rgba(84,164,104,0.9);
    }
    .atlx-trade-bundle .atlx-tb-item.medium {
      background: rgba(167,139,250,0.18);
      border-color: rgba(167,139,250,0.9);
    }
    .atlx-trade-bundle .atlx-tb-item.low {
      background: rgba(156,163,175,0.14);
      border-color: rgba(156,163,175,0.7);
    }
    .atlx-trade-bundle .atlx-tb-item.pulse {
      box-shadow: 0 0 0 0 rgba(251,191,36,0.6);
      animation: tb-pulse 1.6s ease-in-out infinite;
    }
    @keyframes tb-pulse {
      0%, 100% { box-shadow: 0 0 0 0 rgba(251,191,36,0.3); }
      50% { box-shadow: 0 0 0 3px rgba(251,191,36,0); }
    }
    .atlx-trade-bundle .atlx-tb-order.hl {
      border-color: var(--tb-amber);
      box-shadow: 0 0 0 1px var(--tb-amber);
    }
    .atlx-trade-bundle .atlx-tb-callout {
      display: flex;
      gap: .7rem;
      align-items: flex-start;
      margin-top: 1rem;
      padding: .7rem .9rem;
      border: 1px solid var(--tb-line);
      border-radius: 6px;
      background: rgba(255,255,255,0.02);
      color: var(--tb-text);
      font-size: .92rem;
      line-height: 1.5;
    }
    .atlx-trade-bundle .atlx-tb-callout .atlx-tb-order { flex: 0 0 auto; margin-top: .1rem; }
    .atlx-trade-bundle .atlx-tb-order {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 1.8rem;
      height: 1.4rem;
      padding: 0 .4rem;
      border-radius: 999px;
      border: 1px solid var(--tb-line);
      background: rgba(0,0,0,.25);
      font-variant-numeric: tabular-nums;
      font-weight: 600;
      font-size: .78rem;
      flex: 0 0 auto;
      color: var(--tb-ink);
      white-space: nowrap;
    }
    .atlx-trade-bundle .atlx-tb-item-label {
      display: flex;
      align-items: center;
      gap: .4rem;
    }
    .atlx-trade-bundle .atlx-tb-critical-pack {
      display: none;
      margin-top: 1rem;
      border: 1px solid rgba(251,191,36,0.8);
      border-radius: 6px;
      overflow: hidden;
    }
    .atlx-trade-bundle .atlx-tb-critical-pack.visible {
      display: block;
    }
    .atlx-trade-bundle .atlx-tb-critical-pack-header {
      display: flex;
      align-items: center;
      gap: .5rem;
      padding: .7rem 1rem;
      border-bottom: 1px solid rgba(251,191,36,0.6);
      color: var(--tb-ink);
      font-weight: 600;
    }
    .atlx-trade-bundle .atlx-tb-critical-pack-body {
      padding: .8rem;
      display: grid;
      gap: .5rem;
    }
  </style>

  <h3 class="atlx-tb-title">Bundling vs Unbundling Work</h3>
  <p class="atlx-tb-sub">If critical work is bundled with low-priority work, it might wait for the whole package. Breaking it apart lets it jump to the front.</p>

  <noscript><p style="font-size:.9rem;">This figure needs JavaScript. The gist: bundled work forces low priority items in Project 1 ahead of higher value work elsewhere, while unbundling lets the critical item go first.</p></noscript>

  <div class="atlx-tb-btns">
    <button data-action="view" data-view="bundled" aria-pressed="true">Bundled</button>
    <button data-action="view" data-view="unbundled" aria-pressed="false">Unbundled</button>
    <div class="atlx-tb-legend">
      <div class="atlx-tb-legend-item"><span class="atlx-tb-dot critical"></span> Critical</div>
      <div class="atlx-tb-legend-item"><span class="atlx-tb-dot high"></span> High Value</div>
      <div class="atlx-tb-legend-item"><span class="atlx-tb-dot medium"></span> Medium</div>
      <div class="atlx-tb-legend-item"><span class="atlx-tb-dot low"></span> Low Priority</div>
    </div>
  </div>

  <div class="atlx-tb-grid">
    <article class="atlx-tb-project" data-project="1">
      <header class="atlx-tb-project-header">
        <div class="atlx-tb-project-top">
          <span class="atlx-tb-project-title">Project 1</span>
          <span class="atlx-tb-order" data-order></span>
        </div>
        <div class="atlx-tb-project-sub">Critical plus low items</div>
      </header>
      <div class="atlx-tb-project-body">
        <div class="atlx-tb-item critical" data-critical>
          <div class="atlx-tb-item-label">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
              <line x1="12" y1="9" x2="12" y2="13"></line>
              <line x1="12" y1="17" x2="12.01" y2="17"></line>
            </svg>
            Critical Piece of Work
          </div>
        </div>
        <div class="atlx-tb-item low">Low Importance Bug-Fix</div>
        <div class="atlx-tb-item low">Low Importance UI Update</div>
      </div>
    </article>
    <article class="atlx-tb-project" data-project="2">
      <header class="atlx-tb-project-header">
        <div class="atlx-tb-project-top">
          <span class="atlx-tb-project-title">Project 2</span>
          <span class="atlx-tb-order" data-order></span>
        </div>
        <div class="atlx-tb-project-sub">High value</div>
      </header>
      <div class="atlx-tb-project-body">
        <div class="atlx-tb-item high">High Value Enhancement</div>
        <div class="atlx-tb-item high">Long-Term Delivery Improvement</div>
        <div class="atlx-tb-item medium">Medium Value Enhancement</div>
      </div>
    </article>
    <article class="atlx-tb-project" data-project="3">
      <header class="atlx-tb-project-header">
        <div class="atlx-tb-project-top">
          <span class="atlx-tb-project-title">Project 3</span>
          <span class="atlx-tb-order" data-order></span>
        </div>
        <div class="atlx-tb-project-sub">Security fix</div>
      </header>
      <div class="atlx-tb-project-body">
        <div class="atlx-tb-item high">High Value Enhancement</div>
        <div class="atlx-tb-item medium">Medium Value Enhancement</div>
        <div class="atlx-tb-item medium">Medium Risk Security Fix</div>
      </div>
    </article>
  </div>

  <div class="atlx-tb-callout" data-role="callout">
    <span class="atlx-tb-order hl">1st</span>
    <span data-role="callout-text"></span>
  </div>

  <div class="atlx-tb-critical-pack" data-role="critical-pack">
    <header class="atlx-tb-critical-pack-header">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--tb-amber)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="3"></circle>
        <path d="M12 1v6m0 6v6m11-7h-6m-6 0H1"></path>
      </svg>
      <span>Critical work pulled out of Project 1</span>
      <span class="atlx-tb-order" data-order-pack style="margin-left:auto;"></span>
    </header>
    <div class="atlx-tb-critical-pack-body">
      <div class="atlx-tb-item critical pulse">
        <div class="atlx-tb-item-label">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
            <line x1="12" y1="9" x2="12" y2="13"></line>
            <line x1="12" y1="17" x2="12.01" y2="17"></line>
          </svg>
          Critical Piece of Work
        </div>
      </div>
      <p style="margin:.2rem 0 0;color:var(--tb-dim);font-size:.9rem;">Done first, ahead of the rest. High value work in Project 2 and the security fix in Project 3 move up next.</p>
    </div>
  </div>

  <script>
  (function(){
    var root = document.currentScript && document.currentScript.closest ? document.currentScript.closest('.atlx-trade-bundle') : document.querySelector('.atlx-trade-bundle');
    if(!root) return;
    var btns = root.querySelectorAll('[data-action="view"]');
    var critical = root.querySelector('[data-critical]');
    var project1 = root.querySelector('[data-project="1"]');
    var project2 = root.querySelector('[data-project="2"]');
    var project3 = root.querySelector('[data-project="3"]');
    var pack = root.querySelector('[data-role="critical-pack"]');
    var packOrder = root.querySelector('[data-order-pack]');
    var calloutText = root.querySelector('[data-role="callout-text"]');
    var orders = {
      "1": root.querySelector('[data-project="1"] [data-order]'),
      "2": root.querySelector('[data-project="2"] [data-order]'),
      "3": root.querySelector('[data-project="3"] [data-order]')
    };
    function setView(v){
      btns.forEach(function(b){ b.setAttribute('aria-pressed', String(b.getAttribute('data-view') === v)); });
      Object.keys(orders).forEach(function(k){ orders[k].classList.remove('hl'); });
      packOrder.classList.remove('hl');
      if(v === 'bundled'){
        critical.style.display = 'flex';
        project1.classList.remove('critical-border');
        pack.classList.remove('visible');
        orders["1"].textContent = '1st';
        orders["2"].textContent = '2nd';
        orders["3"].textContent = '3rd';
        orders["1"].classList.add('hl');
        calloutText.textContent = 'Project 1 goes first, so its low priority bug fix and UI update get done ahead of high value work in Project 2 and the security fix in Project 3.';
      } else {
        critical.style.display = 'none';
        project1.classList.add('critical-border');
        pack.classList.add('visible');
        packOrder.textContent = '1st';
        orders["2"].textContent = '2nd';
        orders["3"].textContent = '3rd';
        orders["1"].textContent = '4th';
        packOrder.classList.add('hl');
        calloutText.textContent = 'Critical work goes first on its own. High value work in Project 2 and the security fix in Project 3 move up next, and the leftover low items in Project 1 drop to last.';
      }
    }
    btns.forEach(function(b){ b.addEventListener('click', function(){ setView(b.getAttribute('data-view')); }); });
    setView('bundled');
  })();
  </script>
</div>


To illustrate this point, let’s consider an abstract example. Imagine that there are three potential packages of work and one of them contains critical work. There’s no question that this work should take priority over all other work. However, if this critical work is bundled with other non-critical work, the entire package might be completed before other packages containing high-priority work. In this scenario, the lower-priority work ends up taking precedence simply because it was packaged together with the critical work. By breaking work down into smaller, more manageable pieces, teams can avoid this issue and ensure that the most important work always takes priority.

While on the subject of processes, another common pattern is historical linkage; rules and procedures that persist even if they are no longer relevant or useful. For example, some project methodologies require consultation with a vendor or asset management team as a precaution against licensing overages and legal risks. While this may have made sense in the past, with the rise of cloud technology, the need for such consultations is much lower (with software included in the service offering). However, because of the long-standing association between vendor management and licensing, this may be embedded as a required step for going live with delivery even though the previous risk has subsided.

## Idea 4: Who is being served?

Finally, and usually done in concert with the above ideas, is to look at “who is being served” by a choice.

I recall years ago during the transition from an older platform for document management to a newer one, I was part of a group to decide what the folder structure ought to be for projects and support teams. The facilitator in the discussion walked in with the assumption that we needed to have the same structure for everyone. This assumption certainly made sense for their project, once defined it could be copied and pasted for everyone and they could move on. However, in representing teams' needs, the group had very different ideas of what worked best for them.

Seeing an opportunity to ask, I posed a question to the group on where this assumption was made. The conversation went a little something like this:

<em>Facilitator: </em>“We need to standardize folder structure so that when a team member joins from another project they can find documents.”

<em>Me: </em>“How often does it happen?”

<em>Facilitator: </em>“Maybe a couple of times a year”

*Me:* “Are we sure that designing a standard system to serve a twice-a-year event, over allowing the unique needs of teams and projects to be served is the best approach? When I’ve seen new team members join there’s usually been additional guidance provided, a “buddy system” usually, to help them orient themselves on what’s important. Wouldn’t that help serve that need?”

Others seemed to react positively to the idea and the discussion following was more positive. There is no current standard, but there is a “starting” template to get teams off on the right foot. We struck a better balance.

Another example was offered above, requests that may come for status reporting. It’s certainly understandable for leaders to want visibility into work. Yet reporting is never free. When team performance metrics escape the team, psychological safety suffers, especially when an experiment causes a temporary dip in output. Is it worth serving a leader’s need for observability over the potential drawbacks of lower team safety and less available time for work? Perhaps, but raising the discussion and balancing leadership’s need to work with their peers, stakeholders and other leaders allows for more nuance, especially for metrics that may influence team behaviours.

Goodhart's Law famously observes that “when a measure becomes a target, it ceases to be a good measure.” An unfortunate example of this has occurred in hospitals in the UK where a focus on individual mortality rates for surgeons alters their behaviour with [1 in 3 surgeons reported avoiding difficult cases to protect their metrics](https://www.telegraph.co.uk/science/2016/06/03/one-in-three-heart-surgeons-refuse-difficult-operations-to-avoid/). The trade-off we make when metrics escape, doesn’t mean we ought to avoid reporting, but that we should discuss what effects might come from them.

In software, the well-researched [DORA metrics](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance) balance velocity against stability: deployment frequency and lead time measure throughput, while change failure rate and time to restore service measure resilience. When those metrics are used to spot systemic bottlenecks rather than evaluate individuals, teams gain observability without sacrificing psychological safety.

## Wrap-Up

In environments where we are constantly making decisions, it’s easy to overlook the assumptions and trade-offs we make. The idea of a free lunch is a myth; everything we do comes at a cost. A trade-off mentality has helped me have clearer conversations with colleagues and better introspection. By acknowledging the constraints that underlie our systems, I feel better equipped to have constructive, open conversations.

While it’s been helpful for now to adopt a more inquisitive “trade-off mentality,” it’s still a work in progress. Through this lens, I work to support better dialogue. If you are reading this, try it out the next time a statement doesn't quite sit right. Acknowledge that nothing comes for free, and remember that complex work demands open debate. The next time you face an ambiguous decision, challenge yourself and your team to ask: "What's the trade-off here?"

