import os

from agent_planner_editor import execute_marketing_planner_editor


def test_marketing_planner_editor():
    os.environ["AI_MODELS_KEYS_JSON"] = (
        '{ "https://api.mistral.ai/v1": "<!--API Key HERE-->" }'
    )
    PROJECT_NAME = "membership-hub"
    execute_marketing_planner_editor(
        args={
            "idea": PROJECT_NAME,
        },
        language="Vietnamese",
    )


if __name__ == "__main__":
    test_marketing_planner_editor()
