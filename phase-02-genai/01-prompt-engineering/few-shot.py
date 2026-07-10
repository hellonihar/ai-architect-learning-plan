"""
Few-shot prompting example.

Provides examples to guide the model's output format and style.
"""

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = "Classify customer feedback as Positive, Negative, or Neutral."

FEW_SHOT_EXAMPLES = [
    {"role": "user", "content": "The product arrived on time and works perfectly!"},
    {"role": "assistant", "content": "Positive"},
    {"role": "user", "content": "Terrible quality, broke after one use."},
    {"role": "assistant", "content": "Negative"},
    {"role": "user", "content": "It's okay, does what it's supposed to."},
    {"role": "assistant", "content": "Neutral"},
]

NEW_FEEDBACK = "I love the design but the battery life is disappointing."

messages = [{"role": "system", "content": SYSTEM_PROMPT}]
messages.extend(FEW_SHOT_EXAMPLES)
messages.append({"role": "user", "content": NEW_FEEDBACK})

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    temperature=0,
)

print(f"Feedback: {NEW_FEEDBACK}")
print(f"Classification: {response.choices[0].message.content}")
