# Guardrails & Safety Pattern

## Overview

Multi-layer safety system that validates inputs and outputs, enforces policies, and prevents misuse.

---

## Layers

```
User Input
  ↓
Layer 1 — Input Guard: validate length, detect injection, check deny list
Layer 2 — Auth Guard: authenticate user, check rate limit, verify quota
Layer 3 — Content Safety: scan for toxicity, hate, violence, self-harm
Layer 4 — PII Redaction: detect and redact sensitive data
  ↓
LLM
  ↓
Layer 5 — Output Guard: validate format, check for hallucinations
Layer 6 — Policy Guard: enforce business rules, compliance checks
Layer 7 — Audit Log: record full interaction for compliance
  ↓
Response
```

---

## Guard Types

| Guard | What it blocks | Provider |
|-------|---------------|----------|
| Prompt injection | System override attempts | Custom NLP classifier |
| Toxic content | Hate, violence, sexual | Azure AI Content Safety |
| PII | Emails, SSN, credit cards | Azure AI Language PII |
| Hallucination | Ungrounded statements | LLM-as-judge |
| Policy violation | Off-topic, banned topics | Custom classifier |
| Rate limit | Abuse, scraping | API Gateway |

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Block vs flag | Hard block / soft flag / escalate | Flag first, block on repeat |
| Latency budget | Sync / async | Sync for content safety (<200ms), async for audit |
| Tuning | Fixed rules / ML-based | ML-based with human-in-the-loop tuning |

---

## References

- [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/)
- [RAI Impact Assessment template](https://learn.microsoft.com/en-us/assessments/azure-rai/)
