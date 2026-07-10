# AI Expert Architect — Learning Plan

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![Azure AI](https://img.shields.io/badge/Azure-AI%20Foundry-blueviolet)](https://learn.microsoft.com/en-us/azure/ai-studio/)

**Background:** Senior Architect, low-code workflow (Power Platform, Mendix, OutSystems, etc.)  
**Goal:** Transition to AI Expert Architect  
**Audience:** You — read each page, do the exercises, build the projects.

---

## Repository Structure

```
.
├── phase-01-foundations/       # ML, Deep Learning, NLP notebooks
├── phase-02-genai/             # Prompt engineering, RAG scripts
├── phase-03-architecture/      # Agentic systems, enterprise patterns, eval
├── phase-04-azure-ai/          # Azure deployment, fine-tuning, AI Search
├── phase-05-advanced/          # Security, research papers
├── capstone/                   # End-to-end AI solution project
├── docs/                       # Architecture docs, ADRs, cheatsheets
├── templates/                  # Reusable scaffolds
├── shared/                     # Reusable Python modules
└── .github/workflows/          # CI/CD pipelines
```

---

## Timeline

| Phase | Focus | Duration |
|-------|-------|----------|
| 1 | AI/ML Foundations | Weeks 1–3 |
| 2 | Generative AI & LLMs | Weeks 4–6 |
| 3 | AI Architecture Patterns | Weeks 7–9 |
| 4 | Applied AI on Azure | Weeks 10–12 |
| 5 | Expert Level (Ongoing) | Continuous |

---

## Phase 1 — AI/ML Foundations (Weeks 1–3)

| Week | Topic | What to do | Code |
|------|-------|------------|------|
| 1 | Machine Learning basics | Read [Microsoft ML for Beginners](https://github.com/microsoft/ML-For-Beginners) (first 6 lessons) | `phase-01-foundations/01-ml-basics.ipynb` |
| 2 | Deep Learning essentials | Read [fast.ai Practical Deep Learning](https://course.fast.ai/) — Lessons 1–4 | `phase-01-foundations/02-deep-learning.ipynb` |
| 3 | NLP fundamentals | Read [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) — Chapters 1–4 | `phase-01-foundations/03-nlp-transformers.ipynb` |

**Milestone:** *Explain to a peer* what a transformer is and how self-attention works.

---

## Phase 2 — Generative AI & LLMs (Weeks 4–6)

| Week | Topic | What to do | Code |
|------|-------|------------|------|
| 4 | LLM architecture & capabilities | Understand context window, temperature, top-p, system prompt, tool use | — |
| 5 | Prompt Engineering | Complete [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) | `phase-02-genai/01-prompt-engineering/` |
| 6 | RAG (Retrieval-Augmented Generation) | Study patterns: naive RAG, advanced RAG, agentic RAG | `phase-02-genai/02-rag/` |

**Milestone:** *Build* a console app that answers questions from a PDF using RAG.

---

## Phase 3 — AI Architecture Patterns (Weeks 7–9)

| Week | Topic | What to do | Code |
|------|-------|------------|------|
| 7 | Agentic systems | ReAct, multi-agent orchestration, tool calling | `phase-03-architecture/01-agentic-systems/` |
| 8 | Enterprise AI architecture | AI Gateway, prompt management, caching, guardrails | `phase-03-architecture/02-enterprise-patterns/` |
| 9 | Evaluation & Quality | LLM-as-judge, automated metrics, A/B testing | `phase-03-architecture/03-evaluation/` |

**Milestone:** *Design* an architecture for an enterprise AI assistant (multi-agent, RAG, guardrails, eval).

---

## Phase 4 — Applied AI on Azure (Weeks 10–12)

| Week | Topic | What to do | Code |
|------|-------|------------|------|
| 10 | Azure AI Foundry deep-dive | Deploy models, create projects, manage RAI policy | `phase-04-azure-ai/deploy-model/` |
| 11 | Fine-tuning & customization | Fine-tune a GPT-4o model on custom data | `phase-04-azure-ai/fine-tuning/` |
| 12 | Capstone project | End-to-end AI solution with CI/CD, monitoring, eval | `capstone/` |

**Milestone:** *Deliver* a full enterprise AI solution with CI/CD, monitoring, and evaluation.

---

## Phase 5 — Expert Level (Ongoing)

| Area | Resources |
|------|-----------|
| Responsible AI | Microsoft RAI Impact Assessment, content filtering, fairness |
| Cost optimization | Token tracking, caching strategies, prompt compression |
| Advanced agent patterns | Planning agents, reflection, tool-use recursion, human-in-the-loop |
| AI security | Prompt injection, data exfiltration prevention, least-privilege |
| Research papers | [The Prompt Report](https://arxiv.org/abs/2406.06608), [AgentLab](https://arxiv.org/abs/2501.08127), [RAG Survey](https://arxiv.org/abs/2312.10997) |

---

## Key Mindset Shifts

| Low-code background | AI Architect direction |
|---------------------|------------------------|
| Drag-and-drop flows | Code-first orchestration (Python, YAML, Semantic Kernel) |
| Managed connectors | API design, tool creation, custom connectors |
| Platform constraints | Model selection, cost/quality/latency trade-offs |
| Visual debugging | Logging, tracing, eval-driven iteration |
| Vendor lock-in accepted | Multi-model strategy, abstraction layers |

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/YOUR_USER/ai-architect-learning-plan
cd ai-architect-learning-plan

# Create environment
python -m venv .venv
.venv\Scripts\Activate   # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Launch notebooks
jupyter notebook
```

---

## Key Resources

- [Learn Microsoft AI](https://learn.microsoft.com/en-us/ai/)
- [Azure AI Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)
- [OpenAI Platform docs](https://platform.openai.com/docs)
- [Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- [LangChain / LangGraph docs](https://docs.langchain.com/)
- [OpenCode — AI tooling](https://opencode.ai)

---

*Start with Phase 1, build the milestone projects, and revisit as skills grow.*
