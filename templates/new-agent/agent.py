"""
Template: New AI Agent

Copy this directory to create a new agent.
"""

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class MyAgent:
    def __init__(self, name: str = "MyAgent"):
        self.name = name
        self.system_prompt = f"You are {name}, a specialized AI agent."

    def run(self, input_text: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": input_text},
            ],
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    agent = MyAgent()
    print(agent.run("Hello!"))
