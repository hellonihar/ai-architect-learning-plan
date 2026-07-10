# AI + Workflow Integration Pattern

## Overview

Bridge AI agents with existing workflow automation systems (Power Automate, Logic Apps, custom BPM) for human-in-the-loop processes.

---

## Architecture

```
User → Frontend / Portal
  ↓
AI Agent (orchestrates reasoning + tool calls)
  ↓
Workflow Bridge (API Layer)
  ├── Trigger Power Automate Flow (approval, notification)
  ├── Create Logic App Job (async processing)
  ├── Update BPMN Process (signal task completion)
  └── Send to Queue (Service Bus / Event Grid)
       ↓
Existing Workflow System
  → Human Approval → Completion → Callback to Agent
```

---

## Integration Patterns

| Pattern | How it works | Use Case |
|---------|-------------|----------|
| Agent-triggered flow | Agent calls workflow API when it needs human input | Expense approval, content review |
| Workflow-triggered agent | Existing workflow calls AI agent via HTTP | Document classification during onboarding |
| Agent as workflow step | Agent replaces a manual decision step in BPMN | Automated claims adjudication |
| Parallel agent + workflow | Agent suggests, workflow routes for approval | Marketing content generation |

---

## Mapping Low-code to AI

| Low-code concept | AI equivalent |
|-----------------|---------------|
| Trigger | Agent tool call / event listener |
| Condition | LLM decision (router agent) |
| Action | Tool execution (search, API call) |
| Loop | Agent iteration (ReAct loop) |
| Exception handler | Fallback chain, human escalation |
| Variable | Agent memory / conversation context |

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Workflow engine | Power Automate / Logic Apps / Temporal | Logic Apps (Azure-native, lower cost) |
| Communication | HTTP / Queue / Event Grid | Queue (decoupled, reliable) |
| State management | In agent / in workflow / both | Workflow owns state, agent owns context |
| Escalation | Agent escalates / workflow escalates | Workflow (existing escalation paths) |

---

## References

- [Power Automate AI flows](https://learn.microsoft.com/en-us/power-automate/ai-flows/)
- [Azure Logic Apps with AI](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-ai-builder/)
