"""
Semantic caching for LLM responses.

Caches responses based on semantic similarity of queries.
"""

import hashlib
import json
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class SemanticCache:
    def __init__(self):
        self._cache: dict[str, dict] = {}

    def _embed(self, text: str) -> list[float]:
        resp = client.embeddings.create(
            model="text-embedding-3-small",
            input=text,
        )
        return resp.data[0].embedding

    def _cosine_similarity(self, a: list[float], b: list[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = sum(x * x for x in a) ** 0.5
        norm_b = sum(x * x for x in b) ** 0.5
        return dot / (norm_a * norm_b)

    def _make_key(self, query: str, system_prompt: str = "") -> str:
        raw = f"{system_prompt}||{query}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def get(self, query: str, system_prompt: str = "", threshold: float = 0.95) -> str | None:
        query_emb = self._embed(query)
        for key, entry in self._cache.items():
            similarity = self._cosine_similarity(query_emb, entry["embedding"])
            if similarity >= threshold:
                return entry["response"]
        return None

    def set(self, query: str, response: str, system_prompt: str = ""):
        key = self._make_key(query, system_prompt)
        self._cache[key] = {
            "embedding": self._embed(query),
            "response": response,
            "query": query,
        }

    @property
    def size(self) -> int:
        return len(self._cache)


if __name__ == "__main__":
    cache = SemanticCache()

    cache.set("What is RAG?", "RAG is Retrieval-Augmented Generation.")
    cached = cache.get("Explain RAG to me")
    print(f"Cached response: {cached}")
    print(f"Cache size: {cache.size}")
