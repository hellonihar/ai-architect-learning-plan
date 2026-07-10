"""
Agentic RAG — dynamic tool selection based on query type.
"""

from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TOOLS = [
    {
        "name": "search_docs",
        "description": "Search internal documentation",
        "parameters": {"query": "string"},
    },
    {
        "name": "web_search",
        "description": "Search the web for recent information",
        "parameters": {"query": "string"},
    },
    {
        "name": "calculate",
        "description": "Perform mathematical calculations",
        "parameters": {"expression": "string"},
    },
]


def search_docs(query: str) -> str:
    return f"Results for '{query}' from internal docs."


def web_search(query: str) -> str:
    return f"Web results for '{query}'."


def calculate(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


def agent_loop(query: str, max_iterations: int = 5) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant with access to tools. Decide which tool to call based on the query."},
        {"role": "user", "content": query},
    ]

    for _ in range(max_iterations):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=[{
                "type": "function",
                "function": {
                    "name": t["name"],
                    "description": t["description"],
                    "parameters": {
                        "type": "object",
                        "properties": {k: {"type": v} for k, v in t["parameters"].items()},
                        "required": list(t["parameters"].keys()),
                    },
                },
            } for t in TOOLS],
            tool_choice="auto",
        )

        msg = response.choices[0].message
        messages.append(msg)

        if not msg.tool_calls:
            return msg.content

        for tc in msg.tool_calls:
            args = json.loads(tc.function.arguments)
            if tc.function.name == "search_docs":
                result = search_docs(**args)
            elif tc.function.name == "web_search":
                result = web_search(**args)
            elif tc.function.name == "calculate":
                result = calculate(**args)
            else:
                result = "Unknown tool."

            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result,
            })

    return "Max iterations reached."


if __name__ == "__main__":
    queries = [
        "What is our company's policy on data retention?",
        "What is 2+2?",
    ]
    for q in queries:
        print(f"\nQ: {q}")
        print(f"A: {agent_loop(q)}")
