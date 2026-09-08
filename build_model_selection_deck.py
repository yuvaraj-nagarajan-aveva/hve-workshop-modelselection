"""Build the model selection guidance segment for the HVE Hands-on Workshop."""

import sys

SKILL = (
    r"c:\Users\yuvaraj.nagarajan\.vscode\agent-plugins\github.com"
    r"\AVEVA-Copilot-Access\aveva-agent-plugins\plugins\aveva-author"
    r"\skills\aveva-pptx\scripts"
)
sys.path.insert(0, SKILL)

import aveva_deck as deck  # noqa: E402

DECK = "Model-Selection-Guidance.pptx"
ENERGY_SCORE = "https://huggingface.co/spaces/AIEnergyScore/Leaderboard"


def formatted_table(slide, region, headers, rows, column_widths, font_size=10):
    """Draw a compact, branded table in a safe slide region."""
    header_height = 0.34
    row_height = (region[3] - header_height) / len(rows)
    x_positions = [region[0]]
    for column_width in column_widths[:-1]:
        x_positions.append(x_positions[-1] + column_width)

    for index, (header, x, width) in enumerate(zip(headers, x_positions, column_widths)):
        deck.rectangle(slide, (x, region[1], width, header_height), fill=deck.DEEP_PURPLE)
        deck.text(slide, (x + 0.08, region[1] + 0.03, width - 0.16, header_height - 0.06),
                  header, size=font_size, colour=deck.WHITE, bold=True)

    for row_index, row in enumerate(rows):
        y = region[1] + header_height + row_index * row_height
        fill = deck.SURFACE if row_index % 2 == 0 else deck.WHITE
        for column_index, (value, x, width) in enumerate(zip(row, x_positions, column_widths)):
            deck.rectangle(slide, (x, y, width, row_height), fill=fill)
            deck.text(slide, (x + 0.08, y + 0.02, width - 0.16, row_height - 0.04),
                      value, size=font_size, bold=column_index == 0)


presentation = deck.open_deck(DECK)
deck.accent_order(deck.GREEN)

# --- 1. Title --------------------------------------------------------------
slide = deck.add_slide(presentation, "Title Slide")
deck.set_fields(
    slide,
    date="September 2026",
    title="AI Model Selection",
    subtitle="Quality, cost and sustainability in practice",
    presenter="Engineering Enablement",
)
deck.notes(
    slide,
    "Introduce this segment as a practical guide to choosing the right model for "
    "the work. The aim is not to minimise AI use; it is to produce valuable "
    "engineering outcomes with deliberate, proportionate use of AI credits.",
)

# --- 2. Model landscape ----------------------------------------------------
slide = deck.add_slide(presentation, "Title, Subtitle and Content")
deck.set_fields(
    slide,
    title="The Copilot model landscape",
    subtitle="Relative reasoning and agentic effort beside overall cost",
)
region = deck.claim(slide, "content")
deck.ambient_wash(slide, corner="top-right")
cards, foot = deck.split_region_vertical(region, 0.73)
models = [
    ("GPT-5.6 Luna", "High", "Low"),
    ("GPT-5.6 Terra", "Very high", "Medium"),
    ("GPT-5.6 Sol", "Very high", "High"),
    ("Claude Sonnet 5", "High", "Medium"),
    ("Claude Opus 5", "Very high", "High"),
    ("Claude Opus 4.8", "Very high", "High"),
    ("Claude Opus 4.7", "High", "High"),
    ("Claude Haiku 4.5", "Medium", "Low"),
    ("GPT-5.4", "High", "Medium"),
    ("GPT-5.4 mini", "Medium", "Low"),
    ("GPT-5.3 Codex", "High", "Medium"),
    ("GPT-5 mini", "Medium", "Low"),
]
formatted_table(
    slide,
    cards,
    ["Model", "Relative reasoning / agentic effort", "Overall cost"],
    models,
    [cards[2] * 0.35, cards[2] * 0.42, cards[2] * 0.23],
    font_size=9,
)
deck.takeaway(
    slide,
    foot,
    "Start here",
    "Choose the lowest-cost model expected to clear the task's quality and risk threshold.",
    icon_name="target",
)
deck.notes(
    slide,
    "Introduce manual selection as an exception, not the starting point. These are "
    "relative workshop ratings: effort is derived from agentic quality in the model "
    "chart, and cost is relative. Ask participants to start with the lowest-cost "
    "model that can safely meet the task and risk threshold.",
)

# --- 3. Three tiers, three jobs -------------------------------------------
slide = deck.add_slide(presentation, "Three Content")
deck.set_fields(slide, title="Three tiers, three jobs",
                subtitle="Match the model to the complexity of the task, not habit")
deck.ambient_wash(slide, corner="top-right")
left = deck.claim(slide, "left")
deck.claim(slide, "middle")
right = deck.claim(slide, "right")
band = (left[0], left[1], right[0] + right[2] - left[0], left[3])
cards, foot = deck.split_region_vertical(band, 0.58)
deck.feature_cards(
    slide, cards,
    [
        ("Advanced reasoning", "Deep architecture planning, complex debugging, large refactors, and intricate algorithms. Highest cost."),
        ("Standard flagship", "General chat, documentation, boilerplate, and standard feature work. The daily driver."),
        ("Fast and lightweight", "Syntax checks, simple tests, short explanations, and repetitive patterns when speed matters."),
    ], icons=["idea", "gear", "speed"])
deck.takeaway(slide, foot, "Rule of thumb",
              "A bigger model is not a better answer unless the task genuinely needs the reasoning.",
              icon_name="target")
deck.notes(
    slide,
    "Give a short example for each tier. Use advanced reasoning only when the work "
    "genuinely needs deep analysis, a broad design, or a difficult debugging step. "
    "The daily-driver tier handles most normal work; lightweight models keep routine "
    "tasks quick and economical.",
)

# --- 4. How Auto works -----------------------------------------------------
slide = deck.add_slide(presentation, "Two Content")
deck.set_fields(slide, title="Copilot Auto Model Selection",
                subtitle="Two signals route each task to a reliable best-fit model")
deck.ambient_wash(slide, corner="top-left")
left = deck.claim(slide, "left")
right = deck.claim(slide, "right")
deck.gradient_panel(slide, left)
deck.feature_cards(
    slide, deck.inset_region(left, 0.26),
    [
        ("System health", "Latency, capacity, and error rates help select the reliable model for your session."),
        ("Task intent", "Reasoning, tool orchestration, and debugging needs determine the best task fit."),
    ], columns=1, icons=["latency", "flow"])
benefits = [
    ("Reliable", "Routes around availability and performance changes.", "shield"),
    ("Efficient", "Matches model capability to the work, rather than defaulting high.", "speed"),
    ("10% discount", "Paid users receive a discount on models used through Auto.", "cost"),
]
benefit_height = right[3] / len(benefits)
for index, (heading, body, icon_name) in enumerate(benefits):
    y = right[1] + index * benefit_height
    deck.icon_circle(slide, right[0], y + 0.08, 0.48, deck.accent(index + 2),
                     icon_name=icon_name)
    deck.text(slide, (right[0] + 0.68, y, right[2] - 0.68, 0.35), heading,
              size=17, bold=True)
    deck.text(slide, (right[0] + 0.68, y + 0.4, right[2] - 0.68,
                      benefit_height - 0.45), body, size=12)
deck.notes(
    slide,
    "Explain that Auto combines live service health with the prompt's task needs. "
    "It usually chooses at conversation start or after context compaction to preserve "
    "cache. Emphasise the 10% paid-user discount, but frame Auto's main benefit as "
    "reliable, appropriate routing rather than discount hunting.",
)

# --- 5. Cost ---------------------------------------------------------------
slide = deck.add_slide(presentation, "Two Content")
deck.set_fields(slide, title="Cost",
                subtitle="Value-focused use.")
deck.ambient_wash(slide, corner="bottom-right")
left = deck.claim(slide, "left")
right = deck.claim(slide, "right")
deck.gradient_panel(slide, left)
cost_summary = [
    ("Included with seat", "Code completions, next edit suggestions, and normal inline assistance.", "check"),
    ("Consumes AI credits", "Copilot Chat and CLI; cloud agents and Spaces; Spark, third-party agents, and code review.", "cost"),
]
summary_region = deck.inset_region(left, 0.25)
summary_height = summary_region[3] / len(cost_summary)
for index, (heading, body, icon_name) in enumerate(cost_summary):
    y = summary_region[1] + index * summary_height
    deck.icon_circle(slide, summary_region[0], y + 0.05, 0.4, deck.accent(index), icon_name=icon_name)
    deck.text(slide, (summary_region[0] + 0.58, y, summary_region[2] - 0.58, 0.28), heading, size=15, bold=True)
    deck.text(slide, (summary_region[0] + 0.58, y + 0.32, summary_region[2] - 0.58, summary_height - 0.36), body, size=11)
healthy, unhealthy = deck.split_region(right, 0.5)
deck.comparison(slide, healthy, unhealthy, "Healthy high usage",
                ["Scoped migration or refactor", "Measurable time saving", "Small reviewable increments", "Human checkpoints"],
                "Unhealthy high usage",
                ["Agent loops without progress", "Premium model for routine tasks", "Large discarded diffs", "No link to outcomes"],
                left_colour=deck.GREEN, right_colour=deck.CORAL)
deck.notes(
    slide,
    "Separate included inline assistance from credit-consuming, reasoning-heavy work. "
    "Cost awareness means deliberate use that improves cycle time, quality, reduced toil, "
    "or release confidence; investigate loops, discarded diffs, and routine premium-model use.",
)

# --- 6. Default-tier rates -------------------------------------------------
slide = deck.add_slide(presentation, "Title, Subtitle and Content")
deck.set_fields(slide, title="Default-tier model rates",
                subtitle="USD per 1 million tokens")
region = deck.claim(slide, "content")
deck.ambient_wash(slide, corner="top-right")
rates, foot = deck.split_region_vertical(region, 0.77)
default_rates = [
    ("GPT-5.6 Luna", "$0.20", "$0.02", "$0.25", "$1.20"),
    ("GPT-5.6 Terra", "$2.00", "$0.20", "$2.50", "$12.00"),
    ("GPT-5.6 Sol", "$4.00", "$0.40", "$5.00", "$20.00"),
    ("Claude Sonnet 5", "$2.00", "$0.20", "$2.50", "$10.00"),
    ("Claude Opus 5", "$5.00", "$0.50", "$6.25", "$25.00"),
    ("Claude Opus 4.8", "$5.00", "$0.50", "$6.25", "$25.00"),
    ("Claude Opus 4.7", "$5.00", "$0.50", "$6.25", "$25.00"),
    ("Claude Haiku 4.5", "$1.00", "$0.10", "$1.25", "$5.00"),
    ("GPT-5.4", "$2.50", "$0.25", "N/A", "$15.00"),
    ("GPT-5.4 mini", "$0.75", "$0.075", "N/A", "$4.50"),
    ("GPT-5.3 Codex", "$1.75", "$0.175", "N/A", "$14.00"),
    ("GPT-5 mini", "$0.25", "$0.025", "N/A", "$2.00"),
]
formatted_table(
    slide,
    rates,
    ["Model", "Input", "Cached input", "Cache write", "Output"],
    default_rates,
    [rates[2] * 0.34, rates[2] * 0.15, rates[2] * 0.18, rates[2] * 0.17, rates[2] * 0.16],
    font_size=9,
)
deck.takeaway(slide, foot, "Auto advantage",
              "Choosing Auto provides a 10% discount on AI-credit cost. These are token rates, not fixed request prices.",
              icon_name="target")
deck.notes(
    slide,
    "These are token rates per 1 million tokens, not fixed request prices. Cache writes "
    "apply to Anthropic and GPT-5.6 models; some models have higher long-context rates. "
    "Auto's 10% AI-credit discount applies to models selected through Auto. Direct the "
    "audience to the linked source for current pricing.",
)

# --- 7. Sustainable habits -------------------------------------------------
slide = deck.add_slide(presentation, "Title, Subtitle and Content")
deck.set_fields(slide, title="Four habits that keep it efficient",
                subtitle="Lower cost and lower energy, without lower quality")
region = deck.claim(slide, "content")
deck.ambient_wash(slide, corner="bottom-left")
steps, foot = deck.split_region_vertical(region, 0.56)
deck.numbered_rail(
    slide, steps,
    [
        ("Right-size the model", "Use the smallest model expected to meet the task's quality and risk threshold."),
        ("Go local for simple work", "Use lightweight local models where policy permits and the task is appropriate."),
        ("Reserve reasoning models", "Avoid spending deep reasoning tokens on routine boilerplate or documentation."),
        ("Batch your requests", "Ask for related changes together instead of repeating context one error at a time."),
    ])
deck.takeaway(slide, foot, "Check first",
              ["Prefer providers that publish environmental metrics. The ",
               ("AI Energy Score leaderboard", {"link": ENERGY_SCORE}),
               " is a useful starting point."], icon_name="search")
deck.notes(
    slide,
    "Close with four habits participants can apply today. State that local models are "
    "only appropriate where policy permits. Do not provide unverified energy numbers; "
    "point to the AI Energy Score leaderboard for transparent published information.",
)

# --- 8. Closing ------------------------------------------------------------
slide = deck.add_slide(presentation, "End - Dark")
deck.notes(slide, "Thank the audience and invite questions or transition to the next workshop section.")

deck.save(presentation, DECK)
print("Built", DECK)
