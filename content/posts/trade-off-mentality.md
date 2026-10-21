---
title: "Building a Trade-off Mentality"
date: "2023-05-06T00:00:00-04:00"
lastmod: "2026-09-30T17:06:42-04:00"
slug: "trade-off-mentality"
type: posts
layout: posts/single
media_id: 3
authors: ["liam"]
meta_robots: "index, follow"
featured_image: "media/posts/3/tradeoffpost.jpg"
---
> *If you wish to make an apple pie from scratch, you must first invent the universe.  
> – Carl Sagan*

Carl Sagan’s famous quote inspires deeper thought of how connected our universe is, that to “make an apple pie from scratch” you can keep going one step backwards until one has to “invent the universe.” What struck me was, that somewhere between the start of the universe and baking the pie, we had to draw a line for what we consider “from scratch.” Why would buying pre-made pie crust feel like “cheating,” yet buying pre-ground flour would not? What lines have we drawn without much thought of how we choose them?

Let’s imagine a manager asking someone to take on a new task. Consider the assumptions that may be at play: the manager assumes the employee can do the task, will listen, will understand, and could do the work without sacrificing their current efforts. What trade-offs are involved? What work might suffer to focus on this new task? How would the manager or the employee differ in their views of what could be dropped to accommodate the new work and what might those different opinions tell us about what each of them values?

I’ve found it useful to ask myself what assumptions I’m making when I make a statement. This approach helps me identify what trade-offs and assumed truths may need to be evaluated to see if they’re still true. However, within my head, I can take a far more confrontational approach to my thoughts than I may with others. Thus, I worked on trying out a more inquisitive approach using a mental toolkit that I call the “trade-off mentality” as a way to more collaboratively uncover inbuilt assumptions and have open discussions about the underlying rationale behind our decisions, preferences and assumptions.

While I do believe this is a general toolkit that has helped me think better across multiple domains, the focus in the text below will be largely on software development and teams.

This mental toolkit is based on four core ideas:

- First, there ain’t no such thing as a free lunch — we cannot simply get something without giving something up.
- Second, trade-offs allow us to question what we value.
- Third, trade-offs offer an opportunity for us to discuss ways of splitting or breaking down things we bundle together or associate.
- Finally, when we evaluate decisions and assumptions, we can gain additional insight by asking ourselves who is being served by balancing and weighing valuations.

## Idea 1: There ain’t no such thing as a free lunch

Central to the first idea is the acknowledgement that all endeavours entail a cost and are bound by constraints. That we cannot get a “free lunch.” Choosing to stay up late to watch another episode of Succession, means accepting you might be a little tired tomorrow. We are constrained by time, energy, money, and many other limits.

For instance, we can look at even subtle constraints to a team’s productivity. My favourite to consider is the cognitive load incurred by increasing work complexity (or simply using the idea of mental energy). Such complexity may hinder growth, or necessitate trade-offs in terms of longer learning, more challenging onboarding, or higher rates of incidents. Surfacing impacts from complexity could help identify future challenges and uncover risks we might not be willing to accept.

Indicator statements such as: “We should make time for training,” “I would like you to deliver this as well,” or “The team must assume accountability for this new system” may serve as potential triggers for conversations on underlying assumptions and required trade-offs. The figure below shows a hypothetical model of transition for a team taking on a new application, in which a new idea comes to mind — the “cost” of assuming new accountabilities.

![](state-view.webp)

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

One such pattern is *association*. This pattern involves examining implicit connections we make between ideas. For example, we might assume that working in an office is essential for building strong social connections. While there may be some truth to this, it’s important to recognize that there are other ways to foster social connections. By breaking down these associations we can have more a balanced discussion. In the case of working in an office, the trade-off is not simply between having social connections and staying at home. Instead, it’s about the ease of building connections when we are physically together versus the additional effort required to do so when working remotely.

In this example, we change the discussion from “work from home” vs “connect with new colleagues,” to “work from home and have a more difficult time connecting with new colleagues” vs “go to the office where the friction between meeting new people is lower.” This can support a more nuanced decision, where we can open up dialogue on, for example:

- How to support remote colleagues to form new connections?
- Why does being in the office encourage more connections and if moving around the building is an important factor, how can we offer that same benefit to less mobile colleagues?

In the world of project management, the concept of a “work package” is all about bundling tasks together into work packages or projects themselves. This approach can be useful in certain situations, particularly when it comes to managing large-scale investments. After all, the bigger the package, the greater the economies of scale that can be achieved (investment governance tends to be roughly equal effort regardless of project sizes).

However, there are also cases where this approach might be detrimental. In situations where a team is stable, and tools and solutions are already in place, breaking down tasks into smaller packages can be more effective. This allows for greater flexibility in addressing high-priority items, regardless of where they might fit into a larger package.

![](selected-view.webp)

To illustrate this point, let’s consider an abstract example. Imagine that there are three potential packages of work and one of them contains critical work. There’s no question that this work should take priority over all other work. However, if this critical work is bundled with other non-critical work, the entire package might be completed before other packages containing high-priority work. In this scenario, the lower-priority work ends up taking precedence simply because it was packaged together with the critical work. By breaking work down into smaller, more manageable pieces, teams can avoid this issue and ensure that the most important work always takes priority.

While on the subject of processes, another common pattern is historical linkage; rules and procedures that persist even if they are no longer relevant or useful. For example, some project methodologies require consultation with a vendor or asset management team as a precaution against licensing overages and legal risks. While this may have made sense in the past, with the rise of cloud technology, the need for such consultations is much lower (with software included in the service offering). However, because of the long-standing association between vendor management and licensing, this may be embedded as a required step for going live with delivery even though the previous risk has subsided.

## Idea 4: Who is being served?

Finally, and usually done in concert with the above ideas, is to look at “who is being served” by a choice.

I recall years ago during the transition from an older platform for document management to a newer one, I was part of a group to decide what the folder structure ought to be for projects and support teams. The facilitator in the discussion walked in with the assumption that we needed to have the same structure for everyone. This assumption certainly made sense for their project, once defined it could be copied and pasted for everyone and they could move on. However, in representing teams’ needs the group had very different ideas of what worked best for them.

Seeing an opportunity to ask, I posed a question to the group on where this assumption was made. The conversation went a little something like this:

<em>Facilitator: </em>“We need to standardize folder structure so that when a team member joins from another project they can find documents.”

<em>Me: </em>“How often does it happen?”

<em>Facilitator: </em>“Maybe a couple of times a year”

*Me:* “Are we sure that designing a standard system to serve a twice-a-year event, over allowing the unique needs of teams and projects to be served is the best approach? When I’ve seen new team members join there’s usually been additional guidance provided, a “buddy system” usually, to help them orient themselves on what’s important. Wouldn’t that help serve that need?”

Others seemed to react positively to the idea and the discussion following was more positive. There is no current standard, but there is a “starting” template to get teams off on the right foot. We struck a better balance.

Another example was offered above, requests that may come for status reporting. It’s certainly understandable for leaders to want visibility into work. Yet, accepting that reporting doesn’t come for free and that when data on team performance “escapes” the team it costs the team safety to make changes — especially when an experiment might cause a temporary slowdown. Is it worth serving a leader’s need for observability over the potential drawbacks of lower team safety and less available time for work? Perhaps, but raising the discussion and balancing leadership’s need to work with their peers, stakeholders and other leaders allows for more nuance, especially for metrics that may influence team behaviours.

The classic adage of [Goodheart’s Law](https://en.wikipedia.org/wiki/Goodhart%27s_law): would state that “when a measure becomes a target, it ceases to be a good measure.” An unfortunate example of this has occurred in hospitals in the UK where a focus on individual mortality rates for surgeons alters their behaviour with [1 in 3 surgeons reported avoiding difficult cases to protect their metrics](https://www.telegraph.co.uk/science/2016/06/03/one-in-three-heart-surgeons-refuse-difficult-operations-to-avoid/). The trade-off we make when metrics escape, doesn’t mean we ought to avoid reporting, but that we should discuss what effects might come from them.

For those in software, there are well-established metrics available, colloquially called the[DORA metrics](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance), with years of research behind them. These metrics are described by Google as:

*Deployment Frequency — How often an organization successfully releases to production*

*Lead Time for Changes — The amount of time it takes a commit to get into production*

*Change Failure Rate — The percentage of deployments causing a failure in production*

*Time to Restore Service — How long it takes an organization to recover from a failure in production*

## Wrap-Up

In environments where we are constantly making decisions, it’s easy to overlook the assumptions and trade-offs we make. The idea of a free lunch is a myth; everything we do comes at a cost. A trade-off mentality, informed by the four ideas above, has helped me have better conversations with others and better introspection. By acknowledging the constraints that underlie our systems, I feel better equipped to have constructive, open conversations.

While it’s been helpful for now to adopt a more inquisitive “trade-off mentality,” it’s still a work in progress. Through this lens, I work to support better dialogue. If you’re reading this, try it out the next time you are confronted with a difficult decision or hear a statement that “doesn’t sit right.” Remember to acknowledge that nothing comes for free and when we work in complex environments, we work best when we openly discuss our ideas and concerns. When you are brought into these discussions, challenge yourself to question “What’s the trade-off here?”
