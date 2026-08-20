import os

from agent_csro import execute_governance_flow


def test_csro():
    os.environ["AI_MODELS_KEYS_JSON"] = (
        '{ "https://api.mistral.ai/v1": "<!--API Key Here-->" }'
    )
    PROJECT_NAME = "membership-hub"
    execute_governance_flow(args={
        "idea": PROJECT_NAME,
    }, language="Vietnamese")


if __name__ == "__main__":
    test_csro()
