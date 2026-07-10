# Model Router & Fallback Pattern

## Overview

Route queries to the optimal model based on complexity, cost targets, and availability. Fall back gracefully on failure.

---

## Architecture

```
Query → Classifier (GPT-4o-mini)
  ├── Simple → GPT-4o-mini (cheap, fast)
  ├── Complex → GPT-4o (balanced)
  ├── Reasoning → o1 / o3 (expensive, slow)
  └── Fallback chain:
        1. Primary model
        2. Secondary model (e.g., o1 → GPT-4o)
        3. Cache (stale but available)
        4. Graceful degradation ("I'm unavailable, try again later")
```

---

## Routing Strategies

| Strategy | How it works | Best for |
|----------|-------------|----------|
| Threshold | Score query complexity 1-10, route by band | Predictable workloads |
| ML classifier | Train a model to classify query type | Heterogeneous traffic |
| Cost budget | Track cost per user, route to cheaper model when over budget | Consumer apps |
| A/B comparison | Route to multiple models, pick best response | Evaluation |

---

## Fallback Chain

```
try:
    return await call_primary_model(query)
except RateLimitError:
    return await call_secondary_model(query)
except TimeoutError:
    return await call_cache(query)
except Exception:
    return GracefulResponse("I'm unavailable. Please try again.")
```

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Classifier | LLM / ML model / regex | LLM (GPT-4o-mini, no training needed) |
| Fallback timeout | 2s / 5s / 10s | 5s (balance UX vs completion rate) |
| Cache fallback TTL | 1m / 5m / 1h | 5m for general, 1m for real-time queries |

---

## References

- [OpenAI model selection guide](https://platform.openai.com/docs/guides/model-selection)
- [Azure OpenAI fallback pattern](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/fine-tuning-fallback)
