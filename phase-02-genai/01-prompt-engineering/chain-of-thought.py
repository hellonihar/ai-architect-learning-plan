"""
Chain-of-Thought prompting example.

Demonstrates step-by-step reasoning for complex problems.
"""

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = "You are a helpful assistant that thinks step by step."

PROMPT = """Solve this problem step by step:

A store sells apples for $0.50 each and oranges for $0.75 each.
If a customer buys 3 apples and 2 oranges, and pays with a $10 bill,
how much change do they receive?

Let's think step by step:"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": PROMPT},
    ],
    temperature=0,
)

print(response.choices[0].message.content)
