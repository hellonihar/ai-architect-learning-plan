"""
Structured output prompting example.

Requests JSON responses for reliable programmatic consumption.
"""

from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """Extract information from text and return valid JSON."""

USER_PROMPT = """Extract the following fields from the invoice text as JSON:
- "invoice_number": string
- "date": string (YYYY-MM-DD)
- "total": number
- "line_items": array of { "description": string, "amount": number }

Invoice text:
INV-2024-001
Date: March 15, 2024
Items:
  - Consulting services: $2,500.00
  - Software license: $899.00
Total: $3,399.00
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT},
    ],
    response_format={"type": "json_object"},
    temperature=0,
)

result = json.loads(response.choices[0].message.content)
print(json.dumps(result, indent=2))
