"""
Advanced RAG with query rewriting, hybrid search, and re-ranking.
"""

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def rewrite_query(original: str) -> str:
    """Rewrite query for better search results."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Rewrite this query for a documentation search engine. Make it concise and specific."},
            {"role": "user", "content": original},
        ],
        temperature=0,
    )
    return response.choices[0].message.content


def retrieve(query: str) -> list[str]:
    """Placeholder for hybrid vector + keyword search."""
    docs = [
        "Azure AI Foundry supports RAG patterns with AI Search.",
        "Query rewriting improves retrieval accuracy in RAG systems.",
        "Hybrid search combines dense vectors and sparse keywords.",
    ]
    return docs


def rerank(query: str, docs: list[str]) -> list[str]:
    """Simple re-ranking by relevance scoring."""
    scored = []
    for doc in docs:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Rate relevance 0-10. Return only the number."},
                {"role": "user", "content": f"Query: {query}\nDoc: {doc}"},
            ],
            temperature=0,
        )
        score = int(resp.choices[0].message.content.strip())
        scored.append((score, doc))
    return [doc for _, doc in sorted(scored, reverse=True)]


def answer(query: str) -> str:
    rewritten = rewrite_query(query)
    docs = retrieve(rewritten)
    top_docs = rerank(rewritten, docs)[:2]
    context = "\n\n".join(top_docs)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer based on the context. Cite sources."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"},
        ],
        temperature=0,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    query = "How does AI Foundry handle search?"
    print(f"Q: {query}")
    print(f"A: {answer(query)}")
