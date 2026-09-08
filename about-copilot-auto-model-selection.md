# How Auto Mode Works

GitHub Copilot auto mode streamlines workflows by using intelligent, task-based routing. Auto model selection with task optimization combines two systems to provide high quality results and better reliability. One system tracks real-time system health and availability, while the other evaluates task complexity. Putting these together, auto model selection routes the task to the optimal model.

- Dynamic Model Selection: The system monitors real-time metrics, including latency, capacity, and error rates, to rerank and select the most reliable model available for your session.

- Task Intent Routing: Beyond simple availability, the router analyzes the nature and complexity of your specific request. It evaluates dimensions like reasoning, tool orchestration, and debugging needs to match the prompt with the best-fit model .

- Optimization Over Manual Selection: Evaluations show that this system often outperforms using a single, high-reasoning model alone. By correctly matching the task to either a smaller or larger model, users gain both token efficiency and cost savings.

= Session Management: To maintain efficiency and preserve cache, the system typically routes at the start of a conversation or after context compaction, rather than re-evaluating every single user prompt.

Additionally, all paid users receive a 10% discount on models used through auto mode

Reference
<https://www.youtube.com/watch?v=a-c1M8QwK84>
<https://docs.github.com/en/copilot/concepts/models/auto-model-selection>
