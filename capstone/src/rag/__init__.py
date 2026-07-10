"""
RAG module for capstone — handles document retrieval and context building.
"""

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Retriever:
    def __init__(self, vector_store: str = "azure_ai_search"):
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 3) -> list[str]:
        """Retrieve relevant documents."""
        return [f"Document {i} about {query}" for i in range(top_k)]


class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()

    def answer(self, query: str) -> str:
        docs = self.retriever.retrieve(query)
        context = "\n\n".join(docs)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Answer based on the context. Cite sources."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"},
            ],
            temperature=0,
        )
        return response.choices[0].message.content
