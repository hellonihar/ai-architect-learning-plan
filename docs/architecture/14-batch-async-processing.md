# Batch & Async Processing Pattern

## Overview

Process large volumes of AI tasks asynchronously using queues, batch APIs, and result polling for cost efficiency and scalability.

---

## Architecture

```
Client → Submit Job (POST /jobs)
  → Queue (Service Bus / Event Grid)
    → Worker Pool (Container Apps / Functions)
      → Batch LLM Processing (OpenAI batch API / parallel calls)
        → Result Store (Blob Storage / Cosmos DB)
          → Notification (Event Grid / Webhook)
            → Client polls GET /jobs/{id}
```

---

## Sync vs Async Decision

| Factor | Sync | Async |
|--------|------|-------|
| Volume | <10 requests/min | 100–100,000 requests/min |
| Latency requirement | <5s | >30s acceptable |
| Cost sensitivity | Low | High (batch API is 50% cheaper) |
| User waiting | Yes | No (background) |

---

## OpenAI Batch API

- **50% cost reduction** vs real-time
- Submit batch JSONL file → poll for completion
- 24-hour completion SLA (typically <6h)
- Good for: evaluations, bulk classification, data enrichment

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Queue | Service Bus / Event Grid / Kafka | Service Bus (exactly-once delivery) |
| Worker | Azure Functions / Container Apps / AKS | Container Apps (auto-scale, per-request billing) |
| Batch granularity | Per-item / per-job | Per-job (batch API), per-item (real-time) |
| Retry policy | Linear / exponential / dead-letter | Exponential backoff + dead-letter after 5 retries |
| Result storage | Blob / Cosmos DB / Table | Blob for large payloads, Cosmos for structured results |

---

## References

- [OpenAI Batch API](https://platform.openai.com/docs/guides/batch)
- [Azure Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/)
