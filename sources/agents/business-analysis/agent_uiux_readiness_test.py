import os

from agent_uiux_readiness import execute_uiux_readiness_audit


def test_uiux_readiness_audit_generation():
    AI_BASE_URL = "https://openrouter.ai/api/v1"
    AI_API_KEY = (
        "sk-or-v1-*******"
    )
    os.environ["AI_MODELS_KEYS_JSON"] = (
        f"{{ \"{AI_BASE_URL}\": \"{AI_API_KEY}\" }}"
    )
    IDEA = "membership-hub"
    execute_uiux_readiness_audit(
        args={
            "idea": IDEA,
        },
        language="Vietnamese",
    )

if __name__ == "__main__":
    test_uiux_readiness_audit_generation()
