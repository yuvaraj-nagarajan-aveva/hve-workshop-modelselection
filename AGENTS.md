# AGENTS.md

## Purpose

This repository produces an internal HVE workshop presentation on selecting AI
models with quality, cost, and sustainability in mind.

## Repository map

- `Model selection guidance.md` is the authoritative content source for model
  tiers, Auto routing, and sustainable-use practices.
- `build_model_selection_deck.py` builds `Model-Selection-Guidance.pptx` using
  the AVEVA deck helper.
- `References/` contains workshop context. Do not modify the referenced
  workshop deck; this repository produces an insert that the presenter merges
  separately.
- `preview/` holds rendered slide previews for visual review.

## Content rules

- Do not invent pricing, energy-per-token, emissions, benchmark figures, or
  claims about approved local-model tooling. Record missing evidence in the
  plan or presenter handover instead.
- Keep the sustainability guidance practical and proportional. Cost, latency,
  quality, privacy, and local-policy constraints may all affect a model choice.
- Retain the live AI Energy Score leaderboard link when referring to energy
  transparency, unless replacing it with a verified, approved source.

## Deck workflow

1. Use aveva-author plugin and aveva-pptx skill to generate the slides
1. Keep each slide visually composed and readable, rather than turning content
   areas into dense bullet lists. Every content slide needs a meaningful visual
   element.
1. Refer to model-chart.md for listing of models
1. Obtain models and pricing info from <https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing>

## Build and review

- Run `python build_model_selection_deck.py` from the repository root to
  regenerate the presentation after changing the build script or approved plan.
- Review the rendered `preview/` images after every rebuild for text overflow,
  clipping, contrast, alignment, layout drift, and repeated compositions.

## Editing conventions

- Use plain, direct workshop language. Explain trade-offs without marketing
  claims or false precision.
- Update `README.md` when build prerequisites, output names, or repository
  workflow change.
