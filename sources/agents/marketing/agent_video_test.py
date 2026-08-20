import os

from agent_video import execute_marketing_video_creator


def test_marketing_video_creator():
    os.environ["AI_MODELS_KEYS_JSON"] = (
        '{ "https://api.mistral.ai/v1": "<!--API Key HERE-->" }'
    )
    PROJECT_NAME = "membership-hub"
    execute_marketing_video_creator(
        args={
            "idea": PROJECT_NAME,
        },
        language="Vietnamese",
        video="🎬 Shorts",
    )


if __name__ == "__main__":
    test_marketing_video_creator()
