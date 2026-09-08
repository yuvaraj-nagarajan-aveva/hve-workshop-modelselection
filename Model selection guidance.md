# Model selection

1. Advanced Reasoning Models
When to choose: Deep architecture planning, complex debugging, refactoring large codebases, or writing intricate algorithms.
Context: Use these when you are stuck on a difficult logical problem or need a comprehensive system design.
2. Standard Flagship Models
When to choose: General chat, writing documentation, generating boilerplate code, and standard feature implementation.
Context: This can be the "daily driver" category. They offer a great balance of speed, accuracy, and understanding of context window semantics.
3. Fast / Lightweight Models (
When to choose: Quick syntax checks, writing simple unit tests, explaining a small block of code, or generating repetitive code patterns.
Context: Use these when speed is your highest priority or you want to conserve API tokens/credits.

- Model Scale: Match the model size to the complexity of the task. A smaller, highly targeted model (e.g., 7B to 8B parameters) or a distilled variant often matches the performance of a massive frontier model while consuming a fraction of the energy.

- Auto usually routes easier questions to cheaper, smaller models and saves the expensive flagship models for genuinely difficult prompts.

Standard Coding Workflows: If you are jumping seamlessly between asking "what does this function do?" (low complexity) and "write a regex for this" (medium complexity), Auto will correctly match the model to the task without interrupting your flow.

## What is billed vs what is included?

Inline assistance remains included with the seat; reasoning-heavy features drive variable usage.

### Included with seat

- Code completions
- Next edit suggestions
- Normal inline developer assistance

### Consumes AI credits

- Copilot Chat and CLI
- Cloud agent and Spaces
- Spark and third-party coding agents
- Copilot code review

Variable cost tends to come from reasoning, planning, context, tool use, and autonomy.

## Cost awareness is not cost avoidance

Optimise for engineering value, not the lowest possible AI usage.

Not less AI. Better value.

Cost awareness means deliberate use, not reluctant use.

- High usage can be healthy when it accelerates important work.
- Low usage is not automatically efficient.
- The best outcome is valuable engineering work from the credits we use.

Optimise for cycle time, quality, reduced toil, and release confidence.

## What healthy usage looks like

Governance should distinguish valuable investment from inefficient workflow.

### Healthy high usage

- Scoped migration or refactor
- Measurable time saving
- Small reviewable increments
- Human checkpoints

### Unhealthy high usage

- Agent loops without progress
- Premium model for routine tasks
- Large discarded diffs
- No link to outcomes

Understand high usage before judging it.

## Sustainability

- Provider Transparency: Look for vendors that provide Model Cards with environmental metrics (e.g., Hugging Face's Energy Score or Salesforce’s impact section). These act as "nutrition labels" detailing energy-per-token and training emissions
Refer: <https://huggingface.co/spaces/AIEnergyScore/Leaderboard>

- Prioritize Edge / Local Models: Use ultra-lightweight models (like Llama 3 or Phi-4) hosted locally via Ollama for simple tasks. Running models on your own machine eliminates the massive energy overhead of data center routing, cooling, and network transmission.

- Minimize "Reasoning" Tokens for Routine Work: Deep reasoning models generate thousands of internal "thinking" tokens before outputting code. Avoid using them for routine boilerplate or documentation, as they consume significantly more server-side power per request.

- Batch Your Requests: Instead of asking the AI to fix small errors line-by-line, gather your requirements and ask for multiple related changes in a single, well-structured prompt. This reduces the repetitive overhead of transmitting the same codebase context over and over.
