# Cost vs Quality Trade-offs

## Model Selection

| Task | Recommended Model | Cost (per 1M tokens) | Quality |
|------|-------------------|---------------------|---------|
| Simple Q&A | GPT-4o-mini | ~$0.15 | Good |
| Complex reasoning | o1 / o3 | ~$10–15 | Excellent |
| Summarization | GPT-4o-mini | ~$0.15 | Good |
| Code generation | GPT-4o / Claude 3.5 | ~$2.50–3.00 | Very good |
| Classification | GPT-4o-mini | ~$0.15 | Good |
| Creative writing | GPT-4o | ~$2.50 | Excellent |

---

## Optimization Strategies

### Prompt Compression
- Remove redundant instructions
- Use concise few-shot examples
- Leverage system prompt (not repeated per message)

### Caching
- Cache exact query matches (Redis)
- Cache embedding vectors
- Cache common LLM responses (semantic cache)

### Batching
- Batch independent requests
- Process during off-peak hours for non-urgent tasks

### Model Routing
```
Simple query (classifier)
  → GPT-4o-mini (fast, cheap)
Complex query (classifier)
  → GPT-4o / o1 (slow, expensive)
```

---

## Quality Monitoring

| Signal | Detection Method | Action |
|--------|-----------------|--------|
| Hallucination | Groundedness check | Fall back to "I don't know" |
| Off-topic | Intent classifier | Re-route or clarify |
| Toxicity | Content safety API | Block / redact |
| Low confidence | Logprobs analysis | Escalate to human |

---

## Cost Budgeting

- Set per-user / per-team token budgets
- Dashboard with cost per query and daily spend
- Alerts on spend anomalies
- Monthly review of model usage vs performance
