"""
Simple AI Gateway with routing, rate limiting, and logging.

Production: use Azure API Management or a dedicated AI Gateway.
"""

import time
import json
from dataclasses import dataclass
from typing import Optional
from openai import OpenAI
import os


@dataclass
class ModelConfig:
    name: str
    cost_per_1k_tokens: float
    latency_p95_ms: int


MODELS = {
    "fast": ModelConfig("gpt-4o-mini", 0.00015, 500),
    "default": ModelConfig("gpt-4o", 0.0025, 2000),
    "reasoning": ModelConfig("o1", 0.015, 10000),
}


class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests: list[float] = []

    def is_allowed(self) -> bool:
        now = time.time()
        self.requests = [t for t in self.requests if now - t < self.window_seconds]
        if len(self.requests) >= self.max_requests:
            return False
        self.requests.append(now)
        return True


class AIGateway:
    def __init__(self, api_key: Optional[str] = None):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.rate_limiter = RateLimiter(max_requests=100)
        self.total_cost = 0.0

    def route(self, query: str, complexity: str = "default") -> str:
        if not self.rate_limiter.is_allowed():
            return "Rate limit exceeded. Try again later."

        model = MODELS.get(complexity, MODELS["default"])

        start = time.time()
        response = self.client.chat.completions.create(
            model=model.name,
            messages=[{"role": "user", "content": query}],
        )
        elapsed = (time.time() - start) * 1000

        tokens = response.usage.total_tokens
        cost = (tokens / 1000) * model.cost_per_1k_tokens
        self.total_cost += cost

        log_entry = {
            "model": model.name,
            "tokens": tokens,
            "cost": cost,
            "latency_ms": round(elapsed),
            "complexity": complexity,
        }

        return response.choices[0].message.content


if __name__ == "__main__":
    gateway = AIGateway()
    print(gateway.route("What is AI?", complexity="fast"))
    print(f"Total cost so far: ${gateway.total_cost:.6f}")
