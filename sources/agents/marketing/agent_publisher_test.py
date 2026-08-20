import os

from agent_publisher import execute_marketing_publisher


def test_marketing_publisher():
    os.environ["AI_MODELS_KEYS_JSON"] = (
        '{ "https://api.mistral.ai/v1": "<!--API Key HERE-->" }'
    )
    os.environ["SOCIAL_SECRETS_KEY"] = (
        '{ "Generic": { "api_endpoint": "http://localhost", "target_account_handle": "Generic@Account" } }'
    )
    PROJECT_NAME = "membership-hub"
    execute_marketing_publisher(args={
        "idea": PROJECT_NAME,
    }, language="Vietnamese")


if __name__ == "__main__":
    test_marketing_publisher()
