import os

from agent_writer import execute_marketing_writer


def test_marketing_writer():
    os.environ["AI_MODELS_KEYS_JSON"] = (
        '{ "https://api.mistral.ai/v1": "<!--API Key HERE-->" }'
    )
    PROJECT_NAME = "membership-hub"
    execute_marketing_writer(args={
        "idea": PROJECT_NAME,
    }, language="Vietnamese")


if __name__ == "__main__":
    test_marketing_writer()
