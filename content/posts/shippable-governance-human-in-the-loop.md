---
title: "Shippable Governance and the Human in the Loop"
date: "2026-10-24T10:45:00-04:00"
lastmod: "2026-10-27T12:00:00-04:00"
slug: "shippable-governance-human-in-the-loop"
url: "/shippable-governance-human-in-the-loop.html"
type: posts
draft: true
authors: ["liam"]
showComments: true
meta_robots: "index, follow"
---

I have spent an inordinate amount of time over the past month experimenting with coding agents, frameworks, and models on my computer. A silly, slightly obsessive amount of time. 

I have spent days building custom tooling, tearing it down, rebuilding it, and rethinking how models connect to local files. I have evaluated subscriptions, tested different reasoning engines, and wired up guardrails, completely absorbed in the mechanics of how we create software.

I have always loved building things, turning an idea in my head into something visible on a screen. Yet I have never felt drawn toward artistic expression for its own sake. My urge to build has always been about making things work better. While I enjoy turning over an interesting concept, it feels far more satisfying when a thought becomes a durable artifact; something I can return to, learn from, and refine over time. 

Even when I revisit essays on this very blog, I rarely admire what I wrote. I immediately catch blind spots: How did I miss that angle? Why was my structure so rigid? Still, I enjoy the discipline of forcing an idea into the world, suffering through the friction, and learning from the outcome.

Working with modern coding agents became addictive because it tapped directly into that cycle. It paired my desire to engineer away friction with rapid, relentless feedback loops. 

You turn an idea in your head into running code within minutes. You watch it fail. You dig into the logs to understand why. You realize you had an obvious blind spot that you could have avoided had you read the documentation, but you were never going to read up until you felt the pain of the error. Once you recognize a dead end, you delete the directory and move on. From initial thought to working prototype to realizing the idea was flawed took thirty minutes. The cost of failure is so low that you finally get to live the old engineering principle of failing fast.

In Site Reliability Engineering, there is a concept I have always loved: treating operations as an engineering problem. SRE calls the repetitive, manual operational tasks that scale linearly with a system toil. How do you engineer away the toil?

What pop culture refers to with slight derogation as vibe coding allowed me to apply that exact engineering mindset to everyday life. My budget for this sort of tinkering has always been irrationally high; the hours I have spent over the years reconfiguring smart home automations far exceed the effort of simply getting off the couch to flip a light switch. 

Yet coding agents unlocked that problem-solving impulse across an entirely new surface. I began targeting the annoying, administrative drag of daily operations: sorting tax documentation, extracting relevant clauses from opaque terms of service, drafting responses to bureaucratic customer service disputes, and parsing arcane government regulations. Having an agent draft a response from verified policy facts, making two quick edits, and sending it frees up real mental space. 

Engineering away the irksome drag of life is a hell of a thing.

Along the way, I made every possible mistake. I watched my laptop bog down completely under runaway background jobs. I blew past five-hour token limits in ninety minutes. I accidentally placed too much trust in data from a model that was cheerfully hallucinating. 

I began to realize that on my single laptop, I was living through a tempest in a teacup version of the exact dilemma every modern enterprise is now facing.

Less than two years ago, I sat on an early pilot user group at the central bank, granted early access to enterprise generative tools. My role was to experiment, communicate with the teams managing security and rollout, and champion practical use cases to skeptical colleagues. That feels like a lifetime ago. The sheer speed of change has collapsed multi-year technology lifecycles into weeks, and that feeling of continuous experimentation and failure is going to remain our reality for a long time to come.

As I worked through those failures, my approach to governing these agents swung wildly like a pendulum.

At first, I tried to micro-manage everything. I configured the environment to demand my explicit confirmation before every tool call, bash execution, or file write. Within two days, I was exhausted. Sitting in front of a laptop clicking "Approve" every twenty seconds turns a professional into a stressed-out clerk. You end up reading nothing, adding massive latency, and doing almost no real work while clinging to the illusion of control.

Frustrated by the bottleneck, I swung the pendulum to the opposite extreme: total delegation. I removed the permission gates, gave the agents broad tool access, and let them run unattended. 

That failed just as quickly. The agents did not achieve effortless execution; they drifted. They filled my terminal with circular debugging loops, burned through API credits, and generated brittle code that collapsed the moment it touched real-world constraints.

Finding the right level of operational control was not an abstract design exercise. It required circulating through those feedback loops, feeling the friction of both extremes, and discovering where safety actually lives. You cannot determine the right balance of autonomy and constraint in an ivory tower; you have to be an active human in the loop, probing the boundaries of the system.

That realization led me straight into the heart of an institutional battle I lived through years ago: the gatekeeper dilemma.

## The Gatekeeper Dilemma

During my tenure modernizing delivery in central banking, I sat across from an enterprise architecture review board that had become an immovable institutional bottleneck.

Teams across the bank spent months building digital systems, only to have their initiatives stalled for weeks waiting for an architecture committee to convene, debate, and render judgment. Project managers were exasperated; business sponsors were furious. When I challenged the committee on their multi-week backlog, the chair explained that their rigorous manual review was the only barrier protecting the bank from catastrophic failure.

I proposed a straightforward alternative: "Tell us the exact criteria you use to evaluate these systems. Write them down as explicit principles and automated checks. We will embed those checks directly into the delivery pipelines so teams can prove compliance before they ever ask for time on your calendar."

The response was immediate, visceral, and revealing.

"Why would we do that?" a senior architect replied. "If we give you the criteria upfront, you will just design the project so that it passes."

I sat in silence for a moment, waiting for him to recognize the irony. He did not. In his mental model, governance was not an engineering standard to be met; it was a personal interrogation. If a delivery team knew the rules in advance and engineered their system to satisfy every one of them, the committee felt cheated of its sovereign prerogative to pass judgment.

That exchange exposed the fundamental dysfunction of traditional gatekeeping. When organizations treat review criteria as proprietary secrets guarded by a designated priesthood, governance ceases to be a mechanism for quality and becomes a mechanism for control. Delivery teams are forced to guess what the committee wants, while gatekeepers preserve their institutional relevance through arbitrary post-hoc inspection.

The tragedy of this dynamic is that it damages both sides. Delivery teams view governance as an adversarial tax to be evaded whenever possible. Meanwhile, the gatekeepers carry an exhausting emotional burden, convinced that the entire organization will collapse unless they personally inspect every line of documentation.

## The Mechanics of Bounded Autonomy

The lesson from my laptop running coding agents is the exact lesson from the central banking boardroom: you cannot govern autonomous actors through manual tollbooths. You govern them by constructing an operational environment of bounded autonomy.

To let an autonomous agent run fast without wrecking the environment, you do not hover over its shoulder. You engineer the platform so that unsafe operations are mechanically impossible.

In our agentic engineering practice, that meant wiring up explicit technical guardrails:

First, we isolated capabilities using the Model Context Protocol (MCP). Instead of giving an agent broad, untracked shell access, we expose domain-specific tools with clear schemas. An agent tasked with querying data can access local SQLite tables, but it holds no permission to modify the schema or delete records without dedicated review paths.

Second, we installed deterministic pre-flight hooks. Before any code is committed or any document is published, automated scripts scan the work. If an agent introduces banned security patterns, unverified credentials, or corporate filler language, the hook fails immediately with a descriptive error. The agent receives immediate feedback from the system, adjusts its output, and tries again without human intervention.

Third, we separated drafting from verification. We established multi-stage review patterns: an agent that drafts a proposal is not allowed to approve it. A separate reviewer agent, loaded with an adversarial prompt, challenges the assertions, checks calculations against raw source dossiers, and flags unearned assumptions.

When these guardrails are in place, the entire dynamic shifts. I no longer sit watching terminal output with white knuckles. I can assign a complex, multi-stage task, step away, and return to find work that has already passed dozens of deterministic quality checks. Autonomy is unlocked because the boundaries are absolute.

## The Vulnerability of Codification

If shifting governance into automated guardrails is so effective, why do so many organizations resist it?

They resist it because codifying evaluation standards into explicit, testable rules is demanding intellectual work that forces professionals into uncomfortable vulnerability.

Much of what an experienced architect, security officer, or compliance lead considers "judgment" is actually tacit pattern recognition accumulated over decades of operational firefighting. Translating that intuition into unambiguous, written requirements forces reviewers to confront their own assumptions. It requires them to separate genuine, non-negotiable architectural constraints from personal aesthetic preferences and historical corporate folklore.

Worse, codification introduces professional vulnerability. As long as standards remain vague and unwritten, a reviewer can never be proven wrong. They can reject an initiative based on an unarticulated sense that something "does not feel enterprise-ready," safe in the knowledge that no one can audit their reasoning. The moment a committee commits its rules to paper, those rules can be debated, measured, and challenged.

Most threatening of all, once review criteria are codified into explicit rules, those rules can be automated.

This is the psychological threshold where traditional oversight clashes with modern engineering. If an automated suite can verify data classification schemas, boundary protections, cryptographic standards, and identity assertions in five seconds, the traditional two-hour review meeting loses its justification. Gatekeepers sense this intuitively. They resist open criteria because they fear that publishing the rulebook renders the referee obsolete.

In an agentic environment, however, hoarding criteria is fatal. Language models and autonomous agents cannot read minds, navigate political subtext, or divine unwritten corporate norms. If you feed an agentic system vague aspirations and expect it to guess what a committee will approve three weeks later, the system will fail every time. High-velocity automation demands radical transparency of constraints. If a standard cannot be written down and verified, it remains an institutional mood without operational standing.

## Shifting from Tollbooths to Guardrails

The only path to scaling autonomous systems safely is to invert the control structure. We must shift governance from post-hoc manual inspection into shippable, executable guardrails.

In traditional software delivery, this pattern is already familiar as shift-left testing. Decades ago, testing was an isolated phase conducted by a separate quality assurance department after developers declared their code complete. Work was tossed over a wall; defects were logged weeks later; schedules slipped indefinitely. Modern engineering resolved that paralysis by bringing automated unit tests, integration suites, and security scans directly into the developer workflow. Quality became an automated property of the build, freeing delivery teams from quarterly committee approvals.

Years earlier in central banking, we experienced the power of this inversion while automating software distribution across thousands of enterprise endpoints. Salaried professionals routinely waited days for managers to sign off on pre-vetted, low-risk developer tools. By proving that pre-cleared software carried zero incremental risk and replacing manual sign-offs with automated fulfillment, we cut delivery times from days to under thirty seconds, saved over a thousand technician hours annually, and suffered zero security breaches.

Agentic systems require an identical inversion, but applied across an operational canvas that encompasses reasoning, language, and tool invocation.

Governance cannot be an event that occurs after an agent finishes generating artifacts. Governance must be the operational scaffold within which the agent operates. This is the core thesis behind emerging frameworks like Gartner AI Trust, Risk, and Security Management (AI TRiSM): model safety and operational integrity cannot rely on static pre-deployment audits. They require continuous runtime validation, dynamic authorization barriers, and deterministic circuit breakers.

When organizations ship governance as code, compliance becomes frictionless. The delivery team does not wonder whether their work will pass the committee; they know it passes because the automated test suite green-lit the build. The adversarial tension between delivery and oversight dissolves. The rules are open, deterministic, and objective.

<!-- embed "governance-latency-simulator" -->

## The Exploratory Validator

When an organization successfully inverts its controls and ships executable guardrails, an immediate question arises: what happens to the human in the loop?

If deterministic suites verify syntax, test execution, schema compliance, and formatting, does the human disappear?

The answer is an emphatic no. The difference is that the human's role undergoes a qualitative transformation. The human stops serving as a manual gatekeeper performing repetitive compliance checks; the human becomes an exploratory validator.

Consider the reality of testing in an agentic development environment. A deterministic test suite can easily prove that a document contains no banned words, that all cross-references resolve to existing files, that mathematical formulas balance, and that visual components compile without syntax errors. Those checks are binary, objective, and fast. An automated system can execute fifty of them in parallel without breaking stride.

Yet an automated suite cannot tell you whether an essay has struck the right emotional register for an anxious board of directors. It cannot tell you that an interactive diagram, while technically valid, conveys an ambiguous metaphor that will confuse non-technical executives. It cannot tell you that an automated script, while perfectly fulfilling its literal prompt, is optimizing for a local metric that damages the broader strategic goal.

In past enterprise platform delivery, we coached external engineering contractors who wrote code at breakneck speed but optimized purely for the happy path. When edge cases broke, non-technical business stakeholders suffered testing fatigue from reviewing the same features multiple times. Autonomous coding agents exhibit that exact pathology. Left to themselves, they generate happy-path solutions with astonishing velocity, quietly shifting the exhaustion of discovering edge cases onto the human user.

Only an active human, engaging with the system's output with genuine curiosity and operational context, catches those anomalies.

This is the true role of the human in an autonomous workflow. The human does not sit between step three and step four rubber-stamping routine calculations. The human interacts with the synthesized work, probes its boundaries, tests its real-world interfaces, and inspects the unexpected seams where codified rules fall short. The exploratory validator tests not only the application, but the guardrails themselves against real-world ambiguity.

When the human discovers an unexpected failure mode, they do not simply patch the immediate symptom and move on. They do the real work of engineering: they extract the lesson and encode it back into the automated test suite.

If an agentic draft repeatedly adopts a patronizing tone when addressing regulatory auditors, the human does not manually rewrite the paragraphs forever. The human writes a new linter check, updates the system prompt constraints, and adds the failure case to the automated evaluation suite. The human's judgment is leveraged: a single exploratory insight permanently improves every future execution of the system.

In this architecture, human involvement is the primary engine of systemic learning. The machine provides flawless execution of codified rules; the human provides the requisite variety necessary to absorb environmental complexity and explore the uncodified frontier.

## Pocket-Ready Rules

Building high-velocity autonomous systems requires abandoning both the myth of the unattended loop and the security blanket of the bureaucratic tollbooth. For leaders navigating this transition, five operational maxims establish the baseline:

**If a rule cannot be written as an automated check, it remains an unverified aspiration.**

**Engineering designs systems to pass defined constraints; withholding the criteria preserves bureaucratic control.**

**Manual inspection of routine automated outputs produces review fatigue and rubber stamps, never safety.**

**The human in the loop functions as an exploratory validator of edge cases, leaving predictable transactions to deterministic code.**

**Every manual intervention that does not result in a new codified guardrail is technical debt paid in human attention.**
