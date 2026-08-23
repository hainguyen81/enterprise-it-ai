# BLOCK 2: GENERATES PHASE MARKDOWN

import os
import time

# GEMINI
# from google import genai
# from google.genai import types
# OpenAI
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    datetime_for_agent,
    exception_stacktrace,
    get_logger,
    merge_master_prompt,
    parseAIResponseData,
    read_file_raw,
    regex_extract_by_pair_tags,
    render_prompt,
    storage_info,
    write_blueprint_log,
    write_file,
)

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
STORAGE                             = storage_info.get("storage") or {}
STORAGE_AGENTS                      = storage_info.get("agents") or {}
STORAGE_OUTPUT                      = storage_info.get("output") or {}

STORAGE_BLUEPRINT                   = STORAGE.get("storage_blueprint") or {}
STORAGE_AGENT_BLUEPRINT_PROMPTS     = STORAGE_AGENTS.get("storage_blueprint_prompts") or {}

PHASE_SYSTEM_PROMPT_TEMPLATE_PATH   = os.path.join(STORAGE_AGENT_BLUEPRINT_PROMPTS, "block_phase_prompt.system.md")
PHASE_USER_PROMPT_TEMPLATE_PATH     = os.path.join(STORAGE_AGENT_BLUEPRINT_PROMPTS, "block_phase_prompt.user.md")

DEFAULT_BLUEPRINT_LANGUAGE          = "English"

logger = get_logger("🏗️ EnterpriseSystemArchitecturePhaseAgent")

# GEMINI
# def generate_phase_contexts(client: genai.Client, project_name: str, requirements: str, global_context: str, num_phases: int, out_dir: str):

# OpenAI
def generate_phase_contexts(
    client: OpenAI,
    model_name: str,
    master_rules: str,
    project_name: str,
    requirements: str,
    global_context: str,
    num_phases: int,
    max_days_per_phase: int,
    language: str,
    out_dir: str,
    delay: int,
    phase: int = 0,
):
    """
    BLOCK 2: Decomposes requirements into segmented, sandbox-ready development boundaries.
    Executes raw isolated stateless calls per loop item to bypass sequence length degradation.
    """
    logger.info(f"🔄 [BLOCK 2] Decomposing requirements into {num_phases} isolated Phase Markdowns...")
    
    delay = delay if delay else 3
    max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
    log_phase_idx = 0
    log_prompt = ""
    log_system_prompt = ""
    model_name_safe = model_name if model_name else "gpt-4o"
    try:
        datetime_prompt, datetime_docid = datetime_for_agent()
        previous_phase_context = ""
        for phase_idx in range(1, num_phases + 1) if phase <= 0 else range(phase, phase + 1):
            log_phase_idx = phase_idx
            logger.info(f"     |__ 📝 Compiling Context Markdown for Phase {phase_idx} of {num_phases}...")
            
            # parse system prompt from template
            prompt_context = {
                "phase_idx": phase_idx,
                "project_name": project_name,
                "project_requirements": requirements,
                "doc_id": datetime_docid,
                "current_timestamp": datetime_prompt,
                "language": language or DEFAULT_BLUEPRINT_LANGUAGE,
                "num_phases": num_phases,
                "max_days_per_phase": max_days_per_phase,
                "global_markdown_context": global_context,
                "previous_phase_context": previous_phase_context
            }
            
            # parse system prompt from template
            system_prompt = render_prompt(PHASE_SYSTEM_PROMPT_TEMPLATE_PATH, prompt_context)
            log_system_prompt = system_prompt
            system_prompt = merge_master_prompt(master_rules, system_prompt)
            
            # parse user prompt from template
            user_prompt = render_prompt(PHASE_USER_PROMPT_TEMPLATE_PATH, prompt_context)
            log_prompt = user_prompt
            
            # GEMINI
            # response = client.models.generate_content(
            #     model='gemini-2.5-pro',
            #     contents=prompt,
            #     config=types.GenerateContentConfig(system_instruction=system_prompt, temperature=0.2)
            # )
            # raw_data = response.text
            
            # OpenAI
            response = client.chat.completions.create(
                model=model_name_safe,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.1
            )
            raw_data = parseAIResponseData(response)
            previous_phase_context = raw_data
            
            # --- use Regex to extract hidden HTML for next phase history generation ---
            # extract `START_DAY_LOG_INDEX`
            days_number, _ = regex_extract_by_pair_tags(
                tag_start="DAY_HEADER_START", tag_end="DAY_HEADER_END", data=raw_data
            )

            # convert project name
            safe_name = project_name.replace(' ', '-').lower()
            phase_blueprint_file = f"phase-{phase_idx}.context.blueprint.md"
            
            # export to storage
            out_path = write_file(
                dir=os.path.join(STORAGE_BLUEPRINT, safe_name, "plan", "context"),
                file=phase_blueprint_file,
                data=raw_data
            )
            
            # export output context
            out_path = write_file(
                dir=os.path.join(out_dir, "plan", "context"),
                file=phase_blueprint_file,
                data=raw_data
            )
        
            # write log
            write_blueprint_log(log_phase_idx, system_prompt, log_prompt.replace('#', '##'), raw_data.replace('#', '##') if raw_data else "-", False, model_name_safe, out_dir)
            
            logger.info(f"           | ✅ Found {days_number} days by `<!--DAY_HEADER_START-->` for Phase {phase_idx}")
            logger.info(f"           |__  👉 [ SUCCESS ] Received/Saved Phase {phase_idx} MD: {out_path}")
            
            # sleep to avoid 429 Too Many Requests
            if phase_idx < num_phases + 1:
                logger.debug(f"⏳ Rate limit guard active... holding pipeline for { delay } seconds to clear AI TPM window...")
                time.sleep(delay)
            
        result = num_phases > 0
        return result # success or empty phases
    except Exception as e:
        logger.error(f"❌ Failed to initiate chat/generate Phase {log_phase_idx} Blueprint: {exception_stacktrace(e)}")
        write_blueprint_log(log_phase_idx, log_system_prompt, log_prompt.replace('#', '##'), exception_stacktrace(e), False, model_name_safe, out_dir)
        return False


def run_test_phase_generation(callback, phase: int = 0):
    if not callback or not callable(callback):
        raise RuntimeError("Invalid test method!")

    PROJECT_NAME = "membership-hub"
    LANGUAGE = "Vietnamese"
    SOURCES_PATH = (
        "E:\\Java.Working\\16-4.saas.projects.jee-2026-03\\ai-scraper\\sources"
    )
    OUTDIR = os.path.join(SOURCES_PATH, "output", "blueprint", PROJECT_NAME)
    AGENTS_PATH = os.path.join(SOURCES_PATH, "agents")
    MASTER_PROMPT_TEMPLATE_PATH = os.path.join(
        AGENTS_PATH, "prompts", "prompt.rule.enterprise.governance.guardrails.md"
    )
    REQUIREMENTS_PATH = os.path.join(
        SOURCES_PATH, "requirements", PROJECT_NAME, "requirements.md"
    )
    GLOBAL_CONTEXT_PATH = os.path.join(
        SOURCES_PATH, "storage", "blueprint", PROJECT_NAME, "context", f"{PROJECT_NAME}.global.blueprint.md"
    )

    AI_BASE_URL = "https://api.mistral.ai/v1"
    AI_API_KEY = "<!--API Key Here-->"
    MODEL_NAME = "codestral-latest"

    # openAI
    client = OpenAI(
        base_url=AI_BASE_URL,
        api_key=AI_API_KEY,
        # 0 to turn off retries
        max_retries=3,
        # timeout in seconds (600 seconds ~ 10 minutes)
        timeout=600.0,
    )

    model_name = MODEL_NAME
    master_rules = render_prompt(
        MASTER_PROMPT_TEMPLATE_PATH,
        {
            "language": LANGUAGE,
        },
    )
    _, project_requirements = read_file_raw(REQUIREMENTS_PATH)
    _, global_context = read_file_raw(GLOBAL_CONTEXT_PATH)
    

    # run test
    callback(
        client=client,
        model_name=model_name,
        master_rules=master_rules,
        project_name=PROJECT_NAME,
        requirements=project_requirements,
        global_context=global_context,
        num_phases=5,
        max_days_per_phase=7,
        language=LANGUAGE,
        out_dir=OUTDIR,
        delay=5,
        phase=phase,
    )

    # close client
    try:
        client.close()
    except Exception as e:
        logger.error(f"⚠️ Exception while closing AI client: {e!s}")


def test_phase_generation(phase: int = 0):
    run_test_phase_generation(callback=generate_phase_contexts, phase=phase)


# ---------------------
# TEST
# ---------------------
if __name__ == "__main__":
    PHASE = 0
    test_phase_generation(phase=PHASE)

