import hashlib
import re
from types import SimpleNamespace

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    parse_args,
    regex_extract_by_name_pair_tags,
    write_file,
    write_json_file,
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
SYSTEM_PROMPT_TEMPLATE      = "agent_idea_generator.prompt.system.md"
USER_PROMPT_TEMPLATE        = "agent_idea_generator.prompt.user.md"

IDEAS_OUTPUT_FILE           = "ideas.md"
IDEAS_LOG_FILE              = "ideas_log.md"

DEFAULT_IDEAS_DOMAIN        = "Any high-momentum, trending industry in 2026 (such as AI Agents, Automation Web-apps, Renewable Energy tech, Spatial Computing, Web3/Fintech, etc.) where a lightweight software solution or Micro-SaaS can be rapidly deployed to capture immediate market demand with an MVP built within 2-4 weeks"
DEFAULT_IDEAS_QUNATITY      = 3
DEFAULT_IDEAS_LANGUAGE      = "English"


class EnterpriseIdeaGeneratorAgent(AbstractSubAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id='EnterpriseIdeaGeneratorAgent',
            agent_name='💡 EnterpriseIdeaGeneratorAgent',
            **kwargs
        )

    def __idea_history_names__(self):
        history = self.history_ideas if self.history_ideas else []
        return [
            item["idea"]
            for item in history
            if isinstance(item, dict) and item.get("idea")
        ]
    
    # @override
    def initialize(self):
        super().initialize()
        
        # load generated ideas to avoid conflicts
        self.domain = self.get_kwargs("domain") or DEFAULT_IDEAS_DOMAIN
        self.quantity = self.get_kwargs("quantity") or DEFAULT_IDEAS_QUNATITY
        self.initialize_ideas()
    
    def initialize_ideas(self):
        self.history_ideas = self.__read_ideas_history__(ignore_not_found=True) or []
    
    # @override
    def initialize_projects(self):
        pass
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_ideas", file=IDEAS_LOG_FILE)
    
    # @override
    def build_system_prompt_context(self, **kwargs):
        return {
            "ideas_history": self.__idea_history_names__() or None,
            "language": self.language,
        }
    
    # @override
    def system_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_ideas_prompts", file=SYSTEM_PROMPT_TEMPLATE)
    
    # @override
    def build_user_prompt_context(self, **kwargs):
        return {
            "domain": self.domain,
            "quantity": self.quantity,
            "ideas_history": self.__idea_history_names__() or None,
            "language": self.language,
        }
    
    # @override
    def user_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_ideas_prompts", file=USER_PROMPT_TEMPLATE)
    
    # @override
    def agent_temperature(self):
        return 0.8 # high ideas
    
    # @override
    def __pre_execute__(self, **kwargs):
        pass
    
    # @override
    def clean_response(self, raw_response, **kwargs):
        # extract idea blocks
        pattern_block = re.compile(
            r"^####\s+\[IDEA_(\d+)\]\s*(.*?)\r?\n(.*?)(?=^####\s+\[IDEA_\d+\]\s*|\Z)",
            re.MULTILINE | re.DOTALL,
        )
        ideas_blocks = pattern_block.findall(raw_response)
        
        # check history ideas
        history_ideas = []
        if self.history_ideas and isinstance(self.history_ideas, tuple):
            history_ideas = list(self.history_ideas[1]) if len(self.history_ideas) > 1 and isinstance(self.history_ideas[1], list) else list(self.history_ideas)
            
        elif self.history_ideas:
            history_ideas = list(self.history_ideas)
        history_ideas = [ i for i in history_ideas if isinstance(i, dict) ]
        
        # find all idea names match prefix from AI response
        ideas = []
        for idea_index, raw_name, raw_desc in ideas_blocks:
            clean_idea_name = raw_name.replace("**", "").strip()
            clean_idea_desc = raw_desc.strip()
            if not clean_idea_name:
                continue
            
            # Regex lines to dynamically capture technical_codename and brand_name values
            # Scans for the pattern line ending with the plain value payload
            len_technical_codenames, technical_codenames = regex_extract_by_name_pair_tags(
                tag_name="TECHNICAL_CODENAME", data=clean_idea_desc,
            )
            len_branch_names, branch_names = regex_extract_by_name_pair_tags(
                tag_name="BRAND_NAME", data=clean_idea_desc,
            )
            
            # Extract and fallback to clean_idea_name if AI omits the string token
            technical_codename = (
                technical_codenames[0].strip()
                if len_technical_codenames > 0
                else clean_idea_name
            )
            brand_name = (
                branch_names[0].strip() if len_branch_names > 0 else clean_idea_name
            )
            
            # idea unique identity
            unique_id = hashlib.md5(clean_idea_name.encode("utf-8")).hexdigest()[:12]
            idea_id = f"idea_{unique_id}"
            self.logger.info(f"- 🎯 Idea: {idea_id} | [{clean_idea_name}]")
            abs_idea_file = self.__storage_path__(storage_name="relative_ideas", file=f"{idea_id}.md")
            idea_file = self.__storage_path__(storage_name="storage_ideas", file=f"{idea_id}.md")
            idea_content = f"# {clean_idea_name}\n\n{clean_idea_desc}"
            idea_item = {
                "id": idea_id,
                "idea": clean_idea_name,
                "technical_codename": technical_codename,
                "brand_name": brand_name,
                "file": abs_idea_file
            }
            ideas.append({
                **idea_item,
                "physical_file": idea_file,
                "content": idea_content
            })
            history_ideas.append({ **idea_item })
        self.history_ideas = history_ideas
                
        self.logger.info(f"[ 🎯 INFO ] Found / Extracted: {len(ideas)} new ideas.")
        return ideas
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("❌ Invalid AI raw response. Not a valid JSON format data.")
        
        # export new ideas as md files
        for idea in response_data:
            write_file(
                file=idea.get("physical_file"),
                data=idea.get("content")
            )
        
        # update ideas history
        write_json_file(
            file=self.__ideas_history_path__(),
            json_data=self.history_ideas
        )
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.__output_storage_path__(storage_name="output_ideas", file=IDEAS_OUTPUT_FILE),
                data=raw_response
            )
            
def execute_idea_generator(args: dict, **unknown_args):
    # to simple object namespace
    if isinstance(args, dict):
        args = SimpleNamespace(**args)

    # execute
    EnterpriseIdeaGeneratorAgent(
        domain=args.domain if hasattr(args, "domain") else DEFAULT_IDEAS_DOMAIN,
        quantity=args.quantity if hasattr(args, "quantity") else DEFAULT_IDEAS_QUNATITY,
        **unknown_args,
    ).execute()
    
if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--domain", default=DEFAULT_IDEAS_DOMAIN, type=str, help="Domain to find ideas")
        parser.add_argument("--quantity", default=DEFAULT_IDEAS_QUNATITY, type=int, help="The number of ideas")
    
    args, unknown_args = parse_args(
        description="💡 EnterpriseIdeaGeneratorAgent",
        parser_callback=add_known_arguments
    )
    execute_idea_generator(args=args, unknown_args=unknown_args)
