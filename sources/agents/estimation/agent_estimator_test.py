import os

from agent_estimator import EnterpriseAutonomousProjectEstimatorAgent


def test_estimation():
    os.environ["AI_MODELS_KEYS_JSON"] = (
        '{ "https://api.mistral.ai/v1": "<!--API Key Here-->" }'
    )    
    PROJECT_NAME = "membership-hub"
    EnterpriseAutonomousProjectEstimatorAgent(
        idea=PROJECT_NAME,
        project=PROJECT_NAME,
        language="Vietnamese",
        buffer=1.5,
    ).execute()

if __name__ == "__main__":
    test_estimation()
