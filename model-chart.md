# Copilot Model Chart

**Rating scales**

- **Speed:** relative response latency and throughput (`fast`, `medium`, `slow`)
- **Model size:** approximate parameter count (`small` < 200b, `medium` < 1t, `large` < 5t, `huge`)
- **Cost:** relative AI-credit or usage cost (`low`, `medium`, `high`)
- **Code quality:** expected software-development output quality (`low`, `medium`, `high`)
- **Agentic quality:** expected planning, tool use, and multi-step task quality (`low`, `medium`, `high`)
- **Context size options:** Copilot CLI context tiers (`default`, `long_context`); these labels do not specify token counts

| Model | Speed | Model size | Cost | Code quality | Agentic quality | Context size options |
| --- | --- | --- | --- | --- | --- | --- |
| GPT-5.6 Luna | medium | medium | low | high | high | 328k, 1.1m |
| GPT-5.6 Terra | slow | large | medium | very high | very high | 400k, 1.1m |
| GPT-5.6 Sol | fast | huge | high | extremely high | very high | 400k, 1.1m |
| Claude Sonnet 5 | medium | medium | medium | high | high | 264k, 1m |
| Claude Opus 5 | slow | large | high | very high | very high | 264k, 1m |
| Claude Opus 4.8 | slow | large | high | very high | very high | 264k, 1m |
| Claude Opus 4.7 | medium | large | high | high | high | 264k, 1m |
| Claude Haiku 4.5 | fast | small | low | low | medium | 200k |
| GPT-5.4 | medium | large | medium | medium | high | 400k, 1.1m |
| GPT-5.4 mini | fast | small | low | low | medium | 400k |
| GPT-5.3 Codex | medium | large | medium | medium | high | 400k |
| GPT-5 mini | fast | small | low | low | medium | 400k |

## Interpretation

Use the chart as a starting point for model selection:

- Start with the lowest-cost model expected to clear the task's quality and risk threshold.
- Prefer a stronger model for high-risk, ambiguous, repository-wide, or highly agentic work.
- Treat context tiers as selectable options, not as a guarantee that every task benefits from the largest context.
- Recheck model availability, pricing, aliases, and context limits when Copilot or the model catalog changes.
