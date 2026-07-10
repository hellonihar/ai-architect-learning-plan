# Fine-tuning Pipeline Pattern

## Overview

Customize a base model on domain-specific data through a repeatable pipeline from data preparation to deployment.

---

## Architecture

```
Data Collection
  → Data Preparation (curation, formatting, validation)
    → Training Job (Azure OpenAI / Hugging Face)
      → Evaluation (holdout set, LLM-as-judge)
        → Comparison (baseline vs fine-tuned)
          → Deployment (A/B test, gradual rollout)
            → Monitoring (quality drift, data drift)
```

---

## When to Fine-tune vs RAG

| Approach | Best for | Cost | Maintenance |
|----------|---------|------|-------------|
| RAG | Frequently updated knowledge | Low (vector storage) | Low (update docs) |
| Fine-tuning | Consistent behavior, style, tone | High (training + hosting) | Medium (retrain on drift) |
| Both | Deep domain expertise + live data | Highest | High |

---

## Data Preparation

```
Raw Data
  → Clean (remove PII, duplicates, low-quality)
    → Format (conversation format for chat models)
      → Validate (schema check, token limits)
        → Split (train 80% / eval 10% / test 10%)
          → Upload (JSONL format)
```

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Base model | GPT-4o-mini / GPT-4o / open-source | Start with GPT-4o-mini (cheaper to train) |
| Epochs | 1–5 | 3 (balance under/overfitting) |
| Eval method | Holdout set / LLM-as-judge / human eval | Holdout set for regression, LLM-as-judge for quality |
| Deployment | Same endpoint / new endpoint | New endpoint for A/B comparison |
| Retrain trigger | Scheduled / drift detected / manual | Drift detection (automated quality monitoring) |

---

## References

- [Azure OpenAI fine-tuning guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/fine-tuning)
- [OpenAI fine-tuning docs](https://platform.openai.com/docs/guides/fine-tuning)
