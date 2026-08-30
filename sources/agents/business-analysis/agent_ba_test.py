import os

from agent_ba import execute_ba


def test_ba_generation():
    AI_BASE_URL = "https://openrouter.ai/api/v1"
    AI_API_KEY = "sk-or-v1-*******"
    os.environ["AI_MODELS_KEYS_JSON"] = (
        f"{{ \"{AI_BASE_URL}\": \"{AI_API_KEY}\" }}"
    )
    IDEA = "idea_d066d15f9b52"
    execute_ba(
        args={
            "idea": IDEA,
        },
        language="Vietnamese",
    )

if __name__ == "__main__":
    test_ba_generation()
