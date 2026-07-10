"""
Shared data models used across phases.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Message:
    role: str  # system, user, assistant, tool
    content: str
    tool_call_id: Optional[str] = None


@dataclass
class Conversation:
    messages: list[Message] = field(default_factory=list)

    def add(self, role: str, content: str):
        self.messages.append(Message(role=role, content=content))

    def to_openai_format(self) -> list[dict]:
        return [
            {"role": m.role, "content": m.content, **({"tool_call_id": m.tool_call_id} if m.tool_call_id else {})}
            for m in self.messages
        ]


@dataclass
class EvalResult:
    accuracy: float = 0.0
    faithfulness: float = 0.0
    relevance: float = 0.0

    @property
    def average(self) -> float:
        return (self.accuracy + self.faithfulness + self.relevance) / 3

    @property
    def passed(self, threshold: float = 4.0) -> bool:
        return self.average >= threshold
