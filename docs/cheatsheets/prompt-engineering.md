# Prompt Engineering Cheatsheet

## Core Techniques

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| System prompt | Set role, tone, constraints | Every conversation |
| Few-shot | Provide examples in the prompt | Classification, formatting |
| Chain-of-thought | "Let's think step by step" | Reasoning, math, logic |
| Structured output | Request JSON/XML explicitly | API integration |
| Role prompting | "You are a senior architect" | Domain-specific tasks |

---

## System Prompt Template

```
You are a [role]. Your task is to [task].

Rules:
- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

Format your response as [format].
```

---

## Structured Output Example

```
Extract the following fields from the text as JSON:
- "name": string
- "date": string (YYYY-MM-DD)
- "amount": number
- "category": string

Text: [text]

JSON:
```

---

## Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| Vague instructions | Be specific about format, length, tone |
| Overloading context | Keep prompt concise, use retrieval for long docs |
| Ignoring negative prompts | Explicitly say what NOT to do |
| No output validation | Parse and validate structured responses |
