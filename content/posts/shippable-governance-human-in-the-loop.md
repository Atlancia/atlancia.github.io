---
title: "Shippable Governance and the Human in the Loop"
description: "Building governance through debate, feedback loops, and humans guiding AI agents."
date: "2026-10-24T10:45:00-04:00"
lastmod: "2026-11-10T19:05:00-05:00"
slug: "shippable-governance-human-in-the-loop"
url: "/shippable-governance-human-in-the-loop.html"
type: posts
draft: false
authors: ["liam"]
showComments: true
meta_robots: "index, follow"
media_id: 7
featureimage: "media/posts/7/shippable-cover-rest.webp"
coverMotion: "shippable-cover"
coverMotionBase: 0.8
---

> "I may be wrong and you may be right, and by an effort, we may get nearer to the truth."  
> Karl Popper, *The Open Society and Its Enemies* (1945)

I recently put out a small post reflecting on the environments where I feel best suited to drive change and build value. Since putting that out, one idea has been circling in my head: the contrast between rooms where "right" is determined by debate, and rooms where "right" is determined by hierarchy.

Of course, hierarchy has its place. Leadership is a skill like any other, and ultimately accountability cannot be outsourced. Depending on the size of an organization, there may simply be an insurmountable distance between decision-makers and the people doing the work. Structure is how large institutions coordinate action. Still, no position can manufacture truth.

No institution exemplifies that scale and hierarchy quite like government. Years ago, while reading Jürgen Habermas's work on deliberative democracy, I found myself wishing his concepts were more frequently applied to business and technology. Habermas argued that sound collective decisions require more than administrative decrees or raw voting tallies. They require an environment where rank and power are bracketed at the door, leaving authority to what he called "the unforced force of the better argument."

When hierarchy suppresses debate, it creates epistemic blindness. That blindness is not unique to governments. It thrives in boardrooms that lose touch with operational reality, in review committees that hoard evaluation criteria, and in engineering teams that layer technical debt onto technical debt because nobody feels empowered to challenge a delivery schedule.

Every decision eventually hits a surface where it makes contact with reality. For a business, that surface is the market; for a government, it is the voters; for a software team, it is the production runtime. If an organization uses rank to avoid internal debate, it misses the truth, and reality will eventually find it. It is always better to bring that reality toward you as early as possible, learning while the costs are lowest.

Over the past few months, I have immersed myself in using AI agents and developer tooling on my laptop. While countless articles debate the grand promises and perils of artificial intelligence, I have simply enjoyed the fun of making things: using little more than words and the right loops, tests, and guardrails, each discovered through trial and error.

In this environment, there could be no flatter hierarchy. It is simply me working alongside autonomous coding agents and reasoning models doing their best to fulfill an instruction. 

When things fail in that setup, I am left with one of the oldest jokes in IT support: a PEBKAC error. Problem Exists Between Keyboard And Chair. The gap between what is in my mind and the result on the screen lies only in my ability to articulate intent, structure constraints, and design feedback loops. When the output misses the mark, I have nothing to blame besides my own clarity: communicating what good looks like, and specifying what failure looks like.

Through this, I have found the unexpected delight of discovering that I am wrong. Frequently.

Not to say that I enjoy being wrong. I love being right. I work hard to stay informed so that I can stay right. Still, moments of being wrong are inevitable stops on the way to insight. There is no better place to be wrong than where the cost is lowest and the learning is highest.

In this wild west of modern AI, where tooling, models, and conventions shift daily, my misconceptions are handed back to me every few minutes. The tax on being wrong is mercifully low.

## The Giving of Orders and the Receiving of Results

What once took months of toil to learn (and could easily be rendered obsolete by a new version, or abandoned after realizing it was too complicated to maintain) now takes thirty minutes. I can write a clear spec, reuse or write a few tests, and see quickly whether an idea holds water. A technique like test-driven development becomes a vehicle for shipping human intent to a machine.

This year offers a fitting historical marker: 2026 is the centenary of Mary Parker Follett’s 1926 lecture The Giving of Orders. It was a rare, early critique of command-and-control management, arguing that productive work should not derive from "power-over," but from "power-with," grounded in the objective facts of the work itself.

When working with coding agents, "power-over" is not even an option. They are not people. I can yell and type in all caps, but they have no feelings to injure and no mouths to feed at home that I could threaten by docking pay. Coercion does not work on software that already does its best to fulfill a prompt. To fix a broken result, I have to default to a "power-with" model: aligning on objective facts, understanding how the model parses instructions, and steering the work toward truth.

This dynamic creates an exceptional opportunity to practice leadership communication. When a leader gives vague directions to a team ("Fix that login screen"), the instinct is to blame the subordinate. It is easy to assume the team simply failed to understand, especially when results arrive long after an edict and the leader has forgotten their own words.

With a coding agent, you scroll up three inches on your screen and the prompt is staring back at you. There is nothing left to see but your own lack of clarity. The failure is clear and the result immediate. If you want something fixed, you have to define what that actually means. You quickly learn how much room for miscommunication hides in a requirement as seemingly basic as "the login page takes too long to load."

{{< embed "telephone-fix-login" >}}

## The Gatekeeper Dilemma

When I first started using coding agents, I reacted like any cautious practitioner: I tried to control everything. I configured my environment to require explicit approval before every tool call, terminal command, and file edit.

Within days, I was exhausted. Requests came in such a relentless torrent that I was simply a gatekeeper, clicking through without reading, keeping an illusion of control with zero real safety. I was just clicking, knowing the next prompt was already queuing up the moment I hit Approve.

{{}}

Yet, I have to admit to myself: I never would have gotten comfortable granting autonomy had I not lived through that friction. Feeling that drag firsthand forced me to think of smarter ways to govern the system. I could never have found the right balance of autonomy and constraint in the abstract; I had to experience the friction directly.

While earlier I said I enjoyed being wrong, this was a far less enjoyable realization. Being wrong here was not like discovering a flaw in a guardrail or a test that became a logical puzzle to fix. This was different. This was realizing that a frustration I had carried for years from enterprise delivery was built on my own incomplete understanding. I was wrong about the role of gatekeepers.

Review boards seem to have an innate tendency to multiply: architecture review, security audits, service design gates, third-party risk assessments, and financial compliance standards. An endless parade of committees creeps up between the people doing the work and the production environment where users can actually benefit from it. Projects stall for weeks while arcane rules and deliberations line up for a rubber stamp.

During one memorable initiative, we sat down with a review committee whose evaluations were notoriously manual and subjective. I asked a straightforward question: "Could you give us the criteria before we build, so we can embed them into our automated tests and verify them as we develop?"

The response was quick, and carried a tone that what they were about to say should have been obvious:

"We won't know until we see it," a reviewer told me. "Besides, if we give you the criteria upfront, you will just design the system to pass."

I sat in silence, waiting for him to realize that designing to pass was supposed to be the entire point of engineering. He did not.

In the moment, it was easy to dismiss his reaction with cynicism. But sitting at my laptop years later, clicking "Approve" every twenty seconds on an AI agent, I felt an unexpected empathy for that reviewer. He felt a genuine sense of duty to protect the institution from catastrophic failure. He also understood something subtle: if governance is reduced entirely to a static checklist, delivery teams will optimize for the test while missing unpredictable edge cases. Worse, nobody in the loop next time will understand the context behind them.

We were both a little right and a little wrong in that room. My mistake was dismissing the committee as a mere rubber stamp, missing that they were the carriers of hard-won institutional context. His mistake was assuming that writing down the rules was a one-time, irreversible act.

When I asked him for his criteria upfront, I was not asking him to carve stone tablets and walk away forever. I was asking him to *ship his governance*. I wanted him to package up the majority of checks he was looking for into a product our team could actually consume, test against, and reflect back to him. To him, governance was a static monument. He had not yet seen it as a living product.

Like any other product, once you ship version 1.0 of your guardrails into the real world, you get to see where teams work around it, where edge cases slip through, and where the rules need to evolve. Shipping the rules does not end the conversation; it gives you an objective baseline to learn from.

## Shippable Governance

Looking back at that committee room, I will never know whether it was obstinance or wisdom that drove that interaction. Regardless, in an environment where governance is centralized, it is hard to imagine rules as something that could be shaped or evolved. While I recognize I asked that reviewer to take a few steps toward those of us trying to build, I did not offer much in the way of a step toward him. My goal back then was simply to get past the gatekeeper, without appreciating the value of the gate.

Still, that underlying instinct holds up: review boards would be far better off if they could step out of the way of clicking every approval and start shipping their expectations.

In software delivery, the concept of Governance as Code has been established for a while. The core philosophy is straightforward: if a rule can be expressed in code, it should benefit from the modern disciplines of software engineering. From specifications to automated tests to deployment pipelines, software delivery has become remarkably effective at evolutionary change. It is equally effective at dealing with defects. When a policy misses something or creates unnecessary drag, you do not wait six months for an annual committee review. You patch it, bump the version to 1.1, see what fails, and improve.

That was the mentality I had to adopt with modern AI tooling. Sitting and clicking Approve was a necessary stage of learning, but I could not imagine a career of that. I could neither choose "allow all" nor stay trapped clicking "approve" on every tool call. I had to balance velocity and safety, and once I established basic safety, I needed the results to actually be good.

{{< embed "pendulum-v6-evenings" >}}

I needed to find a way to describe what I wanted without starting from scratch every single time. I needed blueprints that defined what a good output looked like, even as the specific content shifted: establishing the shape, the register, and the constraints upfront. Whether that was an orthodox approach or not, it worked. It worked far better than re-explaining the rules with every prompt.

As those automated loops took shape, I stopped treating every interaction as a single generic approval. I began to typify them, learning which tool fit which job. Deterministic checks belong in local code, linters, and automated tests. Contextual judgment is where human intelligence and reasoning models actually add value.

It was reassuring to discover that this intuition lines up with what industry analysts at firms like Gartner are advising: AI governance policies establish expectations, but they cannot enforce behavior during live execution. Real safety requires proportional control: automating baseline checks in code so humans have the time and cognitive capacity to govern the uncodified frontier.

While I said earlier that I value being wrong as an opportunity to learn, I have to admit: it is deeply satisfying to do the reading afterwards and discover that you were right.

This brings us back to the reviewer's instinct. When he said, "We won't know until we see it," he was right in a way he may not have intended. We will not know the risks until we see them, but we will not know the benefits until we see them either. Both the risks we fear and the value we have yet to discover only reveal themselves on contact with reality.

I saw that value firsthand during an early enterprise AI pilot. A colleague sat with a tangled draft of her thoughts, fighting the friction of translating across multiple languages into English. When the model returned a structured, clear revision, she stared at the screen, read the text, and turned to me:

"That is what I sound like in my head," she said, "but I could never write like that."

That moment stayed with me. No procurement checklist, ROI calculator, or business case would have predicted that quiet realization of someone finally expressing their intelligence the way they wanted to. It was an insight that could only be discovered by participating in the work.

## Getting Nearer to the Truth

We cannot govern autonomous systems from the shoreline. Governance cannot be practiced from the outside looking in, and it is never finished on the first pass. It has to move toward the middle, shifting into a product to create the space required to learn and remain in the loop. You cannot reap the benefits unless you participate, because the most meaningful value reveals itself in ways no static policy could predict.

Depending on the sensitivity and risk of what I am building, shipping governance looks different. Sometimes a guardrail is an honor contract: a markdown rule or system prompt held up by the model's statistical willingness to behave. Other times, when the stakes are higher, an honor contract is reckless, and I have to ship a hard, deterministic test suite, pre-commit hooks, or sandboxed tool permissions so a model physically cannot touch protected infrastructure without review.

We rarely know where that line sits until we are already in the work. You have to do both at once: live in the loop and ship the guardrails, then come back, catch the drift, and make maintenance a regular operational habit.

In autonomous systems, intellectual humility is an operational requirement. What seems complete today will look naive in six months as models evolve and discover creative new ways to misunderstand constraints. Staying in the loop is the active discipline of catching where you were wrong yesterday and encoding that lesson into tomorrow's build.

We cannot govern what we refuse to touch. We must step into the loop, feel the friction of what breaks, turn what is predictable into automated guardrails, and reserve human wisdom for the uncodified edges where judgment actually matters.

I may be wrong, and the machine may be right, or more likely, we are both a little wrong. Only by stepping into the loop do we have any shot at getting nearer to the truth.
