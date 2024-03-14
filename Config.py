import autogen
from autogen.retrieve_utils import TEXT_FORMATS
import json

# Loading the donfig

llm_config_list = autogen.config_list_from_json(
    "Configs/LLM_ConfigList.json",
    file_location=".",
    filter_dict={
        "model": ["gpt-3.5-turbo"],
    },
)

# Returns content of 'LLM_ConfigList.json'
def GetLLMConfigList():
     return llm_config_list

# Returns content of 'LLM_Config.json' with added LLM_ConfigList
def GetLLMConfig():
    with open('Configs/LLM_Config.json', 'r') as file:
        llm_config = json.load(file)
    
    llm_config["config_list"] = llm_config_list

    return llm_config

# Returns Agent configs
def GetAgentConfig(AgentName):
    with open('Configs/Agents.json', 'r') as file:
            AgentsConfig = json.load(file)

    return AgentsConfig[AgentName]