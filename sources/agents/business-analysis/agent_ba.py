import hashlib
import sys
from types import SimpleNamespace
from typing import Any

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    datetime_for_docid,
    json_loads,
    parse_args,
    write_file,
    write_json_file,
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
SYSTEM_PROMPT_TEMPLATE      = "agent_ba.prompt.system.md"
USER_PROMPT_TEMPLATE        = "agent_ba.prompt.user.md"

SRS_FILE                    = "requirements.md"
SRS_COMPACTED_FILE          = "compacted_requirements.md"
PROJECT_INFO_FILE           = "project-info.json"
BA_RAW_FILE                 = "ba.md"
BA_LOG_FILE                 = "ba_log.md"

BA_OUTPUT_DELIMITER         = "[EXECUTION_REMEDIATION_PAYLOAD_START]"
BA_OUTPUT_COMPACT_START     = "<COMPACT_SRS_START>"
BA_OUTPUT_COMPACT_END       = "<COMPACT_SRS_END>"


class PrincipalBusinessAnalysisAgent(AbstractSubAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id='PrincipalBusinessAnalysisAgent',
            agent_name='💡🎯 PrincipalBusinessAnalysisAgent',
            **kwargs
        )
    
    def ba_output_raw_file(self):
        return self.__output_storage_path__(storage_name="output_ba", file=BA_RAW_FILE)
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_ba", file=BA_LOG_FILE)
    
    # @override
    def system_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_ba_prompts", file=SYSTEM_PROMPT_TEMPLATE)
    
    # @override
    def user_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_ba_prompts", file=USER_PROMPT_TEMPLATE)
    
    # @override
    def agent_temperature(self):
        return 0.8 # high ideas
    
    # @override
    def __pre_execute__(self, **kwargs):
        # read idea
        idea_same_project, file_content = self.__read_idea_or_requirements__(ignore_not_found=True)
        self.idea_is_project = idea_same_project
        
        # no idea also no requirements
        if not file_content:
            self.logger.critical("💀 Not found IDEA / Requirements file to process")
            sys.exit(1)
        
        # return merged new values
        detected_project_name = self.__try_to_detect_project_name__()
        _, idea_file = self.__idea_files__()
        return {
            **kwargs,
            "project_name": detected_project_name,
            "idea_file": idea_file,
            "raw_idea_content": file_content
        }

    def __split_response__(self, raw_response) -> tuple[str, str, dict[str, Any]]:
        if not raw_response:
            raise RuntimeError("💀 Invalid AI raw response.")

        """
        Split BA response into exactly 3 logical parts:

        1. Full SRS
        2. Compact SRS Registry
        3. Terminal JSON metadata

        Expected output:

            <FULL SRS>

            <COMPACT_SRS_START>
            <COMPACT SRS>
            <COMPACT_SRS_END>

            [EXECUTION_REMEDIATION_PAYLOAD_START]
            { ...JSON... }

        Returns:
            (
                full_srs,
                compact_srs,
                metadata,
            )

        Raises:
            ValueError: when the response violates the expected structure.
        """
        raw_response = (
            str(raw_response).replace("\r\n", "\n").replace("\r", "\n").strip()
        )

        # ---------------------------------------------------------
        # 1. Validate marker counts
        # ---------------------------------------------------------
        marker_counts = {
            BA_OUTPUT_COMPACT_START: raw_response.count(BA_OUTPUT_COMPACT_START),
            BA_OUTPUT_COMPACT_END: raw_response.count(BA_OUTPUT_COMPACT_END),
            BA_OUTPUT_DELIMITER: raw_response.count(BA_OUTPUT_DELIMITER),
        }
        if marker_counts[BA_OUTPUT_COMPACT_START] != 1:
            raise ValueError(
                f"Expected exactly 1 {BA_OUTPUT_COMPACT_START}, got {marker_counts[BA_OUTPUT_COMPACT_START]}"
            )
        if marker_counts[BA_OUTPUT_COMPACT_END] != 1:
            raise ValueError(
                f"Expected exactly 1 {BA_OUTPUT_COMPACT_END}, got {marker_counts[BA_OUTPUT_COMPACT_END]}"
            )
        if marker_counts[BA_OUTPUT_DELIMITER] != 1:
            raise ValueError(
                f"Expected exactly 1 {BA_OUTPUT_DELIMITER}, "
                f"got {marker_counts[BA_OUTPUT_DELIMITER]}"
            )

        # ---------------------------------------------------------
        # 2. Locate markers
        # ---------------------------------------------------------
        compact_start = raw_response.index(BA_OUTPUT_COMPACT_START)
        compact_end = raw_response.index(BA_OUTPUT_COMPACT_END)
        remediation_start = raw_response.index(BA_OUTPUT_DELIMITER)

        # Marker ordering is mandatory:
        #
        # FULL SRS
        #   <
        # COMPACT_START
        #   <
        # COMPACT_END
        #   <
        # REMEDIATION_DELIMITER
        #
        if not (compact_start < compact_end < remediation_start):
            raise ValueError(
                "Invalid marker order. Expected: "
                f"{BA_OUTPUT_COMPACT_START} -> {BA_OUTPUT_COMPACT_END} -> "
                f"{BA_OUTPUT_DELIMITER}"
            )

        # ---------------------------------------------------------
        # 3. Extract Full SRS
        # ---------------------------------------------------------
        full_srs = raw_response[:compact_start].strip()
        if not full_srs:
            raise ValueError("Full SRS section is empty")

        # ---------------------------------------------------------
        # 4. Extract Compact SRS
        # ---------------------------------------------------------
        compact_content_start = compact_start + len(BA_OUTPUT_COMPACT_START)
        compact_srs = raw_response[compact_content_start:compact_end].strip()
        if not compact_srs:
            raise ValueError("Compact SRS section is empty")

        # ---------------------------------------------------------
        # 5. Extract terminal payload
        # ---------------------------------------------------------
        json_text = raw_response[remediation_start + len(BA_OUTPUT_DELIMITER) :].strip()
        if not json_text:
            raise ValueError("Terminal JSON payload is empty")

        # ---------------------------------------------------------
        # 6. JSON must be the ONLY thing after delimiter
        # ---------------------------------------------------------
        metadata = json_loads(data=json_text, silent=False)
        if not isinstance(metadata, dict):
            raise ValueError("Terminal JSON payload must be a JSON object")  # noqa: TRY004

        # ---------------------------------------------------------
        # 7. Validate existing terminal JSON contract
        # ---------------------------------------------------------
        required_keys = {
            "technical_codename",
            "descriptive_name",
            "brand_name",
            "requirement_tags",
        }
        actual_keys = set(metadata.keys())
        if actual_keys != required_keys:
            missing = required_keys - actual_keys
            extra = actual_keys - required_keys
            errors = []
            if missing:
                errors.append(f"missing keys: {sorted(missing)}")
            if extra:
                errors.append(f"unexpected keys: {sorted(extra)}")
            raise ValueError("Invalid terminal JSON contract: " + "; ".join(errors))
        if not isinstance(metadata["technical_codename"], str):
            raise ValueError('"technical_codename" must be a string')  # noqa: TRY004
        if not isinstance(metadata["descriptive_name"], str):
            raise ValueError('"descriptive_name" must be a string')  # noqa: TRY004
        if not isinstance(metadata["brand_name"], str):
            raise ValueError('"brand_name" must be a string')  # noqa: TRY004
        if not isinstance(metadata["requirement_tags"], list):
            raise ValueError('"requirement_tags" must be an array')  # noqa: TRY004
        if not all(isinstance(tag, str) for tag in metadata["requirement_tags"]):
            raise ValueError('Every "requirement_tags" item must be a string')

        # ---------------------------------------------------------
        # 8. Final structural check
        # ---------------------------------------------------------
        # There must be no compact/end/remediation marker accidentally
        # embedded inside the extracted Full SRS / Compact SRS.
        if BA_OUTPUT_COMPACT_END in full_srs:
            raise ValueError(f"{BA_OUTPUT_COMPACT_END} leaked into Full SRS")
        if BA_OUTPUT_DELIMITER in full_srs:
            raise ValueError(f"{BA_OUTPUT_DELIMITER} leaked into Full SRS")
        if BA_OUTPUT_DELIMITER in compact_srs:
            raise ValueError(f"{BA_OUTPUT_DELIMITER} leaked into Compact SRS")

        return (full_srs, compact_srs, metadata)
    
    # @override
    def clean_response(self, raw_response, **kwargs):
        if not raw_response:
            raise RuntimeError("💀 Invalid AI raw response.")
        
        # extract data
        raw_srs_content, raw_compacted_srs_content, project_metadata = (
            self.__split_response__(raw_response=raw_response)
        )
        
        # check srss summary
        projects = []
        if self.projects_summary and isinstance(self.projects_summary, tuple):
            projects = list(self.projects_summary[1]) if len(self.projects_summary) > 1 and isinstance(self.projects_summary[1], list) else list(self.projects_summary)
            
        elif self.projects_summary:
            projects = list(self.projects_summary)
        projects = [ i for i in projects if isinstance(i, dict) ]
        
        # parse technical project name as folder name
        datetimeStr = datetime_for_docid()
        defaultPrjName = f"project-{datetimeStr}"
        project_name = self.project_name if self.idea_is_project and self.project_name else None
        project_name = project_name or project_metadata.get("technical_codename") or None
        detected_project_name = self.get_kwargs_by_key(key="project_name", **kwargs)
        project_name = project_name or detected_project_name or defaultPrjName
        
        # detect existing project info if any
        project_info = next((pi for pi in projects if pi.get("technical_codename") == project_name or pi.get("idea") == self.idea_id), project_metadata)
        
        # remove all existing duplicate project names if found, to avoid duplicates in the summary
        projects[:] = [
            pi for pi in projects
            if pi.get("technical_codename") != project_name and pi.get("idea") != self.idea_id
        ]
        
        # initial project info
        idea_id = self.idea_id
        if self.idea_is_project:
            if "idea" in project_info:
                idea_id = project_info.get("idea")
            else:
                unique_id = hashlib.md5(idea_id.encode("utf-8")).hexdigest()[:12]
                idea_id = f"idea_{unique_id}"
        
        # update existing project info
        project_info = {
            # old info
            **project_info,
            # new info
            **project_metadata,
            # custom built info
            "idea": idea_id,
            "location": self.__storage_path__(
                storage_name="relative_ba", file=project_name
            ),
            "requirements": self.__storage_path__(
                storage_name="relative_ba", file=f"{project_name}/{SRS_FILE}"
            ),
            "compacted_requirements": self.__storage_path__(
                storage_name="relative_ba", file=f"{project_name}/{SRS_COMPACTED_FILE}"
            ),
        }
        
        # append as new project info if not found in the summary
        projects.append(project_info)
        self.projects_summary = projects
        
        # return cleaned/prepared data
        return {
            "raw_srs_content": raw_srs_content,
            "raw_compacted_srs_content": raw_compacted_srs_content,
            "project_info": {**project_info},
            "requirements_file": self.__storage_path__(
                storage_name="storage_ba", file=f"{project_name}/{SRS_FILE}"
            ),
            "compacted_requirements_file": self.__storage_path__(
                storage_name="storage_ba", file=f"{project_name}/{SRS_COMPACTED_FILE}"
            ),
            "project_info_file": self.__storage_path__(
                storage_name="storage_ba", file=f"{project_name}/{PROJECT_INFO_FILE}"
            ),
        }
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("💀 Invalid AI raw response. Not a valid JSON format data.")
        
        # export requirements
        requirements_file = response_data.get("requirements_file")
        requirements_content = response_data.get("raw_srs_content")
        write_file(file=requirements_file, data=requirements_content)
        self.logger.info(
            f"🎉 [ SUCCESS ] Received/Saved SRS Markdown Document: {requirements_file}"
        )
        
        # export compacted requirements
        compacted_requirements_file = response_data.get("compacted_requirements_file")
        compacted_requirements_content = response_data.get("raw_compacted_srs_content")
        write_file(file=compacted_requirements_file, data=compacted_requirements_content)
        self.logger.info(
            f"🎉 [ SUCCESS ] Received/Saved COMPACTED SRS Markdown Document: {compacted_requirements_file}"
        )
        
        # export project info
        project_info = response_data.get("project_info")
        write_json_file(file=response_data.get("project_info_file"), json_data=project_info)
        
        # export projects summary
        write_json_file(file=self.__projects_summary_path__(), json_data=self.projects_summary)
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.ba_output_raw_file(),
                data=raw_response
            )

def execute_ba(args: dict, **unknown_args):
    # to simple object namespace
    if isinstance(args, dict):
        args = SimpleNamespace(**args)

    # execute
    PrincipalBusinessAnalysisAgent(
        idea=args.idea, project=args.idea, **unknown_args
    ).execute()

if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
    
    args, unknown_args = parse_args(
        description="💡🎯 PrincipalBusinessAnalysisAgent",
        parser_callback=add_known_arguments
    )
    execute_ba(args=args, unknown_args=unknown_args)
