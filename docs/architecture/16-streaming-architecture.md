# Streaming Architecture Pattern

## Overview

Stream LLM responses token-by-token to improve perceived latency and enable real-time UX patterns like typewriter effects.

---

## Architecture

```
Client (Browser / Mobile)
  ↓  SSE / WebSocket
API Gateway (FastAPI / Azure API Management)
  ↓  Async stream
Orchestrator (LangGraph / custom)
  ↓  Stream events
LLM Provider (OpenAI / Azure OpenAI)
  → Token stream → Chunk → Client
       │
       └── Also: log tokens, check guardrails incrementally
```

---

## Streaming Approaches

| Approach | Protocol | Client Support | Complexity |
|----------|----------|---------------|------------|
| Server-Sent Events | HTTP (text/event-stream) | Native EventSource API | Low |
| WebSocket | Bidirectional TCP | WebSocket API | Medium |
| Chunked transfer | HTTP 1.1 | XMLHttpRequest / fetch | Low |

---

## Streaming with Guardrails

```
Token stream from LLM
  → Accumulate buffer (e.g., 50 chars)
    → Check content safety (streaming safe / block / flag)
      → If safe: flush to client
        → If flagged: buffer, check more context
          → If blocked: send "Response blocked" to client, log
```

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Protocol | SSE / WebSocket / gRPC | SSE (simple, universal, HTTP-native) |
| Buffer size | Per-token / per-sentence / per 100ms | Per 100ms (balance UX vs guardrail accuracy) |
| Guardrail latency impact | Buffer + scan / async check | Buffer + scan (200ms delay at most) |
| Error handling | Close stream / insert error token / side channel | Close stream + client retry |

---

## Client Implementation (SSE)

```javascript
const eventSource = new EventSource('/api/chat/stream?query=' + query);
eventSource.onmessage = (event) => {
    if (event.data === '[DONE]') {
        eventSource.close();
    } else {
        appendToken(event.data);
    }
};
```

---

## References

- [OpenAI streaming API](https://platform.openai.com/docs/api-reference/streaming)
- [SSE standard (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
