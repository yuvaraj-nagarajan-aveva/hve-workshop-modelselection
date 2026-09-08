# Copilot Model Costs

This table covers the models listed in [model-chart.md](References/model-chart.md).
All rates are in USD per 1 million tokens and are converted to GitHub AI credits
when billed. One GitHub AI credit equals $0.01 USD.

Source: [GitHub Copilot models and pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing). Accessed 2026-09-08.

## Default-tier rates

| Model | Input | Cached input | Cache write | Output |
| --- | ---: | ---: | ---: | ---: |
| GPT-5.6 Luna | $0.20 | $0.02 | $0.25 | $1.20 |
| GPT-5.6 Terra | $2.00 | $0.20 | $2.50 | $12.00 |
| GPT-5.6 Sol | $4.00 | $0.40 | $5.00 | $20.00 |
| Claude Sonnet 5 | $2.00 | $0.20 | $2.50 | $10.00 |
| Claude Opus 5 | $5.00 | $0.50 | $6.25 | $25.00 |
| Claude Opus 4.8 | $5.00 | $0.50 | $6.25 | $25.00 |
| Claude Opus 4.7 | $5.00 | $0.50 | $6.25 | $25.00 |
| Claude Haiku 4.5 | $1.00 | $0.10 | $1.25 | $5.00 |
| GPT-5.4 | $2.50 | $0.25 | Not applicable | $15.00 |
| GPT-5.4 mini | $0.75 | $0.075 | Not applicable | $4.50 |
| GPT-5.3 Codex | $1.75 | $0.175 | Not applicable | $14.00 |
| GPT-5 mini | $0.25 | $0.025 | Not applicable | $2.00 |

## Long-context rates

GitHub lists long-context pricing for the following models. The threshold is the
number of input tokens at which the long-context rate applies.

| Model | Input-token threshold | Input | Cached input | Cache write | Output |
| --- | ---: | ---: | ---: | ---: | ---: |
| GPT-5.6 Luna | More than 200K | $0.40 | $0.04 | $0.50 | $1.80 |
| GPT-5.6 Terra | More than 272K | $4.00 | $0.40 | $5.00 | $18.00 |
| GPT-5.6 Sol | More than 272K | $8.00 | $0.80 | $10.00 | $30.00 |
| GPT-5.4 | More than 272K | $5.00 | $0.50 | Not applicable | $22.50 |

## Notes

- Anthropic models listed here charge for cache writes as well as input, cached
  input, and output tokens.
- GPT-5.6 Luna, Terra, and Sol also charge for cache writes. Earlier OpenAI
  models in this table do not.
- Choosing Auto provides a 10% discount on AI-credit cost.
- Code completions and next edit suggestions are not billed in AI credits.
- Copilot code review uses an automatically selected, undisclosed model, so its
  per-token cost cannot be derived from this table.
- Recheck the linked source before publishing or presenting this data; model
  availability and rates can change.
