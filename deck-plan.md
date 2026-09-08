# Deck plan — Model selection and best practices

Approved by the presenter. Output folder: the `HVE Model Selection` workbench
folder itself (no nested `presentations/` folder), alongside the source notes and
the workshop deck this segment slots into.

## 1. The decisions

* **Audience and template — Internal.** This is HVE champion and employee
  training that slots into `2026 Q3 HVE Hands-on Workshop.pptx`, which is itself
  built on the internal template and carries the internal classification footer.
* **The slot and the ask.** Roughly 10 minutes inside the workshop. The room
  should leave defaulting to Auto, and stepping up or down only when the task
  earns it.
* **Archetype.** Training segment — teach the decision, then give the practice
  rules. Departs from the full archetype in that there is no title or section
  slide: these three slides are an insert into an existing workshop deck.
* **Surface theme — White.** Matches the existing workshop deck exactly.
* **Motif — icon in a coloured circle**, beside every card heading, every step
  and the takeaway band.
* **Accent order — leading with green**, then cyan, amber, blue, coral, magenta.
  Sustainability is half of what this segment says, and green earns the open.
* **Composition variety.** Three different shapes across three content slides:
  a three-column card grid, an asymmetric 60/40 split, then a numbered rail with
  a takeaway band. No two adjacent slides share a shape.

## 2. The slide table

| # | Layout | Shape | What the audience sees | What it says |
| --- | -------- | ------- | ------------------------ | -------------- |
| 1 | Three Content | Three-column card grid over a takeaway band | Three cards across the slide — Advanced reasoning, Standard flagship, Fast and lightweight — each with an icon in a coloured circle, a line on when to choose it and a line on what it costs, with a quiet "rule of thumb" band across the foot | Models come in three tiers and each has a job |
| 2 | Two Content | Asymmetric split, 60/40 | Left, on a soft gradient panel: three short paragraphs saying Auto is the default, that it routes easy prompts to cheap models while saving the flagship for hard ones, and that this is the sustainable default too. Right: two stacked cards, "Override up" and "Override down", each with an icon circle and its trigger | Start on Auto; override deliberately, not by habit |
| 3 | Title, Subtitle and Content | Numbered rail with a takeaway band | Four oversized numerals with a coloured rule under each — right-size the model, prefer local for simple tasks, keep reasoning models off routine work, batch related changes — and a takeaway across the foot | Four habits that cut cost and energy without costing quality |
| 4 | End - Dark | Closing | The standard AVEVA closing slide, unmodified | - |

## 3. Gaps and assumptions

* **Slide 1 — model names.** The source notes name tiers, not products, and no
  AVEVA-approved model list was supplied. The cards stay tier-level. The
  presenter should name the current models for each tier out loud, or supply the
  approved list for a rebuild.
* **Slide 2 — the workshop slot.** Ten minutes is assumed; it is not printed on
  any slide, so a different slot costs nothing.
* **Slide 3 — local and edge models.** The source notes name Llama 3 and Phi-4
  via Ollama. Whether local models are sanctioned for AVEVA work was not
  confirmed, so the step is written as the general principle and names no
  specific runtime.
* **Slide 3 — energy figures.** No energy-per-token numbers were supplied and
  none are invented. The Hugging Face AI Energy Score leaderboard is cited as a
  live link instead, which the internal audience makes both allowed and required.
* **Assumed** this is a standalone insert the presenter merges into the workshop
  deck, rather than an edit of the workshop file itself. The workshop file is not
  touched.

## 4. Amendments after the build

* **Slide 1** gained a "rule of thumb" takeaway band across the foot. Without it
  the card row left a dead band across the lower third of the slide.
* **Slide 2** was planned with two override cards, briefly built with three, and
  returned to two: the narrow column cannot carry three cards at a readable size.
* **Slide 2 layout** moved from `Title, Subtitle and Content` to `Two Content`.
  The single content region of the planned layout cannot carry a 60/40 split with
  a gradient panel on one side and stacked cards on the other; `Two Content`
  gives the two regions the composition needs.
* **No chart or image.** The source notes supplied no numbers and no photography,
  and none were invented, so `Test-AvevaDeck.ps1` raises its `NoChartOrImage`
  warning. Every slide still carries a visual element and the deck uses four
  accents. If real figures become available — cost or energy per tier, or the
  share of prompts Auto routes to small models — slide 1 or slide 3 would carry a
  chart well.
