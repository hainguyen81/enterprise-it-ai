import os

from agent_idea_generator import execute_idea_generator


def test_idea_generation():
    AI_BASE_URL = "https://openrouter.ai/api/v1"
    AI_API_KEY = (
        "sk-or-v1-*******"
    )
    os.environ["AI_MODELS_KEYS_JSON"] = (
        f"{{ \"{AI_BASE_URL}\": \"{AI_API_KEY}\" }}"
    )
    execute_idea_generator(
        args={
            "quantity": 3,
        },
        language="Vietnamese",
    )

if __name__ == "__main__":
    test_idea_generation()
