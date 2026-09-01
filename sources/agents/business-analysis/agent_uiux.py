import json
import sys
from types import SimpleNamespace

from pydantic import BaseModel, Field

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    parse_args,
    parseAIResponseJsonData,
    write_file,
    write_json_file,
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
SYSTEM_PROMPT_TEMPLATE      = "agent_uiux.prompt.system.md"
USER_PROMPT_TEMPLATE        = "agent_uiux.prompt.user.md"

SRS_FILE                    = "requirements.md"
PROJECT_INFO_FILE           = "project-info.json"
UI_UX_RAW_FILE              = "uiux.md"
UI_UX_JSON_FILE             = "uiux.json"
UI_UX_LOG_FILE              = "uiux_log.md"
UI_UX_ALLOWED_DEVICES       = ["Web_Desktop", "Mobile_App_iOS", "Mobile_App_Android"]


# 1. Define the Traceability Sync Schema between BA and UI/UX Layout
class LinkedTraceability(BaseModel):
    requirement_tag: str = Field(
        description="The REQ tag from the BA SRS document, e.g., [REQ-001] or [REQ-002]"
    )
    data_tag: str | None = Field(
        description="The matching DAT tag from the BA data dictionary if applicable, e.g., [DAT-001]"
    )


class UIElement(BaseModel):
    element_id: str = Field(
        description="Unique technical identifier for the UI element, e.g., btn_create_schedule, txt_keyword"
    )
    element_type: str = Field(
        description="The type of interface component: 'Button' | 'Input_Text' | 'Table' | 'Dropdown' | 'Alert' | 'Card'"
    )
    label_en: str = Field(
        description="The English text or label displayed on the interface for users"
    )
    placeholder_or_value: str | None = Field(
        description="The default placeholder text, tooltip, or sample row data"
    )
    traceability: LinkedTraceability = Field(
        description="Direct relational map back to the BA requirement and data definitions"
    )
    ux_justification: str = Field(
        description="The UX cognitive psychology rationale for choosing and placing this component based on the SRS"
    )


class UISection(BaseModel):
    section_name: str = Field(
        description="The interface grid partition: 'Navigation_Bar' | 'Sidebar_Menu' | 'Main_Data_Table' | 'Filter_Panel'"
    )
    visual_hierarchy_weight: int = Field(
        description="The visual priority weight score from 1 (lowest priority) to 5 (highest screen priority)"
    )
    elements: list[UIElement] = Field(
        description="Array of fine-grained interactive UI components contained within this section zone"
    )


class ScreenMockupBlueprint(BaseModel):
    screen_id: str = Field(
        description="The unique screen identifier mapped to the BA Epic Module, e.g., SCR_001_SCHEDULE_MANAGEMENT"
    )
    screen_title: str = Field(
        description="The primary display header title of the screen layout"
    )
    layout_structure: str = Field(
        description="The architectural layout definition blueprint using CSS Flexbox/Grid or technical wireframe structure specifications"
    )
    sections: list[UISection] = Field(
        description="List of detailed visual layout block sections that compose the entire screen viewport"
    )


class ProjectUXMockupPayload(BaseModel):
    technical_codename: str = Field(
        description="The lowercase, hyphenated slug codename of the active project (MUST perfectly match the BA codename)"
    )
    target_device: str = Field(
        description="The physical viewport target factor: 'Web_Desktop' | 'Mobile_App_iOS' | 'Mobile_App_Android'"
    )
    screens: list[ScreenMockupBlueprint] = Field(
        description="Comprehensive array of screen mockups translated directly from the SRS modules"
    )


# 2. Initialize the Downstream Core UX/UI Processing Agent
class EnterpriseUXUIArchitectAgent(AbstractSubAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id="EnterpriseUXUIArchitectAgent",
            agent_name="🎨 EnterpriseUXUIArchitectAgent",
            **kwargs,
        )

    def uiux_output_raw_file(self):
        return self.__output_storage_path__(
            storage_name="output_ba", file=UI_UX_RAW_FILE
        )
    
    def uiux_output_json_file(self):
        return self.__output_storage_path__(storage_name="output_ba", file=UI_UX_JSON_FILE)

    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_ba", file=UI_UX_LOG_FILE)

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
        return 0.2

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
            "allowed_devices": UI_UX_ALLOWED_DEVICES,
            "uiux_json_schema": json.dumps(
                ProjectUXMockupPayload.model_json_schema(), indent=2
            ),
            "raw_srs_content": raw_srs_content,
        }

    # @override
    def clean_response(self, raw_response, **kwargs):
        if not raw_response:
            raise RuntimeError("💀 Invalid AI raw response.")
        self.logger.info("- Raw Response: %s", raw_response)
        return parseAIResponseJsonData(raw_response)

    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError(
                "💀 Invalid AI raw response. Not a valid JSON format data."
            )

        # export UI/UX json
        write_json_file(
            file=self.uiux_output_json_file(), json_data=response_data
        )

        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(file=self.uiux_output_raw_file(), data=raw_response)


def execute_uiux(args: dict, **unknown_args):
    # to simple object namespace
    if isinstance(args, dict):
        args = SimpleNamespace(**args)

    # execute
    EnterpriseUXUIArchitectAgent(
        idea=args.idea, project=args.idea, **unknown_args
    ).execute()


if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument(
            "--idea", type=str, help="Idea Identity / Project Name for searching"
        )

    args, unknown_args = parse_args(
        description="🎨 EnterpriseUXUIArchitectAgent",
        parser_callback=add_known_arguments,
    )
    execute_uiux(args=args, unknown_args=unknown_args)
