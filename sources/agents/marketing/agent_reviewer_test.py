import os

from agent_reviewer import execute_marketing_reviewer


def test_marketing_reviewer():
    os.environ["AI_MODELS_KEYS_JSON"] = (
        '{ "https://api.mistral.ai/v1": "<!--API Key HERE-->" }'
    )
    PROJECT_NAME = "membership-hub"
    execute_marketing_reviewer(args={
        "idea": PROJECT_NAME,
    }, language="Vietnamese", trigger_editor="true")


if __name__ == "__main__":
    test_marketing_reviewer()
