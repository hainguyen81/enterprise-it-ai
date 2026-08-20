import os

from agent_planner import execute_marketing_planner


def test_marketing_planner():
    os.environ["AI_MODELS_KEYS_JSON"] = (
        '{ "https://api.mistral.ai/v1": "ra0JshuU715ZOjcqtRsHmB5sfEriaptM" }'
    )
    PROJECT_NAME = "membership-hub"
    execute_marketing_planner(args={
        "idea": PROJECT_NAME,
    }, language="Vietnamese")


if __name__ == "__main__":
    test_marketing_planner()
