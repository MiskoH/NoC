import autogen
from autogen.retrieve_utils import TEXT_FORMATS
import Config

# Custom class for creating simple Autogen Assistant agent. 
# Assistant agent is mostly initiated with information passed from Agents.json config
class AssistentAgent:

    def __init__(self, name, termination_msg, config):
        
        assistantConfig = Config.GetAgentConfig(name)

        self.assistentAgent = autogen.AssistantAgent(
            name = name,
            is_termination_msg = termination_msg,
            system_message = assistantConfig["prompt"],
            llm_config = config
        )

        self.assistentAgent.reset()

    def GetAgent(self):
        return self.assistentAgent