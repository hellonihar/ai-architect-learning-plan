# Multi-Modal Pipeline Pattern

## Overview

Process and reason across text, images, audio, and documents using multi-modal models like GPT-4o.

---

## Architecture

```
Input
  ├── Text → preprocess (clean, chunk)
  ├── Image → preprocess (resize, OCR if needed)
  ├── Audio → transcribe (Whisper) → text
  └── Document → parse (Azure Document Intelligence) → structured text
       ↓
Multi-Modal Model (GPT-4o / GPT-4o-audio-preview)
  → Structured Output (JSON)
  → Response
```

---

## Input Types & Processing

| Type | Processing | Model | Typical Latency |
|------|-----------|-------|-----------------|
| Text | Tokenization, chunking | GPT-4o | <1s |
| Image | Resize to <20MB, base64 encode | GPT-4o vision | 2–5s |
| Audio (short) | Direct audio input | GPT-4o-audio | 1–3s |
| Audio (long) | Whisper transcription → text | Whisper + GPT-4o | 5–30s |
| PDF/DOCX | Document Intelligence → markdown | DocIntel + GPT-4o | 5–20s |

---

## Design Decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Image sizing | Original / resize to 1024px | Resize to 1024px (cheaper, faster) |
| Audio path | Direct / transcribe first | Direct for short (<1m), transcribe for long |
| Document parsing | Azure DocIntel / Unstructured.io / LlamaParse | Azure DocIntel (enterprise) |
| Fallback | Text-only model if multi-modal unavailable | Route to GPT-4o-mini with extracted text only |

---

## Cost Considerations

| Input | Tokens / cost | Note |
|-------|--------------|------|
| Text only | Standard token pricing | ~$2.50/1M input tokens |
| Image (1024px) | ~255 tokens per image | Fixed cost per image |
| Audio (1 min) | ~960 tokens | GPT-4o-audio pricing |
| Document (10 pages) | ~3000 tokens | After parsing to text |

---

## References

- [GPT-4o vision guide](https://platform.openai.com/docs/guides/vision)
- [Azure Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
