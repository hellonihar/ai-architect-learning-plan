"""
Deploy a fine-tuned model to an Azure OpenAI endpoint.
"""

from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-10-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)


def deploy_model(fine_tuned_model: str, deployment_name: str):
    response = client.deployments.create(
        model=fine_tuned_model,
        deployment_name=deployment_name,
        scale_settings={"scale_type": "standard"},
    )
    print(f"Deployment created: {response.id}")
    return response


def test_deployment(deployment_name: str):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a banking assistant."},
            {"role": "user", "content": "What is my account balance?"},
        ],
    )
    print(f"Response: {response.choices[0].message.content}")


if __name__ == "__main__":
    FINE_TUNED_MODEL = "gpt-4o-mini-ft-2024-..."  # from submit-job.py output
    DEPLOYMENT_NAME = "my-fine-tuned-model"

    deploy_model(FINE_TUNED_MODEL, DEPLOYMENT_NAME)
    test_deployment(DEPLOYMENT_NAME)
