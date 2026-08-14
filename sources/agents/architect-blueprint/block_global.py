# BLOCK 1: GENERATES GLOBAL CONTEXT

import os
import re
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
    json_tostring,
    merge_master_prompt,
    parseAIResponseData,
    read_file_raw,
    render_prompt,
    storage_info,
    write_blueprint_log,
    write_file,
)

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
STORAGE                                 = storage_info.get("storage") or {}
STORAGE_AGENTS                          = storage_info.get("agents") or {}
STORAGE_OUTPUT                          = storage_info.get("output") or {}

STORAGE_BLUEPRINT                       = STORAGE.get("storage_blueprint") or {}
STORAGE_AGENT_BLUEPRINT_PROMPTS         = STORAGE_AGENTS.get("storage_blueprint_prompts") or {}

GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH      = os.path.join(STORAGE_AGENT_BLUEPRINT_PROMPTS, "block_global_prompt.system.md")
GLOBAL_USER_PROMPT_TEMPLATE_PATH        = os.path.join(STORAGE_AGENT_BLUEPRINT_PROMPTS, "block_global_prompt.user.md")

GLOBAL_CHUNK_LOG_FILE                   = "{}.global.blueprint.chunk.{}.md"
GLOBAL_CHUNK_LOG                        = "# System Prompt {}:\n\n---\n\n{}\n\n---\n\n# User Prompt {}:\n\n---\n\n{}\n\n---\n\n# Output Chunk {}:\n\n---\n\n{}\n\n"

DEFAULT_BLUEPRINT_LANGUAGE              = "English"

DEFAULT_LIMIT_PHASE_LOG_TOKEN           = 4000

logger = get_logger("🏗️ EnterpriseSystemArchitectureGlobalAgent")

# GEMINI
# def generate_global_context(client: genai.Client, project_name: str, requirements: str, num_phases: int, out_dir: str) -> str:

# OpenAI
def generate_global_context(client: OpenAI, model_name: str, master_rules: str, project_name: str, requirements: str, num_phases: int, max_days_per_phase: int, language: str, out_dir: str) -> str:
    """
    BLOCK 1: Transforms raw text requirements into the supreme global project blueprint.
    Operates inside an isolated transactional API request to maximize logic token efficiency.
    """
    logger.info("🏗️  [ BLOCK 1 ] Extracting Raw Requirements into Global Context MD...")
    
    max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
    log_prompt = ""
    log_system_prompt = ""
    model_name_safe = model_name if model_name else "gpt-4o"
    try:
        datetime_prompt, datetime_docid = datetime_for_agent()
        
        # parse system prompt from template
        prompt_context = {
            "project_name": project_name,
            "project_requirements": requirements,
            "doc_id": datetime_docid,
            "current_timestamp": datetime_prompt,
            "language": language or DEFAULT_BLUEPRINT_LANGUAGE,
            "num_phases": num_phases,
            "max_days_per_phase": max_days_per_phase,
            # not using, it belongs to chunk case, add to avoid compile error
            "target_phase_index": -1,
            "force_full_export": True,
        }
        # parse system prompt from template
        system_prompt = render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, prompt_context)
        log_system_prompt = system_prompt
        system_prompt = merge_master_prompt(master_rules, system_prompt)
        logger.trace("=============================================================================")
        logger.trace("🤖 Combine MASTER + SYSTEM PROMPTS:")
        logger.trace(system_prompt)
        logger.trace("=============================================================================")
        
        # parse user prompt from template
        user_prompt = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, prompt_context)
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
            temperature=0.2
        )
        raw_data = parseAIResponseData(response)
        
        # convert project name
        safe_name = project_name.replace(' ', '-').lower()
        blueprint_file = f"{safe_name}.global.blueprint.md"
        
        # export to storage
        out_path = write_file(
            dir=os.path.join(STORAGE_BLUEPRINT, safe_name, "context"),
            file=blueprint_file,
            data=raw_data
        )
        
        # export to output path
        out_path = write_file(
            dir=os.path.join(out_dir, "context"),
            file=blueprint_file,
            data=raw_data
        )
        
        # write log
        write_blueprint_log(0, system_prompt, log_prompt.replace('#', '##'), raw_data.replace('#', '##') if raw_data else "-", False, model_name_safe, out_dir)
        
        logger.info(f"✅ [BLOCK 1 SUCCESS] Saved Global Blueprint: {out_path}")
        return raw_data
    except Exception as e:
        logger.error(f"❌ Failed to initiate chat/generate Global Blueprint: {exception_stacktrace(e)}")
        write_blueprint_log(0, log_system_prompt, log_prompt.replace('#', '##'), exception_stacktrace(e), False, model_name_safe, out_dir)
        return None

def generate_global_context_by_chunk(client: OpenAI, model_name: str, master_rules: str, project_name: str, requirements: str, num_phases: int, max_days_per_phase: int, language: str, out_dir: str, force_full_export: bool = False) -> str:
    # full export
    if force_full_export:
        return generate_global_context(
            client=client,
            model_name=model_name,
            master_rules=master_rules,
            project_name=project_name,
            requirements=requirements,
            num_phases=num_phases,
            max_days_per_phase=max_days_per_phase,
            language=language,
            out_dir=out_dir
        )
    
    # BLOCK 1: Transforms raw text requirements into the supreme global project blueprint.
    # Splits the generation pipeline into 3 discrete, non-truncating sequential steps.
    logger.info("🏗️ [ BLOCK 1 ] Initiating Multi-Part Progressive Extraction Pipeline...")
    
    max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
    model_name_safe = model_name if model_name else "gpt-4o"
    safe_name = project_name.replace(' ', '-').lower()
    blueprint_file = f"{safe_name}.global.blueprint.md"
    chunk_prompts = {}
    
    # result chunks
    accumulated_blueprint_chunks = []
    chunk_idx = 1
    
    try:
        datetime_prompt, datetime_docid = datetime_for_agent()
        time_in_seconds = 5
        
        # prompt context
        base_prompt_context = {
            "project_name": project_name,
            "project_requirements": requirements,
            "doc_id": datetime_docid,
            "current_timestamp": datetime_prompt,
            "language": language or DEFAULT_BLUEPRINT_LANGUAGE,
            "num_phases": num_phases,
            "max_days_per_phase": max_days_per_phase,
            "force_full_export": False,
            
            # chunk variables
            "target_segment": None,
            "total_tasks_registered": -1,
            "master_backlog_context": None,  # Nạp bối cảnh bảng 4.1 vừa sinh để AI phân bổ Phase
            "target_phase_index": -1,
            # only using for latest phase for audit
            "historic_ledger_map": None,
            "generated_phases_context": None
        }
        # history phases from phase loop chunks to use for final chunk
        immutable_tag_phase_summaries = []

        # # ==============================================================================
        # # CHUNK 1: from Section 1 to the end of Section 4
        # # ==============================================================================
        # logger.info(f"    |__ [ PART 1/3 ] Generating System Matrix and Master Product Backlog...")
        # ctx_part1 = {
        #     **base_prompt_context,
        #     "target_segment": "PART_1_INITIAL",
        # }
        
        # # build conversation
        # sys_prompt_p1 = merge_master_prompt(master_rules, render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, ctx_part1))
        # usr_prompt_p1 = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, ctx_part1)
        # conversation_history_messages = [
        #     {"role": "system", "content": sys_prompt_p1},
        #     {"role": "user", "content": usr_prompt_p1}
        # ]
        # chunk_prompts["chunk_1"] = conversation_history_messages
        
        # # communicate AI
        # response = client.chat.completions.create(
        #     model=model_name_safe,
        #     messages=conversation_history_messages,
        #     temperature=0.1
        # )
        # chunk_1 = parseAIResponseData(response)
        # accumulated_blueprint_chunks.append(chunk_1)
        
        # # --- count the task in section 4.1 trong chunk_1 ---
        # backlog_anchor_pattern = re.compile(r'<!--\s*REGISTERED_BACKLOG_TASK_ROW\s*-->')
        # actual_registered_tasks = len(backlog_anchor_pattern.findall(chunk_1))
        # if actual_registered_tasks <= 0:
        #     logger.warning("              | ⚠️ Token `<!--REGISTERED_BACKLOG_TASK_ROW-->` missing, activating Fallback Engine to scan Tag...")
        #     task_row_count = 0
        #     for line in chunk_1.split('\n'):
        #         line_clean = line.strip()
        #         # count task line (REQ/ARC/EXC/DAT/NFR)
        #         if (
        #             line_clean.startswith('|') and line_clean.endswith('|')
        #             and re.search(r'\[(REQ|ARC|EXC|DAT|NFR)-\d+\]', line_clean)
        #             and not re.search(r'[:\-]{3,}', line_clean)
        #         ):
        #             task_row_count += 1
        #     actual_registered_tasks = task_row_count
        #     logger.info(f"              |__  👉 📊 Fallback scan task line(s) (Calculated Task Rows): {actual_registered_tasks}")
        
        # # write chunk log
        # chunk_log_file = GLOBAL_CHUNK_LOG_FILE.format(project_name, chunk_idx)
        # write_file(
        #     dir=os.path.join(out_dir, "chunks"),
        #     file=chunk_log_file,
        #     data=GLOBAL_CHUNK_LOG.format(chunk_idx, json_tostring(conversation_history_messages), chunk_idx, chunk_1)
        # )
        # logger.info(f"              | ✅ [ SUCCESS ] Found total {actual_registered_tasks} tasks.")
        # logger.info(f"              |__  👉 Received/Saved chunk {chunk_idx} log: {chunk_log_file}")
        # chunk_idx += 1
        
        # # sleep 5 seconds to guard rate limit
        # logger.debug("    |__ ⏳ Rate limit guard active... holding pipeline for 15 seconds to clear AI TPM window...")
        # time.sleep(5)
        
        # ==============================================================================
        # CHUNK 1A: SECTION 1 TO SECTION 3 (INITIAL ARCHITECTURE METRICS)
        # ==============================================================================
        logger.info("    |__ [ PART 1/3 ] Generating System Matrix and Master Product Backlog...")
        logger.info("          |__ [ PART 1A ] Initial Global Context...")
        ctx_part1a = {
            **base_prompt_context,
            "target_segment": "PART_1_INITIAL",
        }
        
        # build conversation
        sys_prompt_p1a = merge_master_prompt(master_rules, render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, ctx_part1a))
        usr_prompt_p1a = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, ctx_part1a)
        msg_p1a = [{"role": "system", "content": sys_prompt_p1a}, {"role": "user", "content": usr_prompt_p1a}]
        chunk_prompts[f"chunk_{chunk_idx}"] = msg_p1a
        
        # communicate AI
        res_p1a = client.chat.completions.create(
            model=model_name_safe,
            messages=msg_p1a,
            temperature=0.1
        )
        chunk_1a = parseAIResponseData(res_p1a)
        accumulated_blueprint_chunks.append(chunk_1a)
        
        # write chunk log
        chunk_log_file = GLOBAL_CHUNK_LOG_FILE.format(project_name, chunk_idx)
        write_file(dir=os.path.join(out_dir, "chunks"), file=chunk_log_file,
                   data=GLOBAL_CHUNK_LOG.format(chunk_idx, sys_prompt_p1a, chunk_idx, usr_prompt_p1a, chunk_idx, chunk_1a))
        logger.info("                | ✅ [ SUCCESS ] Initial Global Context successfully.")
        logger.info(f"                |__  👉 Received/Saved chunk {chunk_idx} log: {chunk_log_file}")
        chunk_idx += 1
        
        # sleep in few seconds to guard rate limit
        logger.debug(f"    |__ ⏳ Rate limit guard active... holding pipeline for {time_in_seconds} seconds to clear AI TPM window...")
        time.sleep(time_in_seconds)

        # ==============================================================================
        # CHUNK 1B: SECTION 4.1 (MASTER PRODUCT BACKLOG - ATOMIC EXPANSION)
        # ==============================================================================
        logger.info("          |__ [ PART 1B ] Executing Atomic Extraction for Section 4.1 Backlog Table...")
        ctx_part1b = {
            **base_prompt_context,
            "target_segment": "PART_1_BACKLOG_4_1"
        }
        
        # build conversation
        sys_prompt_p1b = merge_master_prompt(master_rules, render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, ctx_part1b))
        usr_prompt_p1b = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, ctx_part1b)
        msg_p1b = [{"role": "system", "content": sys_prompt_p1b}, {"role": "user", "content": usr_prompt_p1b}]
        chunk_prompts[f"chunk_{chunk_idx}"] = msg_p1b
        
        # communicate AI
        res_p1b = client.chat.completions.create(
            model=model_name_safe,
            messages=msg_p1b,
            temperature=0.1
        )
        chunk_1b = parseAIResponseData(res_p1b)
        accumulated_blueprint_chunks.append(chunk_1b)

        # --- count the task in section 4.1 trong chunk_1b ---
        backlog_anchor_pattern = re.compile(r'<!--\s*REGISTERED_BACKLOG_TASK_ROW\s*-->')
        actual_registered_tasks = len(backlog_anchor_pattern.findall(chunk_1b))
        if actual_registered_tasks <= 0:
            logger.warning("                | ⚠️ Token `<!--REGISTERED_BACKLOG_TASK_ROW-->` missing, activating Fallback Engine to scan Tag...")
            task_row_count = 0
            for line in chunk_1b.split('\n'):
                line_clean = line.strip()
                # count task line (REQ/ARC/EXC/DAT/NFR)
                if (
                    line_clean.startswith('|') and line_clean.endswith('|')
                    and re.search(r'\[(REQ|ARC|EXC|DAT|NFR)-\d+\]', line_clean)
                    and not re.search(r'[:\-]{3,}', line_clean)
                ):
                    task_row_count += 1
            actual_registered_tasks = task_row_count
            logger.info(f"                |__  👉 📊 Fallback scan task line(s) (Calculated Task Rows): {actual_registered_tasks}")

        # write chunk log
        chunk_log_file = GLOBAL_CHUNK_LOG_FILE.format(project_name, chunk_idx)
        write_file(dir=os.path.join(out_dir, "chunks"), file=chunk_log_file,
                   data=GLOBAL_CHUNK_LOG.format(chunk_idx, sys_prompt_p1b, chunk_idx, usr_prompt_p1b, chunk_idx, chunk_1b))
        logger.info(f"                | ✅ [ SUCCESS ] Found total {actual_registered_tasks} tasks.")
        logger.info(f"                |__  👉 Received/Saved chunk {chunk_idx} log: {chunk_log_file}")
        chunk_idx += 1
        
        # sleep in few seconds to guard rate limit
        logger.debug(f"    |__ ⏳ Rate limit guard active... holding pipeline for {time_in_seconds} seconds to clear AI TPM window...")
        time.sleep(time_in_seconds)

        # ==============================================================================
        # CHUNK 1C: SECTION 4.2 (MULTI-PHASE SYNOPSIS MATRIX)
        # ==============================================================================
        logger.info("          |__ [ PART 1C ] Distributing Workload into Section 4.2 Synopsis Matrix...")
        ctx_part1c = {
            **base_prompt_context,
            "target_segment": "PART_1_MATRIX_4_2",
            "total_tasks_registered": actual_registered_tasks,
            "master_backlog_context": chunk_1b  # load master tasks backlog from chunk 4.1 to distribute phases
        }
        
        # build conversation
        sys_prompt_p1c = merge_master_prompt(master_rules, render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, ctx_part1c))
        usr_prompt_p1c = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, ctx_part1c)
        msg_p1c = [{"role": "system", "content": sys_prompt_p1c}, {"role": "user", "content": usr_prompt_p1c}]
        chunk_prompts[f"chunk_{chunk_idx}"] = msg_p1c
        
        # communicate AI
        res_p1c = client.chat.completions.create(model=model_name_safe, messages=msg_p1c, temperature=0.1)
        chunk_1c = parseAIResponseData(res_p1c)
        accumulated_blueprint_chunks.append(chunk_1c)
        
        # --- count the phase rows in section 4.2 trong chunk_1b ---
        phase_anchor_pattern = re.compile(r"<!--\s*REGISTERED_PHASE_ROW\s*-->")
        actual_registered_phases = len(phase_anchor_pattern.findall(chunk_1c))
        if actual_registered_phases != num_phases:
            logger.warning("                | ⚠️ Token `<!--REGISTERED_PHASE_ROW-->` missing, activating Fallback Engine to scan Phase...")
            phase_row_count = 0
            for line in chunk_1b.split('\n'):
                line_clean = line.strip()
                # count phase line (REQ/ARC/EXC/DAT/NFR)
                if (
                    line_clean.startswith('|') and line_clean.endswith('|')
                    and re.search(r'\[(REQ|ARC|EXC|DAT|NFR)-\d+\]', line_clean)
                    and not re.search(r'[:\-]{3,}', line_clean)
                ):
                    phase_row_count += 1
            actual_registered_phases = phase_row_count
            logger.info(f"                |__  👉 📊 Fallback scan phase line(s) (Calculated Phase Rows): {actual_registered_phases}")
            if actual_registered_phases != num_phases:
                logger.warning(f"                     | ⚠️ Phase matrix maybe WRONG, due to the scanned {actual_registered_phases} phases number doesn't match the expected {num_phases} phases...")
        
        # write chunk log
        chunk_log_file = GLOBAL_CHUNK_LOG_FILE.format(project_name, chunk_idx)
        write_file(dir=os.path.join(out_dir, "chunks"), file=chunk_log_file,
                   data=GLOBAL_CHUNK_LOG.format(chunk_idx, sys_prompt_p1c, chunk_idx, usr_prompt_p1c, chunk_idx, chunk_1c))
        logger.info(f"                | ✅ Found total {actual_registered_phases} phase rows.")
        logger.info( "                | ✅ [ SUCCESS ] Distributing Workload Synopsis Matrix successfully.")
        logger.info(f"                |__  👉 Received/Saved chunk {chunk_idx} log: {chunk_log_file}")
        chunk_idx += 1
        
        # sleep in few seconds to guard rate limit
        logger.debug(f"    |__ ⏳ Rate limit guard active... holding pipeline for {time_in_seconds} seconds to clear AI TPM window...")
        time.sleep(time_in_seconds)
        
        # ==============================================================================
        # CHUNK 2: LOOP PHASE IN SECTION 5
        # ==============================================================================
        logger.info(f"    |__ [ PART 2/3 ] Extracting Granular Daylog for {num_phases} phases...")
        for phase_idx in range(1, num_phases + 1):
            logger.info(f"          |__ Extracting Granular Daylog for Phase {phase_idx} out of {num_phases}...")
            ctx_part2 = {
                **base_prompt_context,
                "target_segment": "PART_2_PHASE_LOOP",
                "target_phase_index": phase_idx,
                "total_tasks_registered": actual_registered_tasks,
                # only using for latest phase for audit
                "historic_ledger_map": "\n\n".join(immutable_tag_phase_summaries),
                # inject synopsis table context for phase generation refer
                "master_backlog_context": f"{chunk_1b}\n\n{chunk_1c}",
            }
            
            # build conversation
            sys_prompt_p2 = merge_master_prompt(master_rules, render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, ctx_part2))
            usr_prompt_p2 = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, ctx_part2)
            active_loop_messages = [
                {"role": "system", "content": sys_prompt_p2},
                {"role": "user", "content": usr_prompt_p2}
            ]
            chunk_prompts["chunk_2"] = {
                phase_idx: active_loop_messages
            }
            
            # communicate AI
            response = client.chat.completions.create(
                model=model_name_safe,
                messages=active_loop_messages,
                temperature=0.1
            )
            phase_chunk = parseAIResponseData(response)
            
            # append conversation history for generating next phase
            accumulated_blueprint_chunks.append(phase_chunk)

            # --- use Regex to extract hidden HTML for next phase history generation ---
            # extract `START_ATOMIC_SUB_TASK_NODE`
            phase_tag_pattern = re.compile( r"<!--\s*START_DAY_LOG_INDEX\s*-->")
            found_day_logs = phase_tag_pattern.findall(phase_chunk)
            days_in_phase = len(found_day_logs)
            if days_in_phase <= 0:
                logger.warning("                | ⚠️ Token `<!--START_DAY_LOG_INDEX-->` missing, activating Fallback Engine to scan day logs...")

                # use regex to remove all code blocks as SQL, DDL, JSON
                clean_text = re.sub(r"```.*?```", "", phase_chunk, flags=re.DOTALL).strip()
                # if token exceeded
                if len(clean_text) > DEFAULT_LIMIT_PHASE_LOG_TOKEN:
                    logger.warning(f"                     | ⚠️ Phase Log Token exceeded {DEFAULT_LIMIT_PHASE_LOG_TOKEN} chracters, activating Fallback Engine to compress Day Logs Blocks...")
                    # Maximum compression, only collect lines that contains technical Tag IDs
                    salvaged_lines = []
                    for line in clean_text.split("\n"):
                        if re.search(r"\[(REQ|ARC|EXC|DAT|NFR)-\d+\]", line):
                            salvaged_lines.append(line.strip())
                    extracted_block = "\n".join(salvaged_lines)
                else:
                    # if it's in limit token, use it
                    extracted_block = f"### Phase {phase_idx} Logs (Salvaged Text):\n{clean_text.strip()}"
            else:
                extracted_block = "".join(found_day_logs)
            extracted_block = f"### Phase {phase_idx} Logs (Atomic Salvaged Tag Lines):\n\n{extracted_block}"
            immutable_tag_phase_summaries.append(extracted_block)

            # write chunk log
            chunk_log_file = GLOBAL_CHUNK_LOG_FILE.format(project_name, chunk_idx)
            write_file(dir=os.path.join(out_dir, "chunks"), file=chunk_log_file,
                    data=GLOBAL_CHUNK_LOG.format(chunk_idx, sys_prompt_p2, chunk_idx, usr_prompt_p2, chunk_idx, phase_chunk))
            logger.info(f"                | ✅ [ SUCCESS ] Found {days_in_phase} days (sub-tasks) from Phase {phase_idx}.")
            logger.info(f"                |__  👉 Received/Saved chunk {chunk_idx} log: {chunk_log_file}")
            chunk_idx += 1
        
            # sleep in few seconds to guard rate limit
            logger.debug(f"    |__ ⏳ Rate limit guard active... holding pipeline for {time_in_seconds} seconds to clear AI TPM window...")
            time.sleep(time_in_seconds)

        # # ==============================================================================
        # # CHUNK 3: from Section 6 to the end
        # # ==============================================================================
        # logger.info(f"    |__ [ PART 3/3 ] Generating Universal Security Codes & Git Branch Flow...")
        # ctx_part3 = {
        #     **base_prompt_context,
        #     "target_segment": "PART_3_FINAL",
        #     "total_tasks_registered": actual_registered_tasks,
        #     "generated_phases_context": "\n\n---\n\n".join(immutable_tag_phase_summaries)
        # }
        
        # # build conversation
        # sys_prompt_p3 = merge_master_prompt(master_rules, render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, ctx_part3))
        # usr_prompt_p3 = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, ctx_part3)
        # final_messages = [
        #     {"role": "system", "content": sys_prompt_p3},
        #     {"role": "user", "content": usr_prompt_p3}
        # ]
        # chunk_prompts["chunk_3"] = final_messages
        
        # # communicate AI
        # response = client.chat.completions.create(
        #     model=model_name_safe,
        #     messages=final_messages,
        #     temperature=0.1
        # )
        # chunk_3 = parseAIResponseData(response)
        # accumulated_blueprint_chunks.append(chunk_3)

        # # write chunk log
        # chunk_log_file = GLOBAL_CHUNK_LOG_FILE.format(project_name, chunk_idx)
        # write_file(dir=os.path.join(out_dir, "chunks"), file=chunk_log_file,
        #         data=GLOBAL_CHUNK_LOG.format(chunk_idx, sys_prompt_p3, chunk_idx, usr_prompt_p3, chunk_idx, chunk_3))
        # logger.info(f"          | ✅ [ SUCCESS ] 👉 Received/Saved chunk {chunk_idx} log: {chunk_log_file}")
        # chunk_idx += 1

        # ==============================================================================
        # COMBINE ALL CHUNKS
        # ==============================================================================
        raw_data = "\n\n".join(accumulated_blueprint_chunks)
        
        # export to storage
        out_path = write_file(
            dir=os.path.join(STORAGE_BLUEPRINT, safe_name, "context"),
            file=blueprint_file,
            data=raw_data
        )
        
        # export to output path
        out_path = write_file(
            dir=os.path.join(out_dir, "context"),
            file=blueprint_file,
            data=raw_data
        )
        
        # write log
        write_blueprint_log(0, json_tostring(chunk_prompts), raw_data, False, model_name_safe, out_dir)
        
        logger.info(f"✅ [ BLOCK 1 SUCCESS ] Saved Global Blueprint: {out_path}")
        return raw_data

    except Exception as e:
        logger.error(f"❌ Failed to initiate chat/generate Global Blueprint: {exception_stacktrace(e)}")
        write_blueprint_log(0, "SYSTEM_ERROR", "PIPELINE_CRASH", exception_stacktrace(e), False, model_name_safe, out_dir)
        return None

def test_global_generation():
    PROJET_NAME = "membership-hub"
    LANGUAGE = "Vietnamese"
    SOURCES_PATH = "E:\\Java.Working\\16-4.saas.projects.jee-2026-03\\ai-scraper\\sources"
    OUTDIR = os.path.join(SOURCES_PATH, "output", "blueprint", PROJET_NAME)
    AGENTS_PATH = os.path.join(SOURCES_PATH, "agents")
    MASTER_PROMPT_TEMPLATE_PATH = os.path.join(AGENTS_PATH, "prompts", "prompt.rule.enterprise.governance.guardrails.md")
    REQUIREMENTS_PATH = os.path.join(SOURCES_PATH, "requirements", PROJET_NAME, "requirements.md")
    
    AI_BASE_URL = "https://api.mistral.ai/v1"
    AI_API_KEY = "17yPa7JI942u1cqTmFAIuM3UmT6itKFv"
    MODEL_NAME = "codestral-latest"
    
    # openAI
    client = OpenAI(
        base_url=AI_BASE_URL,
        api_key=AI_API_KEY,
        # 0 to turn off retries
        max_retries=3, 
        # timeout in seconds (600 seconds ~ 10 minutes)
        timeout=600.0
    )
    
    model_name = MODEL_NAME
    master_rules = render_prompt(MASTER_PROMPT_TEMPLATE_PATH, { "language": LANGUAGE, })
    _, project_requirements = read_file_raw(REQUIREMENTS_PATH)

    # context generation
    generate_global_context_by_chunk(
            client=client,
            model_name=model_name,
            master_rules=master_rules,
            project_name="membership-hub",
            requirements=project_requirements,
            num_phases=5,
            max_days_per_phase=7,
            language=LANGUAGE,
            out_dir=OUTDIR,
            force_full_export=False
    )

    # close client
    try:
        client.close()
    except Exception as e:
        logger.error(f"⚠️ Exception while closing AI client: {e!s}")

# ---------------------
# TEST
# ---------------------
if __name__ == "__main__":
    test_global_generation()
