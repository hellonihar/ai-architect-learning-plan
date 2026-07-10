# Capstone Architecture

## System Design

```
┌─────────────┐     ┌─────────────┐     ┌───────────────┐
│   Client    │────▶│ API Gateway │────▶│  Supervisor   │
│  (Web/API)  │     │ (FastAPI)   │     │   (Agent)     │
└─────────────┘     └─────────────┘     └───────┬───────┘
                                                 │
                    ┌────────────────────────────┼────────────────────────────┐
                    │                            │                            │
              ┌─────▼──────┐            ┌────────▼───────┐         ┌─────────▼──────┐
              │ RAG Agent  │            │   Code Agent   │         │ General Agent │
              │ (Azure AI  │            │ (GPT-4o-mini)  │         │ (GPT-4o-mini) │
              │  Search)   │            └────────────────┘         └────────────────┘
              └─────┬──────┘
                    │
              ┌─────▼──────┐
              │ Vector DB  │
              │ (AI Search)│
              └────────────┘
```

## Data Flow

1. User sends query → API Gateway validates → routes to Supervisor
2. Supervisor classifies query type → delegates to appropriate agent
3. Agent uses tools (search, code execution) → returns result
4. Supervisor aggregates → passes to Eval check
5. Eval scores response → if pass, return to user; if fail, retry or escalate

## Deployment

- **Azure OpenAI**: GPT-4o (reasoning), GPT-4o-mini (fast/cheap)
- **Azure AI Search**: Document indexing + hybrid search
- **Azure App Service**: API host (FastAPI)
- **Azure AI Content Safety**: Guardrails
- **Application Insights**: Monitoring

## Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Orchestration framework | LangGraph | Flexible agent workflows |
| Vector store | Azure AI Search | Native Azure + hybrid search |
| API framework | FastAPI | Async, auto-docs, performant |
| Deployment | Bicep + GitHub Actions | IaC + CI/CD |
