"""
Tool implementations for capstone agents.
"""

import json
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def search_docs(query: str, index_name: str = "company-docs") -> str:
    """Search indexed company documentation."""
    return f"Search results for '{query}' from {index_name}."


def web_search(query: str) -> str:
    """Search the web for recent information."""
    return f"Web search results for '{query}'."


def run_code(code: str) -> str:
    """Execute Python code in a sandbox."""
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return str(exec_globals.get("result", "Code executed."))
    except Exception as e:
        return f"Error: {e}"


AVAILABLE_TOOLS = {
    "search_docs": search_docs,
    "web_search": web_search,
    "run_code": run_code,
}
