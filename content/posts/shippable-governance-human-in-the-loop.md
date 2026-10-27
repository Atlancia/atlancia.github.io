---
title: "Shippable Governance and the Human in the Loop"
date: "2026-10-24T10:45:00-04:00"
lastmod: "2026-10-27T09:40:00-04:00"
slug: "shippable-governance-human-in-the-loop"
url: "/shippable-governance-human-in-the-loop.html"
type: posts
draft: true
authors: ["liam"]
showComments: true
meta_robots: "index, follow"
---

I have spent an inordinate amount of time over the past year experimenting with coding agents, models, and frameworks on my computer. A slightly absurd amount of time.

I have always loved building things, turning a raw thought into something visible on a screen. Yet I have never felt drawn toward artistic expression for its own sake. My urge to build has always been about making things work better. I want to turn an ephemeral thought into a durable artifact, something I can return to and inspect.

Usually, when I look at something I built yesterday, I do not admire it. I immediately start interrogating my own blind spots: How did I fail to see a cleaner structure? Why was my initial approach so narrow?

That is why working with modern coding agents became addictive in a very specific way. It unlocked rapid, relentless learning loops. You turn an idea over in your head, watch it materialize into code within minutes, and occasionally watch it fall flat on its face. Because you did not spend three days writing boilerplate, you carry zero sunk-cost attachment to the code. You can spend forty-five minutes building an experimental tool, realize it is a dead end, delete the directory, and move on without a second of regret. What you acquired was not the script; it was the clarity that came from testing the assumption against reality.

In Site Reliability Engineering, there is a technical term for repetitive, manual operational tasks that scale linearly with service growth: toil.

What the zeitgeist calls vibe coding let me approach daily life with an SRE mindset. How do we engineer away the toil?

I began applying autonomous agents to the operational friction of everyday life: sorting tax documentation, extracting contract clauses from opaque terms of service, navigating consumer dispute filings, and turning job applications into disciplined, evidence-based packages. Instead of spending an exhausting evening drafting an email to a customer service bureaucracy, an agent drafts the note from verified policy facts, I make two edits, and send it.

Engineering away the irksome, administrative drag of life is a hell of a thing.

Yet the moment you move past personal scripts and attempt to build durable software systems with these tools, the naive dream of effortless automation collides with reality.

Working with an ecosystem of autonomous agents does not feel like operating a compiler, a code generator, or a spreadsheet. It feels strikingly, unmistakably like coaching an engineering delivery team.

You assign an objective, observe the execution, and inspect the resulting output. When something breaks, you step in with diagnostic questions that any seasoned engineering leader would recognize: What was your foundation for that design? What sources did you lean on? Did you verify whether that dependency actually exists, or did you assume it was there because it sounded plausible?

Working across multiple models, reasoning engines, and subagents exposes the reality of cognitive diversity in machines. One model is brilliant at creative architectural synthesis but prone to silent drift if left unmonitored. Another is pedantically literal, executing instructions with surgical precision while missing obvious systemic context. A third model hallucinates libraries with cheerful confidence unless pinned to deterministic schemas. Coaxing consistent, high-integrity outcomes from this ensemble requires constant calibration, coaching, and boundary setting.

The initial temptation for any practitioner discovering these quirks is to micro-manage the system. You configure the software to prompt you for permission before every single tool invocation, file edit, or terminal command.

That instinct is a trap. Sitting in front of a computer screen manually approving dozens of routine function calls reduces a seasoned professional to a stressed-out clerk. You spend your day clicking "Approve" on shell commands you barely have time to read, introducing massive cognitive latency while achieving zero genuine safety. You end up doing almost nothing useful, exhausted by the illusion of control.

If you cannot micro-manage every move, and you cannot let autonomous agents run wild without boundaries, how do you govern them?

The answer is the same answer that great engineering leaders discovered decades ago when scaling human organizations: you stop acting like a manual gatekeeper, and you start shipping the rules as code.

## The Gatekeeper Dilemma

Years ago, while leading delivery modernization initiatives in central banking, I found myself sitting in an enterprise architecture review board that had become an immovable institutional bottleneck.

Teams across the bank spent months building digital capabilities, only to have their initiatives held in limbo for weeks waiting for an architecture committee to convene, debate, and render judgment. Project managers were exasperated; business sponsors were furious. When I challenged the committee on the multi-week backlog, the chair explained that their rigorous manual review was the only barrier standing between the bank and catastrophic systemic failure.

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
