"""
Query Azure AI Search with hybrid search and generate responses.
"""

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from openai import AzureOpenAI
import os

search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
search_key = os.getenv("AZURE_SEARCH_KEY")
openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
openai_key = os.getenv("AZURE_OPENAI_API_KEY")

INDEX_NAME = "rag-docs"


def hybrid_search(query: str, top: int = 3):
    openai_client = AzureOpenAI(
        api_key=openai_key,
        api_version="2024-10-01-preview",
        azure_endpoint=openai_endpoint,
    )
    search_client = SearchClient(search_endpoint, INDEX_NAME, AzureKeyCredential(search_key))

    query_embedding = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=query,
    ).data[0].embedding

    results = search_client.search(
        search_text=query,
        vector_queries=[{
            "kind": "vector",
            "vector": query_embedding,
            "fields": "content_vector",
            "k": top,
        }],
        top=top,
    )

    return [{"title": r["title"], "content": r["content"], "score": r["@search.score"]} for r in results]


def answer(query: str):
    docs = hybrid_search(query)
    context = "\n\n".join(d["content"] for d in docs)

    openai_client = AzureOpenAI(
        api_key=openai_key,
        api_version="2024-10-01-preview",
        azure_endpoint=openai_endpoint,
    )

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer based on the provided context. Cite sources."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"},
        ],
        temperature=0,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    q = "What is RAG?"
    print(f"Q: {q}")
    print(f"A: {answer(q)}")
