# RAG (Retrieval-Augmented Generation) Pattern

## Overview

RAG enhances LLM responses by grounding them in external knowledge sources, reducing hallucination and improving accuracy.

---

## Architecture Levels

### Naive RAG
```
User Query → Embedding → Vector Search → Retrieved Chunks → LLM → Response
```

- Single-shot retrieval
- Static chunking
- No query rewriting

### Advanced RAG
```
User Query → Query Rewriting → Hybrid Search (Vector + Keyword)
  → Re-ranking → Context Compression → LLM → Response + Citations
```

- Query transformation (rewriting, expansion)
- Hybrid search (dense + sparse)
- Re-ranking for precision
- Context compression to fit token limits

### Agentic RAG
```
User Query → Agent → Tool Selection
  ├── Web Search
  ├── Vector Search
  ├── SQL Query
  └── Code Interpreter
       → Aggregation → LLM → Response
```

- Dynamic tool selection based on query
- Multi-hop reasoning
- Self-correction and iteration

---

## Key Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Embedding model | `text-embedding-3-small` / `ada-002` | `text-embedding-3-small` (cost/quality) |
| Vector store | Azure AI Search / Chroma / Pinecone | Azure AI Search (enterprise) |
| Chunking strategy | Fixed / Semantic / Recursive | Semantic chunking (better context) |
| Search type | Pure vector / Hybrid | Hybrid (recall + precision) |
| Re-ranking | Cohere / Azure AI / Cross-encoder | Cross-encoder (higher quality) |

---

## References

- [Azure RAG pattern](https://learn.microsoft.com/en-us/azure/developer/ai/get-started-rag)
- [RAG Survey (arXiv)](https://arxiv.org/abs/2312.10997)
