# Data Pipeline for AI Pattern

## Overview

Ingest, process, chunk, embed, and index documents to power RAG and fine-tuning workflows.

---

## Architecture

```
Source Documents
  ├── SharePoint / OneDrive
  ├── Blob Storage
  ├── Web crawler
  └── Database (SQL / Cosmos DB)
       ↓
Ingestion (Azure Data Factory / Logic Apps)
  → Document Parsing (Azure Document Intelligence / Unstructured)
    → Chunking (Fixed / Semantic / Recursive)
      → Embedding (text-embedding-3-small / ada-002)
        → Indexing (Azure AI Search / Chroma / Pinecone)
          → Vector Store
```

---

## Chunking Strategies

| Strategy | How it works | Best for |
|----------|-------------|----------|
| Fixed size | Split every N characters with overlap | Simple documents, consistent format |
| Recursive | Split by paragraphs → sentences → words | General purpose |
| Semantic | Split at topic boundaries using embeddings | Long documents with distinct sections |
| Agentic | LLM decides chunk boundaries | Complex documents, highest quality |

---

## Embedding Refresh

```
Detect document change (event grid / scheduled scan)
  → Re-chunk changed document
    → Re-embed chunks
      → Update vector index (delete old, insert new)
```

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Chunk size | 256 / 512 / 1024 tokens | 512 tokens (balance context vs precision) |
| Overlap | 0 / 10% / 20% | 10% (maintains context across chunks) |
| Embedding model | text-embedding-3-small / 3-large | text-embedding-3-small (cost/quality) |
| Index refresh | Full rebuild / incremental | Incremental (faster, less expensive) |
| Document formats | PDF / DOCX / HTML / Markdown | Support all, normalize to Markdown |

---

## References

- [Azure AI Search data ingestion](https://learn.microsoft.com/en-us/azure/search/search-howto-load-search-index)
- [Chunking strategies for RAG](https://www.pinecone.io/learn/chunking-strategies/)
