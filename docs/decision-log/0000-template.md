# ADR-0000: [Title]

## Status

[Proposed | Accepted | Deprecated | Superseded]

## Context

[What is the issue that we're seeing that is motivating this decision?]

## Decision

[What is the change that we're proposing and/or doing?]

## Consequences

[What becomes easier or more difficult as a result?]

---

## Example

```markdown
# ADR-0001: Use Azure AI Search for Vector Store

## Status
Accepted

## Context
We need a vector store for RAG that supports hybrid search,
is enterprise-grade (SLA, RBAC, geo-redundancy), and integrates
with Azure OpenAI.

## Decision
Use Azure AI Search with:
- Hybrid search (dense + sparse)
- Semantic ranker for re-ranking
- Integrated vectorization (Azure OpenAI embeddings)

## Consequences
- + Native Azure integration, no extra vendor
- + RBAC and private endpoint support
- - Higher cost vs open-source solutions (Chroma, Qdrant)
- - Requires provisioning and configuration
```
