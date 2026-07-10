# Capstone Project: Enterprise AI Assistant

## Objective

Build an end-to-end enterprise AI assistant that answers questions from company documentation using multi-agent RAG.

## Requirements

### Functional

1. **Multi-turn chat** — Users can ask follow-up questions
2. **RAG on internal docs** — Answers grounded in indexed documentation
3. **Multi-agent orchestration** — Supervisor delegates to specialist agents
4. **Citation support** — Every answer cites source documents
5. **Evaluation pipeline** — Automated quality scoring of responses

### Non-Functional

1. **Latency** — P95 < 5s for simple queries
2. **Cost** — < $0.01 per query average
3. **Security** — Prompt injection detection, rate limiting
4. **Observability** — Log all queries, responses, costs, latencies
5. **RAI compliance** — Content filtering, PII redaction

## Architecture

```
User → API Gateway → Supervisor Agent
  → Router (classify query)
    ├── RAG Agent (knowledge questions)
    ├── Code Agent (code generation)
    └── General Agent (chat/FAQ)
  → Aggregator → Eval Check → Response
```

## Deliverables

| Artifact | Description |
|----------|-------------|
| `src/` | Application code (orchestrator, tools, RAG, eval) |
| `infra/` | Bicep templates for Azure deployment |
| `tests/` | Unit and integration tests |
| `architecture.md` | Architecture decision record |
| `README.md` | Setup and usage instructions |

## Evaluation Criteria

1. Response accuracy (LLM-as-judge >= 4/5)
2. Faithfulness to source documents
3. Handling of multi-turn context
4. Cost and latency under targets
5. Security and RAI compliance
