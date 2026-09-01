import os

from agent_csro import execute_governance_flow


def test_csro():
    AI_BASE_URL = "https://openrouter.ai/api/v1"
    AI_API_KEY = (
        "sk-or-v1-*******"
    )
    os.environ["AI_MODELS_KEYS_JSON"] = f'{{ "{AI_BASE_URL}": "{AI_API_KEY}" }}'
    PROJECT_NAME = "membership-hub"
    execute_governance_flow(args={
        "idea": PROJECT_NAME,
    }, language="Vietnamese")


if __name__ == "__main__":
    test_csro()
