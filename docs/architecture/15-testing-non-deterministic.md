# Testing Non-Deterministic Systems Pattern

## Overview

Strategies for testing AI systems where the same input can produce different outputs, requiring shift from assert-equals to assert-quality.

---

## Testing Pyramid for AI

```
            ╱  Human Eval  ╲        ← Expert review, A/B tests
           ╱  End-to-End    ╲       ← Full system integration tests
          ╱  Quality Eval    ╲      ← LLM-as-judge, faithfulness, relevance
         ╱  Integration       ╲     ← Tool calling, RAG retrieval, API contracts
        ╱  Unit Tests          ╲    ← Schema validation, guardrails, prompt format
```

---

## Test Types

| Type | What it tests | Tool / Method |
|------|--------------|---------------|
| **Schema test** | Structured output matches expected schema | Pydantic, JSON Schema |
| **Guardrail test** | Harmful inputs are blocked, safe inputs pass | Assert-blocked / assert-passed |
| **Tool call test** | Agent selects correct tool with valid args | Mock tools, assert calls |
| **Eval test** | Response meets quality threshold | LLM-as-judge >= 4/5 |
| **Regression test** | Key scenarios maintain quality over time | Eval pipeline on saved dataset |
| **Human eval** | Subject matter expert reviews samples | Labeling tool, scoring rubric |

---

## Golden Dataset

```
Maintain a versioned dataset of 50–200 test cases:
  - query: "What is our return policy?"
  - expected: "30-day return from date of purchase"
  - context: "Return policy doc chunk"
  - criteria: {"accuracy": >=4, "faithfulness": >=4}
```

Run against every prompt/model change. Fail CI if average drops below threshold.

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Eval dataset size | 20 / 100 / 500 | 100 (balance coverage vs cost) |
| Threshold | 3.5 / 4.0 / 4.5 | 4.0 (good quality, achievable) |
| Test frequency | Per commit / nightly / weekly | Per commit (CI gate), nightly (full suite) |
| Human eval | In-house / outsourced / automated only | In-house for domain accuracy |

---

## References

- [Evaluating LLM systems (LangChain)](https://docs.langchain.com/docs/guides/evaluation/)
- [Testing AI applications (DeepEval)](https://docs.confident-ai.com/docs/testing-intro)
