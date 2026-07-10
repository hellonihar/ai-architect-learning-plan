"""
Naive RAG implementation.

Simple single-shot retrieval + generation.
"""

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DOCUMENTS = [
    "Azure AI Foundry is a unified platform for building AI solutions.",
    "RAG stands for Retrieval-Augmented Generation.",
    "GPT-4o supports multimodal inputs including text and images.",
]


def search(query: str) -> str:
    """Simple keyword-based retrieval (replace with vector search)."""
    query_lower = query.lower()
    for doc in DOCUMENTS:
        if any(word in doc.lower() for word in query_lower.split()):
            return doc
    return "No relevant documents found."


def answer(query: str) -> str:
    context = search(query)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer using the provided context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"},
        ],
        temperature=0,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    query = "What is RAG?"
    print(f"Q: {query}")
    print(f"A: {answer(query)}")
