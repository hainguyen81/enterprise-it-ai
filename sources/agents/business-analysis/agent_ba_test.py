import os

from agent_ba import execute_ba


def test_ba_generation():
    # openrouter
    # AI_BASE_URL = "https://openrouter.ai/api/v1"
    # AI_API_KEY = (
    #     # "sk-or-v1-*********" # GMail
    #     # "sk-or-v1-*********" # Yahoo! Mail
    #     # "sk-or-v1-*********" # Proton! Mail
    # )

    # cloudflare
    # AI_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/*********/ai/v1" # GMail
    # AI_API_KEY = (
    #     "cfut_*********"  # GMail
    # )
    AI_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/*********/ai/v1"  # Proton! Mail
    AI_API_KEY = "cfut_*********"  # Proton! Mail

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
