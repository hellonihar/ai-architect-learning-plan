"""
Multi-agent orchestrator pattern.

A supervisor delegates tasks to specialized agents.
"""

from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def research_agent(topic: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a research agent. Summarize key information about the topic concisely."},
            {"role": "user", "content": topic},
        ],
    )
    return response.choices[0].message.content


def code_agent(task: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a code agent. Write clean, working code for the task."},
            {"role": "user", "content": task},
        ],
    )
    return response.choices[0].message.content


def review_agent(content: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a review agent. Check for errors, improvements, and best practices."},
            {"role": "user", "content": f"Review this:\n{content}"},
        ],
    )
    return response.choices[0].message.content


def supervisor_orchestrator(task: str) -> dict:
    """Supervisor decomposes the task and delegates to agents."""

    decomposition = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Decompose this task into sub-tasks: research, coding, and review. Return as JSON with keys 'research', 'code', and 'review_prompt'."},
            {"role": "user", "content": task},
        ],
        response_format={"type": "json_object"},
    )
    sub_tasks = json.loads(decomposition.choices[0].message.content)

    results = {}
    if "research" in sub_tasks:
        results["research"] = research_agent(sub_tasks["research"])
    if "code" in sub_tasks:
        code_result = code_agent(sub_tasks["code"])
        results["code"] = code_result
        if "review_prompt" in sub_tasks:
            results["review"] = review_agent(code_result)

    return results


if __name__ == "__main__":
    task = "Write a Python function to calculate Fibonacci numbers and explain how it works."
    results = supervisor_orchestrator(task)
    for agent, output in results.items():
        print(f"\n=== {agent.upper()} ===")
        print(output[:200])
