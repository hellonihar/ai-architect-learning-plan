# Agent Patterns

## Overview

AI agents use LLMs to reason, call tools, and take actions autonomously to accomplish goals.

---

## Patterns

### ReAct (Reasoning + Acting)
```
Thought → Action → Observation → Thought → Action → ... → Final Answer
```

- Interleaves reasoning with tool calls
- Observable chain-of-thought
- Good for single-agent tasks

### Multi-Agent Orchestration
```
Supervisor/Orchestrator
  ├── Research Agent (web search + summarization)
  ├── Coding Agent (code generation + execution)
  ├── Review Agent (quality check + critique)
  └── Reporting Agent (format + output)
```

- Each agent has a specialized role
- Supervisor delegates and aggregates
- Enables complex workflows

### Planning Agents
```
Goal → Task Decomposition → Dependency Graph
  → Parallel Execution → Verify → Iterate
```

- Decomposes complex goals into sub-tasks
- Handles dependencies between tasks
- Re-plans on failure

### Human-in-the-Loop
```
Agent → Escalation Decision → Human Approval → Continue / Abort
```

- Agent identifies high-risk actions
- Pauses for human input
- Logs all decisions for audit

---

## Tool Calling

Tools are functions the agent can invoke:

```python
tools = [
    {
        "name": "search_docs",
        "description": "Search internal documentation",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            },
            "required": ["query"]
        }
    }
]
```

---

## Key Considerations

| Concern | Approach |
|---------|----------|
| Max iterations | Set limit (e.g., 25) to avoid infinite loops |
| Error recovery | Retry with backoff, fallback to human |
| Observability | Log every thought, action, and observation |
| Security | Sandbox tool execution, validate inputs |
| Cost | Cache common queries, limit tool calls per session |
