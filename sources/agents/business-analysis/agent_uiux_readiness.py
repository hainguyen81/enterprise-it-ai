import json
import sys
from types import SimpleNamespace

from pydantic import BaseModel, Field

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    datetime_for_docid,
    parse_args,
    read_json_file,
    write_file,
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
SYSTEM_PROMPT_TEMPLATE  = "agent_uiux_readiness.prompt.system.md"
USER_PROMPT_TEMPLATE    = "agent_uiux_readiness.prompt.user.md"

BA_UI_UX_RAW_FILE       = "ba_uiux_audit.md"
BA_UI_UX_LOG_FILE       = "uiux_audit_log.md"


class EnterpriseUIUXReadinessAuditAgent(AbstractSubAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id="EnterpriseUIUXReadinessAuditAgent",
            agent_name="📐 EnterpriseUIUXReadinessAuditAgent",
            **kwargs,
        )
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_ba", file=BA_UI_UX_LOG_FILE)

    # @override
    def system_prompt_template(self) -> str:
        return self.__agents_path__(
            storage_name="storage_ba_prompts", file=SYSTEM_PROMPT_TEMPLATE
        )

    # @override
    def user_prompt_template(self) -> str:
        return self.__agents_path__(
            storage_name="storage_ba_prompts", file=USER_PROMPT_TEMPLATE
        )

    # @override
    def agent_temperature(self):
        return 0.3

    # @override
    def __pre_execute__(self, **kwargs):
        # read idea
        idea_same_project, raw_idea_content = self.__read_idea_or_requirements__(
            ignore_not_found=True
        )
        self.idea_is_project = idea_same_project

        # no idea also no requirements
        if not raw_idea_content:
            self.logger.critical("💀 Not found IDEA / Requirements file to process")
            sys.exit(1)

        # read ba/SRS
        raw_srs_content = self.__read_srs__(ignore_not_found=False)

        # return merged new values
        return {
            **kwargs,
            "project_name": self.__try_to_detect_project_name__(),
            "raw_srs_content": raw_srs_content,
        }

    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError(
                "💀 Invalid AI raw response."
            )
        
        # parse technical project name as folder name
        datetimeStr = datetime_for_docid()
        defaultPrjName = f"project-{datetimeStr}"
        project_name = self.project_name if self.idea_is_project and self.project_name else None
        detected_project_name = self.get_kwargs_by_key(key="project_name", **kwargs)
        project_name = project_name or detected_project_name or defaultPrjName

        # export UI/UX readiness audit
        write_file(
            file=self.__storage_path__(storage_name="storage_ba", file=f"{project_name}/{BA_UI_UX_RAW_FILE}"),
            data=response_data
        )

        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(file=self.__output_storage_path__(storage_name="output_ba", file=BA_UI_UX_RAW_FILE), data=raw_response)


def execute_uiux_readiness_audit(args: dict, **unknown_args):
    # to simple object namespace
    if isinstance(args, dict):
        args = SimpleNamespace(**args)

    # execute
    EnterpriseUIUXReadinessAuditAgent(
        idea=args.idea, project=args.idea, **unknown_args
    ).execute()


if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument(
            "--idea", type=str, help="Idea Identity / Project Name for searching"
        )

    args, unknown_args = parse_args(
        description="📐 EnterpriseUIUXReadinessAuditAgent",
        parser_callback=add_known_arguments,
    )
    execute_uiux_readiness_audit(args=args, unknown_args=unknown_args)
