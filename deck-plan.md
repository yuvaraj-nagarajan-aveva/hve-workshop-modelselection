# Deck plan — Model selection and best practices

**Amended at presenter direction.** This revision combines Cost and healthy-use
guidance into one slide, and adds a dedicated default-tier pricing reference.
The segment now has an internal title slide, six content slides, and the
standard closing slide. Every slide includes presenter notes and is rebuilt into
the output PowerPoint. Output folder: the `HVE Model Selection` workbench folder
itself (no nested `presentations/` folder), alongside the source notes and the
workshop deck this segment slots into.

## 1. The decisions

* **Audience and template — Internal.** This is HVE champion and employee
  training that slots into `2026 Q3 HVE Hands-on Workshop.pptx`, which is itself
  built on the internal template and carries the internal classification footer.
* **The slot and the ask.** Roughly 15 minutes inside the workshop. The room
  should understand the available models and their relative cost, default to
  Auto, and choose a larger or smaller model only when the task earns it.
* **Archetype.** Training segment — open with a short title slide, teach the
  decision, then give the practice rules. These six content slides are an insert
  into an existing workshop deck.
* **Surface theme — White.** Matches the existing workshop deck exactly.
* **Motif — icon in a coloured circle**, beside every card heading, every step
  and the takeaway band.
* **Accent order — leading with green**, then cyan, amber, blue, coral, magenta.
  Sustainability is half of what this segment says, and green earns the open.
* **Composition variety.** Six different shapes across the content slides: a
  formatted model table, a three-column card grid, a routing flow, a cost and
  value comparison, a formatted rate table, and a numbered rail. No two
  adjacent slides share a shape.

## 2. The slide table

| # | Layout | Shape | What the audience sees | What it says |
| --- | -------- | ------- | ------------------------ | -------------- |
| 1 | Title Slide | Internal dark title slide | Matches the opening slide of `copilot-agents-and-skills.pptx`: date, accent rule, large title, subtitle, owner line, and AVEVA wordmark on the internal dark surface. Title: "AI Model Selection"; subtitle: "Quality, cost and sustainability in practice"; owner: "Engineering Enablement"; date: "September 2026". | Choose the right model for the work and use AI credits deliberately |
| 2 | Title, Subtitle and Content | Formatted model table | A compact, scannable table of every model in `model-chart.md`, with Model, relative reasoning/agentic effort, and overall cost columns. The header is branded, rows are visibly aligned, and a takeaway band says that the lowest-cost model that clears the task's quality and risk threshold is the starting point. | Know the choices before choosing manually |
| 3 | Three Content | Three-column card grid over a takeaway band | Three cards across the slide — Advanced reasoning, Standard flagship, Fast and lightweight — each with an icon in a coloured circle, a line on when to choose it and a line on what it costs, with a quiet "rule of thumb" band across the foot. | Models come in three tiers and each has a job |
| 4 | Two Content | Routing flow, 60/40 split | Left: a simple two-signal route showing system health and task intent feeding Auto model selection. Right: three benefit cards for reliability, task fit, and token efficiency, followed by a small 10% discount callout for paid users. A footer notes that routing usually happens at conversation start or after context compaction to preserve cache. | Copilot Auto Model Selection chooses a reliable best-fit model and lowers cost |
| 5 | Two Content | Cost and value comparison | Subtitle: "Value-focused use." Left: a billing split distinguishing seat-included inline assistance from AI-credit-consuming Chat, CLI, agents, Spaces, and code review. Right: "Not less AI. Better value." with healthy high-use signals and warning signs of inefficient workflow. | Cost is driven by model choice and token use; judge its value and outcome, not the raw volume |
| 6 | Title, Subtitle and Content | Formatted default-tier rate table | A complete formatted table mirroring the Default-tier rates in `model-costs.md`: Model, Input, Cached input, Cache write, and Output. A note establishes that all rates are USD per 1 million tokens; a takeaway records the 10% Auto discount on AI-credit cost. | Compare model rates without mistaking token prices for fixed request prices |
| 7 | Title, Subtitle and Content | Numbered rail with a takeaway band | Four oversized numerals with a coloured rule under each — right-size the model, prefer local for simple tasks where policy permits, reserve reasoning models, batch related changes — and a takeaway with the AI Energy Score leaderboard link. | Four habits reduce cost and energy without reducing quality |
| 8 | End - Dark | Closing | The standard AVEVA closing slide, unmodified | - |

## 3. Speaker notes

| Slide | Speaker notes |
| --- | --- |
| 1 | Introduce this segment as a practical guide to choosing the right model for the work. The aim is not to minimise AI use; it is to produce valuable engineering outcomes with deliberate, proportionate use of AI credits. |
| 2 | Introduce manual selection as an exception, not the starting point. These are relative workshop ratings: effort is derived from agentic quality in the model chart, and cost is relative. Ask participants to start with the lowest-cost model that can safely meet the task and risk threshold. |
| 3 | Give a short example for each tier. Use advanced reasoning only when the work genuinely needs deep analysis, a broad design, or a difficult debugging step. The daily-driver tier handles most normal work; lightweight models keep routine tasks quick and economical. |
| 4 | Explain that Auto combines live service health with the prompt's task needs. It usually chooses at conversation start or after context compaction to preserve cache. Emphasise the 10% paid-user discount, but frame Auto's main benefit as reliable, appropriate routing rather than discount hunting. |
| 5 | Separate included inline assistance from credit-consuming, reasoning-heavy work. Cost awareness means deliberate use that improves cycle time, quality, reduced toil, or release confidence; investigate loops, discarded diffs, and routine premium-model use. |
| 6 | These are token rates per 1 million tokens, not fixed request prices. Cache writes apply to Anthropic and GPT-5.6 models; some models have higher long-context rates. Auto's 10% AI-credit discount applies to models selected through Auto. Direct the audience to the linked source for current pricing. |
| 7 | Close with four habits participants can apply today. State that local models are only appropriate where policy permits. Do not provide unverified energy numbers; point to the AI Energy Score leaderboard for transparent published information. |
| 8 | Thank the audience and invite questions or transition to the next workshop section. |

## 4. Gaps and assumptions

* **Slide 1 — reasoning effort.** `model-chart.md` supplies cost and agentic
  quality, but does not contain an explicit model reasoning-effort rating. The
  visual must label this as relative reasoning/agentic effort and derive it from
  the existing agentic-quality rating, or use presenter-approved ratings. Do not
  represent this as vendor-published reasoning effort.
* **Slide 1 — readability.** Twelve model names must remain readable at normal
  presentation distance. The build should use grouped rows and badges, rather
  than trying to reproduce every column from `model-chart.md`.
* **Slide 3 — Auto claims.** The routing, cache-preservation, reliability, and
  paid-user 10% discount statements are sourced from
  `about-copilot-auto-model-selection.md`. Recheck the linked GitHub reference
  before publishing because product behaviour can change.
* **Slide 5 — pricing.** `model-costs.md` reports token rates, not a fixed
  per-request cost. The slide must retain the per-million-token unit and source,
  use only enough rows to remain readable, and direct the audience to the file
  or linked GitHub pricing page for the full table.
* **Slide 6 — local and edge models.** The source notes name Llama 3 and Phi-4
  via Ollama. Whether local models are sanctioned for AVEVA work was not
  confirmed, so the step is written as the general principle and names no
  specific runtime.
* **Slide 6 — energy figures.** No energy-per-token numbers were supplied and
  none are invented. The Hugging Face AI Energy Score leaderboard is cited as a
  live link instead, which the internal audience makes both allowed and required.
* **Assumed** this is a standalone insert the presenter merges into the workshop
  deck, rather than an edit of the workshop file itself. The workshop file is not
  touched.

## 5. Amendments after the build

* **Previous slide 1** gained a "rule of thumb" takeaway band across the foot. Without it
  the card row left a dead band across the lower third of the slide.
* **Previous slide 2** was planned with two override cards, briefly built with three, and
  returned to two: the narrow column cannot carry three cards at a readable size.
* **Previous slide 2 layout** moved from `Title, Subtitle and Content` to `Two Content`.
  The single content region of the planned layout cannot carry a 60/40 split with
  a gradient panel on one side and stacked cards on the other; `Two Content`
  gives the two regions the composition needs.
* **Superseded composition note.** The previous build had no chart or image
  because no figures or photography were supplied. This amendment adds a model
  matrix and a simplified pricing table from the newly supplied sources; the
  completed rebuild must be visually reviewed for density and legibility.
