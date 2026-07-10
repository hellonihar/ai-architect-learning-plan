"""
Submit a fine-tuning job to Azure OpenAI.
"""

from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-10-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)


def upload_training_file(file_path: str) -> str:
    with open(file_path, "rb") as f:
        response = client.files.create(file=f, purpose="fine-tune")
    print(f"Uploaded file: {response.id}")
    return response.id


def create_fine_tune_job(training_file_id: str, model: str = "gpt-4o-mini") -> str:
    response = client.fine_tuning.jobs.create(
        training_file=training_file_id,
        model=model,
        hyperparameters={
            "n_epochs": 3,
        },
    )
    print(f"Fine-tuning job created: {response.id}")
    print(f"Status: {response.status}")
    return response.id


def monitor_job(job_id: str):
    import time
    while True:
        response = client.fine_tuning.jobs.retrieve(job_id)
        print(f"Status: {response.status}")
        if response.status in ["succeeded", "failed", "cancelled"]:
            print(f"Final status: {response.status}")
            if response.status == "succeeded":
                print(f"Fine-tuned model: {response.fine_tuned_model}")
            return response
        time.sleep(30)


if __name__ == "__main__":
    file_id = upload_training_file("training_data.jsonl")
    job_id = create_fine_tune_job(file_id, "gpt-4o-mini")
    monitor_job(job_id)
