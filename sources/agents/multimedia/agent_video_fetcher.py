# ==========================================
# FILE: ./marketing_pipeline/video_extractor.py
# DESCRIPTION: Enterprise Raw Multi-media Stream Fetcher for Manual Local Storage
# COMMENTS: Written in English as mandated
# ==========================================
import sys
import time
from types import SimpleNamespace

import requests
from jsonpath_ng import parse

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    exception_stacktrace,
    parse_args,
    read_json_file,
    write_file,
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
VIDEO_FETCHER_LOG_FILE          = "video-fetcher_log.md"
VIDEO_FETCHER_API_SECRETS_KEY   = "VIDEO_FETCHER_API_SECRETS_KEY"         


class EnterpriseRawVideoFetcher(AbstractSubAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id='EnterpriseRawVideoFetcher',
            agent_name='🎞️ EnterpriseRawVideoFetcher',
            **kwargs
        )
    
    def __project_marketing_scenes_video_file__(self):
        return self.__storage_path__(storage_name="storage_multimedia", file=f"{self.project_name}/marketing-video-creator.json")
    
    # @override
    def initialize_models(self):
        pass
    
    # @override
    def __close_ai_client__(self):
        pass
    
    def agent_secrets_key(self) -> str:
        return VIDEO_FETCHER_API_SECRETS_KEY
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_multimedia", file=VIDEO_FETCHER_LOG_FILE)
    
    # @override
    def system_prompt_template(self) -> str:
        pass
    
    # @override
    def user_prompt_template(self) -> str:
        pass
    
    # @override
    def __pre_execute__(self, **kwargs):
        # read scenes video file
        scenes_file = self.__project_marketing_scenes_video_file__()
        _, json_scenes = read_json_file(file_path=scenes_file)
        
        # not anything to publish, exit
        if not json_scenes or "storyboard_flow" not in json_scenes or len(json_scenes.get("storyboard_flow", [])) <= 0:
            self.logger.warning("⚠️ Not found MARKETING SCENES VIDEO file to process")
            sys.exit(0)
        
        # return merged new values
        return {
            **kwargs,
            "scenes": json_scenes.get("storyboard_flow", [])
        }
    
    def __api_headers__(self, api_key: str, json_content: bool, **api_headers):
        headers = { "Content-Type": "application/json" } if json_content else {}
        return {
            **(api_headers or {}),
            **headers,
            "Authorization": f"Bearer {api_key}",
        } if "Authorization" not in api_headers else {
            "Authorization": f"Bearer {api_key}",
            **(api_headers or {}),
            **headers,
        }
    
    def __build_video_generation_requests__(
        self,
        api_key: str,
        base_url: str,
        api_path: str,
        api_method: str,
        prompt: str,
        api_params: dict,
        api_payload: dict,
        api_prompt_key: str,
        **api_headers,
    ):
        # request method
        api_method = api_method.upper() if api_method else "POST"
        
        # Step 1: Build headers
        headers = self.__api_headers__(api_key, True, **api_headers)
        self.logger.debug(f"     |__  Headers: {headers}")

        # Step 2: Build params
        params = {
            **(api_params or {}),
        }
        self.logger.debug(f"     |__  Params: {params}")

        # Step 3: Build payload
        payload = (
            {
                **(api_payload or {}),
                api_prompt_key: prompt,
            }
            if api_prompt_key and prompt
            else {
                **(api_payload or {}),
                "prompt": prompt,
            } if prompt
            else {
                **(api_payload or {}),
            }
        )
        self.logger.debug(f"     |__  Payload: {payload}")

        # Step 4: Build endpoint
        url = f"{base_url}/{api_path}" if api_path else base_url
        url_prompt_path_key = (
            f"${{{api_prompt_key}}}" if api_prompt_key else "${prompt}"
        )
        if url_prompt_path_key in url:
            payload_prompt = payload.pop(
                api_prompt_key
            ) if api_prompt_key and api_prompt_key in payload \
                else payload.pop("prompt", None)
            url = url.replace(url_prompt_path_key, payload_prompt)
            
        self.logger.info(f"     |__  URL: {api_method} | {url}")
        
        # Step 5: Build request function 
        request_method = {
            "POST": requests.post,
            "GET": requests.get,
            "PATCH": requests.patch,
            "PUT": requests.put,
            "DELETE": requests.delete,
            "HEAD": requests.head
        }
        # return meterials
        return (
            request_method.get(api_method) if api_method in request_method else request_method.get("POST"),
            url, headers, params, payload
        )
    
    def __trigger_video_generation_task__(
        self,
        api_key: str,
        base_url: str,
        api_path: str,
        api_method: str,
        scene_visual_prompt: str,
        api_params: dict,
        api_payload: dict,
        api_prompt_key: str,
        api_task_path: str,
        **api_headers,
    ) -> str:
        # Build request meterials
        request_method, url, headers, params, payload = (
            self.__build_video_generation_requests__(
                api_key=api_key,
                base_url=base_url,
                api_path=api_path,
                api_method=api_method,
                prompt=scene_visual_prompt,
                api_params=api_params,
                api_payload=api_payload,
                api_prompt_key=api_prompt_key,
                **api_headers,
            )
        )
        
        # Executes native programmatic request dispatch loop
        response = request_method(
            url=url, headers=headers, params=params, json=payload, timeout=120
        )
        response_json = response.json()
        self.logger.info(f"     |__  Response: {response_json}")
        response.raise_for_status() # check response
        
        # parse task identity
        jsonpath_expr = parse(api_task_path) if api_task_path else parse("taskId")
        matches = jsonpath_expr.find(response_json)
        return matches[0].value if matches \
            else response_json.get(api_task_path) if api_task_path and api_task_path in response_json \
                else response_json.get("taskId") or None
    
    def __video_render_status_polling__(self, api_key: str, base_url: str, task_id: str, **api_headers) -> str:
        # Build request meterials
        request_method, url, headers, params, payload = (
            self.__build_video_generation_requests__(
                api_key=api_key,
                base_url=base_url,
                api_path=task_id,
                api_method="GET",
                prompt=None,
                api_params=None,
                api_payload=None,
                api_prompt_key=None,
                **api_headers,
            )
        )
        
        # Execute active polling loops until status switches to complete
        while True:
            response = request_method(
                url=url, headers=headers, params=params, json=payload, timeout=120
            )
            status_data = response.json()
            self.logger.info(f"     |__  [ POLLING ] Response: {status_data}")
            response.raise_for_status() # check response
            if status_data.get("status") == "SUCCEEDED":
                return status_data.get("assetUrl")
            elif status_data.get("status") == "FAILED":
                raise RuntimeError(f"[ ERROR ] Remote cloud render pipeline crashed for task: {task_id}")
            time.sleep(5) # Wait 5 seconds between status verification check beats
    
    def __render_video_scene__(
        self,
        api_key: str,
        base_url: str,
        api_path: str,
        scene: dict,
        api_scene_key: str,
        api_payload: dict,
        api_prompt_key: str,
        api_task_path: str,
        **api_headers,
    ) -> bytes:
        scene = scene or {}
        scene_id = scene.get("scene_id")
        scene_visual_prompt = scene.get(api_scene_key) if api_scene_key else scene.get("visual_description")
        self.logger.info(f"[ ASYNC PROCESS ] Spawning render task for Scene {scene_id}")
        self.logger.info(f"     |__  🎬 Scene: {scene_visual_prompt}")
        
        # Step 1: Dispatch text-to-video prompt to cloud AI engine
        task_id = self.__trigger_video_generation_task__(
            api_key=api_key,
            base_url=base_url,
            api_path=api_path,
            scene_virtual_prompt=scene_visual_prompt,
            api_payload=api_payload,
            api_prompt_key=api_prompt_key,
            api_task_path=api_task_path,
            **api_headers,
        )
        if not task_id:
            self.logger.error(
                "     |__  [ 💀 CRITICAL ] Could not request video task identity"
            )
            raise ConnectionError("[ 💀 CRITICAL ] Could not request video task identity")
        
        # Step 2: Poll and grab the raw CDN download URL link string
        video_download_url = self.__video_render_status_polling__(
            api_key=api_key,
            base_url=base_url,
            task_id=task_id,
            **api_headers
        )
        
        # Step 3: Stream and capture the pure raw video binary bytes from the network server
        self.logger.info(
            f"     |__  [ DOWNLOAD ] Pulling video bytes data from endpoint: {video_download_url}"
        )
        raw_video_response = requests.get(video_download_url, stream=True, timeout=120)
        raw_video_response.raise_for_status() # check response
        if raw_video_response.status_code == 200:
            return (scene_id, raw_video_response.content)
        else:
            raise ConnectionError(
                f"[ 💀 CRITICAL ] Network buffer failed fetching bytes. Status: {raw_video_response.status_code}"
            )
    
    def __sync_render_video_scene__(
        self,
        api_key: str,
        base_url: str,
        api_path: str,
        api_method: str,
        scene: dict,
        api_scene_key: str,
        api_params: dict,
        api_payload: dict,
        api_prompt_key: str,
        **api_headers,
    ) -> bytes:
        scene = scene or {}
        scene_id = scene.get("scene_id")
        api_method = api_method.upper() if api_method else "POST"
        scene_visual_prompt = scene.get(api_scene_key) if api_scene_key else scene.get("visual_description")
        self.logger.info(f"[ SYNC PROCESS ] Spawning render task for Scene {scene_id}")
        self.logger.info(f"     |__  🎬 Scene: {scene_visual_prompt}")
        
        # Build request meterials
        request_method, url, headers, params, payload = (
            self.__build_video_generation_requests__(
                api_key=api_key,
                base_url=base_url,
                api_path=api_path,
                api_method=api_method,
                prompt=scene_visual_prompt,
                api_params=api_params,
                api_payload=api_payload,
                api_prompt_key=api_prompt_key,
                **api_headers,
            )
        )
        
        # Stream and capture the pure raw video binary bytes from the network server
        self.logger.info(
            f"     |__  [ DOWNLOAD ] Pulling video bytes data from endpoint: {url}"
        )
        raw_video_response = request_method(
            url=url,
            headers=headers,
            params=params,
            json=payload,
            stream=True,
            timeout=120,
        )
        raw_video_response_json = raw_video_response.json()
        self.logger.info(f"                |__  Response: {raw_video_response_json}")
        raw_video_response.raise_for_status() # check response
        if raw_video_response.status_code == 200:
            return (scene_id, raw_video_response.content)
        else:
            raise ConnectionError(
                f"[ 💀 CRITICAL ] Network buffer failed fetching bytes. Status: {raw_video_response.status_code}"
            )
    
    # @override
    def __execute__(self, **kwargs):
        scenes = self.get_kwargs_by_key(key="scenes", **kwargs)
        if not scenes:
            raise RuntimeError("❌ Invalid scenes data: No scenes to process")
        
        # loop to try for each video API
        rendered_videos = []
        for api in self.secrets:
            # parse API configuration from secrets
            api_key = api.get("api_key")
            base_url = api.get("base_url")
            api_path = api.get("path") if "path" in api else None
            api_method = api.get("method") if "method" in api else "POST"
            api_headers = api.get("headers") if "headers" in api else {}
            api_params = api.get("params") if "params" in api else {}
            api_payload = api.get("payload") if "payload" in api else {}
            api_prompt_key = api.get("promptKey") if "promptKey" in api else None
            api_task_path = api.get("taskIdPath") if "taskIdPath" in api else None
            api_scene_key = (
                api.get("sceneKey") if "sceneKey" in api else "visual_description"
            )
            api_sync = str(api.get("sync")).lower() in ("yes", "true", "t", "1") if "sync" in api else False
            if not api_key or not base_url:
                self.logger.warning("⚠️ Invalid API configuration: Missing api_key or base_url")
                continue
            
            # call API to rendering video scenes
            try:
                for scene in scenes:
                    # render scene video and get raw bytes
                    if api_sync:
                        scene_id, raw_video_bytes = self.__sync_render_video_scene__(
                            api_key=api_key,
                            base_url=base_url,
                            api_path=api_path,
                            api_method=api_method,
                            scene=scene,
                            api_scene_key=api_scene_key,
                            api_params=api_params,
                            api_payload=api_payload,
                            api_prompt_key=api_prompt_key,
                            **api_headers,
                        )
                    
                    # async
                    else:
                        scene_id, raw_video_bytes = self.__render_video_scene__(
                            api_key=api_key,
                            base_url=base_url,
                            api_path=api_path,
                            api_method=api_method,
                            scene=scene,
                            api_scene_key=api_scene_key,
                            api_params=api_params,
                            api_payload=api_payload,
                            api_prompt_key=api_prompt_key,
                            api_task_path=api_task_path,
                            **api_headers,
                        )
                    
                    # write raw video bytes to local storage
                    video_file = self.__storage_path__(storage_name="storage_multimedia", file=f"{self.project_name}/scene-{scene_id}.mp4")
                    write_file(
                        file=video_file,
                        data=raw_video_bytes
                    )
                    rendered_videos.append(scene_id)
                    self.logger.info(
                        f"✅ [ SUCCESS ] Scene {scene_id} video fetched and stored at: {video_file}"
                    )
            except Exception as e:
                self.logger.error(f"❌ Error processing Scene {scene.get('scene_id')}: {exception_stacktrace(e)}")
                self.__handle_execute_exception__(e, **kwargs)
            
            # remove rendered videos out of scenes list to avoid reprocessing
            scenes = [scene for scene in scenes if scene.get("scene_id") not in rendered_videos]
            
            # out of scenes
            if len(scenes) <= 0:
                break
    
    # @override
    def process_communication(self, **kwargs):
        pass

def execute_video_fetcher(args: dict, **unknown_args):
    # to simple object namespace
    if isinstance(args, dict):
        args = SimpleNamespace(**args)

    # execute
    EnterpriseRawVideoFetcher(
        idea=args.idea, project=args.idea, **unknown_args
    ).execute()


if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
    
    args, unknown_args = parse_args(
        description="🎞️ EnterpriseRawVideoFetcher",
        parser_callback=add_known_arguments
    )
    execute_video_fetcher(args=args, unknown_args=unknown_args)
