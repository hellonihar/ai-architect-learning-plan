"""
Shared utility functions.
"""

import json
import time
from functools import wraps


def timer(func):
    """Decorator to measure execution time in ms."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = (time.time() - start) * 1000
        print(f"[{func.__name__}] took {elapsed:.1f}ms")
        return result
    return wrapper


def truncate(text: str, max_length: int = 500) -> str:
    """Truncate text to max_length with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def pretty_json(obj) -> str:
    """Format object as pretty-printed JSON."""
    return json.dumps(obj, indent=2, default=str)


def estimate_tokens(text: str) -> int:
    """Rough estimate of token count (4 chars per token)."""
    return len(text) // 4
