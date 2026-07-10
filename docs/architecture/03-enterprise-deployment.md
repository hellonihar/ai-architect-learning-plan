# Enterprise AI Deployment

## Architecture Components

```
Client App
  → API Gateway / AI Gateway
    → Load Balancer
      → Model Endpoints (GPT-4o, o1, o3)
        → Vector Store (Azure AI Search)
        → Cache (Redis)
        → Guardrails (Azure AI Content Safety)
  → Monitoring & Observability (App Insights)
```

---

## AI Gateway Responsibilities

- Rate limiting and throttling
- Authentication and authorization
- Request/response logging
- Model routing (GPT-4o vs o1 based on complexity)
- Cost tracking per user/team
- Prompt injection detection

---

## Deployment Models

| Model | Latency | Cost | Use Case |
|-------|---------|------|----------|
| Global Standard | Low | Low | General chat, summarization |
| Data Zone Standard | Low | Low | Data residency requirements |
| Provisioned Throughput | Very low | High (committed) | High-volume production |

---

## Observability

| Metric | Tool |
|--------|------|
| Token usage per user | App Insights custom metrics |
| Response latency | App Insights requests |
| Hallucination rate | LLM-as-judge eval pipeline |
| Cost per query | Cost Management + tags |
| User satisfaction | Feedback collection + sentiment |

---

## RAI (Responsible AI)

- Content filtering (Azure AI Content Safety)
- Rate limiting to prevent abuse
- PII detection and redaction
- Audit logs for all model interactions
- Human review for sensitive decisions
