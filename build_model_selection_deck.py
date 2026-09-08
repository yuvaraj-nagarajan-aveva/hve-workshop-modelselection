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

presentation = deck.open_deck(DECK)
deck.accent_order(deck.GREEN)

# --- 1. Three tiers, three jobs -------------------------------------------
slide = deck.add_slide(presentation, "Three Content")
deck.set_fields(
    slide,
    title="Three tiers, three jobs",
    subtitle="Match the model to the complexity of the task, not to habit",
)
deck.ambient_wash(slide, corner="top-right")
left = deck.claim(slide, "left")
deck.claim(slide, "middle")
right = deck.claim(slide, "right")
band = (left[0], left[1], right[0] + right[2] - left[0], left[3])
cards, foot = deck.split_region_vertical(band, 0.58)
foot = (foot[0], foot[1], foot[2], 1.15)  # the band only needs one line

deck.feature_cards(
    slide,
    cards,
    [
        (
            "Advanced reasoning",
            "Deep architecture planning, complex debugging, large refactors, "
            "intricate algorithms. Highest cost and energy per request.",
        ),
        (
            "Standard flagship",
            "The daily driver. General chat, documentation, boilerplate and "
            "standard feature work, with a good balance of speed and accuracy.",
        ),
        (
            "Fast and lightweight",
            "Quick syntax checks, simple unit tests, explaining a short block, "
            "repetitive patterns. Reach for it when speed is the priority.",
        ),
    ],
    icons=["idea", "gear", "speed"],
)

deck.takeaway(
    slide,
    foot,
    "Rule of thumb",
    "A bigger model is not a better answer. It is a slower, more expensive one "
    "\u2014 unless the task genuinely needs the reasoning.",
    icon_name="target",
)

# --- 2. Start on Auto ------------------------------------------------------
slide = deck.add_slide(presentation, "Two Content")
deck.set_fields(
    slide,
    title="Start on Auto",
    subtitle="Let the router do the routine, and override on purpose",
)
deck.ambient_wash(slide, corner="top-left")
left = deck.claim(slide, "left")
right = deck.claim(slide, "right")

deck.gradient_panel(slide, left)
inner = deck.inset_region(left, 0.36)
deck.text(
    slide,
    (inner[0], inner[1], inner[2], 0.5),
    "Why Auto is the default",
    size=20,
    bold=True,
    colour=deck.heading_ink(slide),
)

points = [
    ("It routes easier questions to cheaper, smaller models and saves the "
     "flagship models for genuinely difficult prompts.", "flow"),
    ("You move between \u201cwhat does this function do?\u201d and \u201cwrite a "
     "regex for this\u201d without breaking your flow.", "cycle"),
    ("The smallest model that can do the job is also the one that burns the "
     "least energy, so the convenient default is the sustainable one.", "global"),
]
top = inner[1] + 0.85
step = (inner[1] + inner[3] - top) / len(points)
for index, (line, icon_name) in enumerate(points):
    y = top + index * step
    deck.icon_circle(slide, inner[0], y, 0.56, deck.accent(index),
                     icon_name=icon_name)
    deck.text(
        slide,
        (inner[0] + 0.86, y - 0.06, inner[2] - 0.86, step - 0.2),
        line,
        size=15,
    )

deck.feature_cards(
    slide,
    right,
    [
        ("Override up",
         "You are stuck on a genuinely hard logical problem, or you need a "
         "whole system design rather than an answer."),
        ("Override down",
         "The work is mechanical and you already know the shape of the "
         "answer. Speed is what you want, not depth."),
    ],
    columns=1,
    icons=["layers", "speed"],
)

# --- 3. Four habits --------------------------------------------------------
slide = deck.add_slide(presentation, "Title, Subtitle and Content")
deck.set_fields(
    slide,
    title="Four habits that keep it cheap",
    subtitle="Lower cost and lower energy, without lower quality",
)
region = deck.claim(slide, "content")
deck.ambient_wash(slide, corner="bottom-left")
steps, foot = deck.split_region_vertical(region, 0.56)
foot = (foot[0], foot[1], foot[2], 1.45)  # the band only needs two lines

deck.numbered_rail(
    slide,
    steps,
    [
        ("Right-size the model",
         "A smaller, targeted model often matches a frontier model on a narrow "
         "task for a fraction of the energy."),
        ("Go local for simple work",
         "Ultra-lightweight models on your own machine skip data centre "
         "routing, cooling and network overhead."),
        ("Reserve reasoning models",
         "They emit thousands of internal thinking tokens first. Do not spend "
         "that on boilerplate or documentation."),
        ("Batch your requests",
         "Ask for several related changes in one structured prompt instead of "
         "fixing errors line by line."),
    ],
)

deck.takeaway(
    slide,
    foot,
    "Check first",
    [
        "Prefer vendors that publish model cards with energy per token and "
        "training emissions. The ",
        ("AI Energy Score leaderboard", {"link": ENERGY_SCORE}),
        " is the nutrition label for this.",
    ],
    icon_name="search",
)

# --- 4. Closing ------------------------------------------------------------
deck.add_slide(presentation, "End - Dark")

deck.save(presentation, DECK)
print("Built", DECK)
