"""
Capstone orchestrator — routes queries to the right agent.
"""

import json
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class SupervisorAgent:
    def __init__(self):
        self.agents = {
            "rag": RAGAgent(),
            "code": CodeAgent(),
            "general": GeneralAgent(),
        }

    def classify(self, query: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Classify the query as 'rag', 'code', or 'general'. Return only the label."},
                {"role": "user", "content": query},
            ],
            temperature=0,
        )
        return response.choices[0].message.content.strip()

    def run(self, query: str) -> str:
        agent_type = self.classify(query)
        agent = self.agents.get(agent_type, self.agents["general"])
        return agent.run(query)


class RAGAgent:
    def run(self, query: str) -> str:
        return f"[RAG Agent] Answer for: {query}"


class CodeAgent:
    def run(self, query: str) -> str:
        return f"[Code Agent] Code for: {query}"


class GeneralAgent:
    def run(self, query: str) -> str:
        return f"[General Agent] Response for: {query}"
