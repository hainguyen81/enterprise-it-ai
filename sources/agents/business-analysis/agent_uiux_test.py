import os

from agent_uiux import execute_uiux


def test_uiux_generation():
    AI_BASE_URL = "https://openrouter.ai/api/v1"
    AI_API_KEY = "sk-or-v1-*******"
    os.environ["AI_MODELS_KEYS_JSON"] = (
        f"{{ \"{AI_BASE_URL}\": \"{AI_API_KEY}\" }}"
    )
    IDEA = "membership-hub"
    execute_uiux(
        args={
            "idea": IDEA,
        },
        language="Vietnamese",
    )

if __name__ == "__main__":
    test_uiux_generation()
