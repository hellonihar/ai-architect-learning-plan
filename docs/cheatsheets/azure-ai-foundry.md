# Azure AI Foundry Cheatsheet

## Quick Commands

```powershell
# Login to Azure
az login

# List AI Foundry projects
az ml workspace list

# Deploy a model
az ml model create --name gpt-4o --path ./model
az ml online-endpoint create --name my-endpoint
az ml online-deployment create --endpoint my-endpoint --model gpt-4o
```

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| Hub | Top-level resource, manages compute + connections |
| Project | Isolated workspace for experimentation/deployment |
| Model Catalog | Azure OpenAI, Meta, Mistral, Cohere, Hugging Face |
| Deployment | Model + instance + endpoint |
| RAI Policy | Content filters, safety settings per deployment |

---

## Model Selection

| Model | Best For |
|-------|----------|
| GPT-4o | General purpose, vision, multilingual |
| GPT-4o-mini | Cost-sensitive, high volume |
| o1 / o3 | Complex reasoning, math, code |
| embedding-3 | Embeddings for search/RAG |
| Dall-E-3 | Image generation |

---

## Useful Links

- [Azure AI Foundry portal](https://ai.azure.com)
- [Azure OpenAI pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/)
- [RAI Content Filtering docs](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/)
