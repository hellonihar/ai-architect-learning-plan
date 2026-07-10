"""
ReAct (Reasoning + Acting) agent implementation.

Interleaves reasoning with tool calls for complex tasks.
"""

from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TOOLS = {
    "search": lambda q: f"Results for: {q}",
    "calculator": lambda e: str(eval(e)),
}


REACT_SYSTEM_PROMPT = """You are a ReAct agent. Follow this loop:

1. Thought: reason about what to do
2. Action: choose a tool and provide arguments
3. Observation: see the tool result
4. Repeat until you can answer

Available tools: {tools}

Respond in this format:
Thought: <your reasoning>
Action: <tool_name>
Action Input: <arguments>
"""


def react_agent(query: str, max_steps: int = 10) -> str:
    messages = [
        {"role": "system", "content": REACT_SYSTEM_PROMPT.format(tools=list(TOOLS.keys()))},
        {"role": "user", "content": query},
    ]

    for step in range(max_steps):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0,
        )
        content = response.choices[0].message.content
        messages.append({"role": "assistant", "content": content})

        if "Final Answer:" in content:
            return content.split("Final Answer:")[-1].strip()

        if "Action:" in content:
            action_line = [l for l in content.split("\n") if l.startswith("Action:")]
            input_line = [l for l in content.split("\n") if l.startswith("Action Input:")]

            if action_line and input_line:
                action = action_line[0].replace("Action:", "").strip()
                action_input = input_line[0].replace("Action Input:", "").strip()

                if action in TOOLS:
                    result = TOOLS[action](action_input)
                    messages.append({"role": "user", "content": f"Observation: {result}"})

    return "Max steps reached."


if __name__ == "__main__":
    result = react_agent("What is 15 * 27?")
    print(f"Result: {result}")
