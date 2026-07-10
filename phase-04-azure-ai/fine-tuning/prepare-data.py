"""
Prepare training data for fine-tuning.

Converts raw data into the JSONL format required by Azure OpenAI.
"""

import json


def prepare_conversation_data(input_file: str, output_file: str):
    """
    Converts a list of conversations to fine-tuning JSONL format.

    Input format (JSON):
    [
        {
            "system": "System prompt",
            "messages": [
                {"role": "user", "content": "User message"},
                {"role": "assistant", "content": "Assistant message"}
            ]
        }
    ]
    """

    with open(input_file, "r", encoding="utf-8") as f:
        conversations = json.load(f)

    with open(output_file, "w", encoding="utf-8") as f:
        for conv in conversations:
            entry = {"messages": [
                {"role": "system", "content": conv["system"]},
                *conv["messages"],
            ]}
            f.write(json.dumps(entry) + "\n")

    print(f"Prepared {len(conversations)} examples → {output_file}")


if __name__ == "__main__":
    sample_data = [
        {
            "system": "You are a helpful AI assistant for a bank.",
            "messages": [
                {"role": "user", "content": "What is my account balance?"},
                {"role": "assistant", "content": "Your current account balance is $1,234.56 as of today."},
            ],
        },
        {
            "system": "You are a helpful AI assistant for a bank.",
            "messages": [
                {"role": "user", "content": "How do I transfer money?"},
                {"role": "assistant", "content": "To transfer money, log in to online banking, select 'Transfers', choose the accounts, enter the amount, and confirm."},
            ],
        },
    ]

    with open("raw_data.json", "w") as f:
        json.dump(sample_data, f, indent=2)

    prepare_conversation_data("raw_data.json", "training_data.jsonl")
