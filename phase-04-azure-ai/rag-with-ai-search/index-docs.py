"""
Index documents into Azure AI Search for RAG.
"""

from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
    AzureOpenAIVectorizer,
    AzureOpenAIVectorizerParameters,
)
from azure.search.documents import SearchClient
from openai import AzureOpenAI
import os

search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
search_key = os.getenv("AZURE_SEARCH_KEY")
openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
openai_key = os.getenv("AZURE_OPENAI_API_KEY")

INDEX_NAME = "rag-docs"


def create_index():
    index_client = SearchIndexClient(search_endpoint, AzureKeyCredential(search_key))

    fields = [
        SimpleField(name="id", type="Edm.String", key=True),
        SearchableField(name="title", type="Edm.String"),
        SearchableField(name="content", type="Edm.String"),
        SearchableField(
            name="content_vector",
            type="Collection(Edm.Single)",
            vector_search_dimensions=1536,
            vector_search_profile_name="vp",
        ),
    ]

    vector_search = VectorSearch(
        algorithms=[HnswAlgorithmConfiguration(name="algo")],
        profiles=[VectorSearchProfile(name="vp", algorithm_configuration_name="algo")],
    )

    index = SearchIndex(name=INDEX_NAME, fields=fields, vector_search=vector_search)
    index_client.create_or_update_index(index)
    print(f"Index '{INDEX_NAME}' created/updated.")


def index_documents():
    openai_client = AzureOpenAI(
        api_key=openai_key,
        api_version="2024-10-01-preview",
        azure_endpoint=openai_endpoint,
    )

    search_client = SearchClient(search_endpoint, INDEX_NAME, AzureKeyCredential(search_key))

    documents = [
        {
            "id": "1",
            "title": "Introduction to RAG",
            "content": "Retrieval-Augmented Generation (RAG) combines retrieval from a knowledge base with LLM generation to produce grounded, accurate responses.",
        },
        {
            "id": "2",
            "title": "Azure AI Search",
            "content": "Azure AI Search provides hybrid vector and keyword search for enterprise RAG applications.",
        },
    ]

    for doc in documents:
        resp = openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=doc["content"],
        )
        doc["content_vector"] = resp.data[0].embedding

    result = search_client.upload_documents(documents)
    print(f"Indexed {len(result)} documents.")


if __name__ == "__main__":
    create_index()
    index_documents()
