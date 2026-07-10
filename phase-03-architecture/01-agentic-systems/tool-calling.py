"""
Tool calling with OpenAI function calling.

Defines and invokes tools from an LLM.
"""

from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Send an email to a recipient",
            "parameters": {
                "type": "object",
                "properties": {
                    "to": {"type": "string", "description": "Email address"},
                    "subject": {"type": "string"},
                    "body": {"type": "string"},
                },
                "required": ["to", "subject", "body"],
            },
        },
    },
]


def get_weather(location: str, unit: str = "celsius") -> str:
    return f"The weather in {location} is 22° {unit}."


def send_email(to: str, subject: str, body: str) -> str:
    return f"Email sent to {to} with subject '{subject}'."


def run_conversation(user_input: str):
    messages = [{"role": "user", "content": user_input}]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    msg = response.choices[0].message
    messages.append(msg)

    if msg.tool_calls:
        for tc in msg.tool_calls:
            args = json.loads(tc.function.arguments)
            if tc.function.name == "get_weather":
                result = get_weather(**args)
            elif tc.function.name == "send_email":
                result = send_email(**args)
            else:
                result = "Unknown tool."

            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result,
            })

        final = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        return final.choices[0].message.content

    return msg.content


if __name__ == "__main__":
    print(run_conversation("What is the weather in Tokyo?"))
