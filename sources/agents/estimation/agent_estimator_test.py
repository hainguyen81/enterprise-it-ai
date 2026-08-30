import os

from agent_estimator import EnterpriseAutonomousProjectEstimatorAgent


def test_estimation():
    AI_BASE_URL = "https://openrouter.ai/api/v1"
    AI_API_KEY = (
        "sk-or-v1-*******"
    )
    os.environ["AI_MODELS_KEYS_JSON"] = (
        f"{{ \"{AI_BASE_URL}\": \"{AI_API_KEY}\" }}"
    )
    PROJECT_NAME = "social-scheduler"
    EnterpriseAutonomousProjectEstimatorAgent(
        idea=PROJECT_NAME,
        project=PROJECT_NAME,
        language="Vietnamese",
        buffer=1.5,
    ).execute()

if __name__ == "__main__":
    test_estimation()
