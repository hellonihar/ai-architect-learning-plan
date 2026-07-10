"""
Automated evaluation pipeline for AI responses.

Supports batch evaluation with LLM-as-judge, metrics, and reporting.
"""

import json
import csv
from dataclasses import dataclass, field
from datetime import datetime
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@dataclass
class EvalCase:
    question: str
    context: str
    expected: str
    actual: str = ""
    scores: dict = field(default_factory=dict)


class EvalPipeline:
    def __init__(self):
        self.cases: list[EvalCase] = []

    def add_case(self, question: str, context: str, expected: str):
        self.cases.append(EvalCase(question=question, context=context, expected=expected))

    def generate_responses(self, model: str = "gpt-4o-mini"):
        for case in self.cases:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Answer based on the context."},
                    {"role": "user", "content": f"Context: {case.context}\n\nQuestion: {case.question}"},
                ],
                temperature=0,
            )
            case.actual = response.choices[0].message.content

    def evaluate(self):
        for case in self.cases:
            eval_prompt = f"""
            Score the following response (1-5):
            - accuracy: Is it factually correct?
            - faithfulness: Does it stay true to the context?

            Context: {case.context}
            Question: {case.question}
            Expected: {case.expected}
            Response: {case.actual}

            Return JSON: {{"accuracy": int, "faithfulness": int}}
            """
            result = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": eval_prompt.strip()}],
                response_format={"type": "json_object"},
                temperature=0,
            )
            case.scores = json.loads(result.choices[0].message.content)

    def report(self) -> dict:
        if not self.cases:
            return {"error": "No cases"}

        avg_accuracy = sum(c.scores.get("accuracy", 0) for c in self.cases) / len(self.cases)
        avg_faithfulness = sum(c.scores.get("faithfulness", 0) for c in self.cases) / len(self.cases)

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "total_cases": len(self.cases),
            "avg_accuracy": round(avg_accuracy, 2),
            "avg_faithfulness": round(avg_faithfulness, 2),
            "pass_rate": sum(1 for c in self.cases if c.scores.get("accuracy", 0) >= 4) / len(self.cases),
        }

    def export_csv(self, path: str):
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["question", "expected", "actual", "accuracy", "faithfulness"])
            for case in self.cases:
                writer.writerow([
                    case.question, case.expected, case.actual,
                    case.scores.get("accuracy", ""),
                    case.scores.get("faithfulness", ""),
                ])


if __name__ == "__main__":
    pipeline = EvalPipeline()
    pipeline.add_case(
        question="What is RAG?",
        context="RAG combines retrieval with generation.",
        expected="RAG is a technique that combines retrieval and generation.",
    )
    pipeline.generate_responses()
    pipeline.evaluate()
    print(json.dumps(pipeline.report(), indent=2))
