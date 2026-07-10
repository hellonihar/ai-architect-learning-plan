"""
LLM-as-judge evaluation pipeline.

Uses an LLM to evaluate the quality of another LLM's responses.
"""

from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


EVALUATION_CRITERIA = {
    "accuracy": "Is the answer factually correct based on the context?",
    "relevance": "Does the answer directly address the question?",
    "completeness": "Does the answer cover all aspects of the question?",
    "conciseness": "Is the answer concise without unnecessary information?",
}


def evaluate_response(question: str, context: str, response: str) -> dict:
    scores = {}

    for criterion, description in EVALUATION_CRITERIA.items():
        eval_prompt = f"""
        Evaluate the following response on "{criterion}" ({description}).

        Question: {question}
        Context: {context}
        Response: {response}

        Score from 1-5 where:
        1 = Very poor
        2 = Poor
        3 = Acceptable
        4 = Good
        5 = Excellent

        Return only the number.
        """

        result = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": eval_prompt.strip()}],
            temperature=0,
        )
        try:
            scores[criterion] = int(result.choices[0].message.content.strip())
        except ValueError:
            scores[criterion] = 0

    scores["average"] = sum(scores.values()) / len(scores)
    return scores


if __name__ == "__main__":
    question = "What is RAG?"
    context = "RAG (Retrieval-Augmented Generation) combines retrieval from a knowledge base with LLM generation."
    response = "RAG is a technique that retrieves relevant documents and uses them to generate more accurate answers."

    scores = evaluate_response(question, context, response)
    print(json.dumps(scores, indent=2))
