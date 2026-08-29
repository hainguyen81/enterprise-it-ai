import os

from agent_video_fetcher import execute_video_fetcher


def test_marketing_video_fetcher():
    os.environ["AI_MODELS_KEYS_JSON"] = (
        '{ "https://api.mistral.ai/v1": "*******" }'
    )
    # os.environ["VIDEO_FETCHER_API_SECRETS_KEY"] = (
    #     '[{"api_key":"<!--API Key HERE-->","base_url":"https://api.dev.runwayml.com/v1","path":"text_to_video","provider":"Runway (Gen-3 Alpha)","headers":{"X-Runway-Version":"2024-11-06"},"payload":{"contentModeration":{"publicFigureThreshold":"auto"},"outputFormat":"prores","proresProfile":"422","model":"gen4.5","watermark":false,"ratio":"1280:720","duration":5},"promptKey":"promptText","sceneKey":"visual_description","taskIdPath":"taskId"}]'
    # )
    os.environ["VIDEO_FETCHER_API_SECRETS_KEY"] = (
        '[{"api_key":"*******","base_url":"https://gen.pollinations.ai","path":"video/pollen/${prompt}","method":"GET","params":{"model":"p-video","quality":"medium","resolution":"720p","duration":5,"aspectRatio":"16:9","audio":true},"sync":true,"promptKey":"prompt","sceneKey":"visual_description"}]'
    )
    PROJECT_NAME = "membership-hub"
    execute_video_fetcher(args={
        "idea": PROJECT_NAME,
    }, language="Vietnamese")


if __name__ == "__main__":
    test_marketing_video_fetcher()
