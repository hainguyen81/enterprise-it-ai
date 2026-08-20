# ==========================================
# FILE: ./marketing_pipeline/planner_editor.py
# DESCRIPTION: Native OpenAI Implementation of MarketingPlannerAgent
# COMMENTS: Written in English as mandated
# ==========================================
import sys
from types import SimpleNamespace

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    parse_args,
    write_file,
)

# super agent
from sources.agents.marketing.agent_marketing import AbstractMarketingAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
# models list
SYSTEM_PROMPT_TEMPLATE      = "prompt.system.planner.editor.md"
USER_PROMPT_TEMPLATE        = "prompt.user.planner.editor.md"

APPROVAL_PLANNER_RAW_FILE   = "marketing-planner.approval.md"
PLANNER_LOG_FILE            = "marketing-planner-editor_log.md"

class EnterpriseMarketingPlannerEditorAgent(AbstractMarketingAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id="EnterpriseMarketingPlannerEditorAgent",
            agent_name="💡🎯 EnterpriseMarketingPlannerEditorAgent",
            **kwargs,
        )
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_marketing", file=PLANNER_LOG_FILE)
    
    # @override
    def system_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_marketing_prompts", file=SYSTEM_PROMPT_TEMPLATE)
    
    # @override
    def user_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_marketing_prompts", file=USER_PROMPT_TEMPLATE)

    # @override
    def __pre_execute__(self, **kwargs):
        # read planner file
        raw_planner_content = self.__read_marketing_planner__()

        # not anything to publish, exit
        if not raw_planner_content:
            self.logger.critical("💀 Not found MARKETING PLANNER file to process")
            sys.exit(1)
        
        # read rejected-planner file
        raw_reviewed_planner_content = self.__read_reviewed_marketing_planner__()

        # not anything to publish, exit
        if not raw_reviewed_planner_content:
            self.logger.critical("💀 Not found REJECTED MARKETING PLANNER file to process")
            sys.exit(1)

        # return merged new values
        return {
            **kwargs,
            "platform_target": self.get_kwargs_by_key(key="platform_target", **kwargs)
            or self.get_kwargs_by_key(key="platform", **kwargs)
            or "Generic",
            "raw_flawed_planner_content": raw_planner_content,
            "raw_rejected_planner_content": raw_reviewed_planner_content
        }
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("❌ Invalid AI raw response: No data to process")
        
        # -------------------------------------------------------------
        # FIXED MARKETING PLANNER
        # -------------------------------------------------------------
        # write storage planner report
        write_file(
            file=self.__storage_path__(
                storage_name="storage_marketing",
                file=f"{self.project_name}/{APPROVAL_PLANNER_RAW_FILE}",
            ),
            data=response_data,
        )
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.__output_storage_path__(
                    storage_name="output_marketing", file=APPROVAL_PLANNER_RAW_FILE
                ),
                data=raw_response,
            )

def execute_marketing_planner_editor(args: dict, **unknown_args):
    # to simple object namespace
    if isinstance(args, dict):
        args = SimpleNamespace(**args)
    
    # execute
    EnterpriseMarketingPlannerEditorAgent(
        idea=args.idea, project=args.idea, **unknown_args
    ).execute()

if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
    
    args, unknown_args = parse_args(
        description="🎯 EnterpriseMarketingPlannerEditorAgent",
        parser_callback=add_known_arguments,
    )
    execute_marketing_planner_editor(args=args, unknown_args=unknown_args)
