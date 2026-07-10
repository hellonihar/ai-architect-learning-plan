# Caching Strategies Pattern

## Overview

Multi-level caching reduces latency, cost, and load on LLM APIs by serving repeated or similar queries from cache.

---

## Cache Levels

```
Query
  ↓
Level 1 — Exact Match Cache (Redis / Memcached)
  Identical query + system prompt → return cached response
  TTL: 1h–24h depending on data staleness
  ↓ miss
Level 2 — Semantic Cache (Vector DB)
  Similar query (cosine > 0.95) → return cached response
  TTL: 1h–24h
  ↓ miss
Level 3 — Embedding Cache (Local / Redis)
  Reuse computed embeddings for same text
  TTL: session or permanent
  ↓ miss
Level 4 — LLM Call
```

---

## Caching Decision Matrix

| Cache Type | Hit Rate | Latency Savings | Cost Savings | Implementation Complexity |
|------------|----------|----------------|--------------|---------------------------|
| Exact match | 5–15% | 50–100ms | 100% of token cost | Low (Redis GET/SET) |
| Semantic | 20–40% | 100–300ms | 100% of token cost | Medium (vector search) |
| Embedding | 30–50% | 200–500ms | Embedding cost only | Low (dict lookup) |

---

## Cache Invalidation

| Trigger | Action |
|---------|--------|
| Time-based TTL | Automatic expiration |
| Document update | Invalidate related semantic cache entries |
| Prompt change | Flush all cache for that prompt ID |
| Manual | Admin purge endpoint |

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Semantic similarity threshold | 0.90 / 0.95 / 0.99 | 0.95 (balance recall vs correctness) |
| Cache storage | Redis / Azure Cache / in-memory | Redis (durable, shared across instances) |
| Embedding cache | Local / Redis / none | Local for single-instance, Redis for multi-instance |
| Invalidation | TTL / event-driven / manual | TTL + event-driven (document changes) |

---

## References

- [Redis caching patterns](https://redis.io/docs/manual/patterns/)
- [Semantic caching for LLMs (research)](https://arxiv.org/abs/2405.02693)
