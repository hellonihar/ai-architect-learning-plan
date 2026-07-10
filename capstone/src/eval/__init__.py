"""
Evaluation module for capstone — quality scoring and monitoring.
"""

from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Evaluator:
    def __init__(self, threshold: float = 4.0):
        self.threshold = threshold

    def score(self, question: str, context: str, response: str) -> dict:
        eval_prompt = f"""
        Evaluate this response (1-5 scale):
        1. accuracy: Is it factually correct?
        2. faithfulness: Does it stay true to the context?
        3. relevance: Does it address the question?

        Question: {question}
        Context: {context}
        Response: {response}

        Return JSON: {{"accuracy": int, "faithfulness": int, "relevance": int}}
        """
        result = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": eval_prompt.strip()}],
            response_format={"type": "json_object"},
            temperature=0,
        )
        scores = json.loads(result.choices[0].message.content)
        scores["average"] = sum(scores.values()) / len(scores)
        scores["passed"] = scores["average"] >= self.threshold
        return scores

    def should_return(self, scores: dict) -> bool:
        return scores.get("passed", False)
