# Evaluation & Observability Pattern

## Overview

Continuous measurement of AI output quality and system health through automated evaluation pipelines and tracing.

---

## Architecture

```
Production Traffic
  ↓
Trace (LangSmith / App Insights)
  ├── Span 1: Input guard check
  ├── Span 2: LLM call (model, tokens, latency)
  ├── Span 3: Tool call (search result, score)
  └── Span 4: Output guard check
       ↓
Eval Pipeline (async)
  ├── Accuracy (LLM-as-judge)
  ├── Faithfulness (groundedness check)
  ├── Relevance (cosine similarity)
  └── Toxicity (content safety API)
       ↓
Dashboard (Grafana / App Insights)
```

---

## Metrics

| Category | Metrics | Collection |
|----------|---------|------------|
| Quality | Accuracy, faithfulness, relevance, toxicity | Async eval pipeline |
| Performance | Latency (P50/P95/P99), TTFT | Traced spans |
| Cost | Tokens per query, cost per user | Logged per request |
| Usage | Queries per user, active users, session length | Application logs |

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Tracing | OpenTelemetry / LangSmith / App Insights | OpenTelemetry for vendor neutrality |
| Eval model | GPT-4o-mini / o1 / dedicated eval model | GPT-4o-mini (cost-effective) |
| Alerting | Threshold / anomaly detection | Anomaly detection for quality, threshold for latency |
| Sampling | 100% / 10% / adaptive | Adaptive (100% of anomalies, 10% of normal) |

---

## References

- [LangSmith tracing](https://docs.smith.langchain.com/)
- [Application Insights for AI](https://learn.microsoft.com/en-us/azure/azure-monitor/app/ai-monitoring/)
