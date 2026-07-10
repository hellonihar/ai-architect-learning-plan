# Prompt Management Pattern

## Overview

Treat prompts as first-class artifacts: versioned, tested, and deployed through a CI/CD pipeline alongside application code.

---

## Architecture

```
Prompt Authoring (Playground / IDE)
  → Version Control (Git)
    → CI (lint, eval, test)
      → Prompt Registry (DB / file store)
        → Deployment (dev → staging → prod)
          → Runtime (A/B test, monitor)
```

---

## Key Components

| Component | Purpose |
|-----------|---------|
| Prompt Registry | Stores prompt templates by ID, version, environment |
| Eval Pipeline | Runs automated quality checks on prompt changes |
| A/B Testing | Routes traffic between prompt versions |
| Rollback | Reverts to previous prompt version on degradation |

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Storage | Git / DB / dedicated registry | Git for small teams, registry for enterprise |
| Versioning | Semantic / Git hash / timestamp | Git hash (traceable to code changes) |
| Eval trigger | Manual / PR gate / scheduled | PR gate (block merge if quality drops) |
| Rollout | Canary / blue-green / all-at-once | Canary (10% → 50% → 100%) |

---

## References

- [Prompt engineering with Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/prompt-management)
- [OpenAI prompt management](https://platform.openai.com/docs/guides/prompt-management)
