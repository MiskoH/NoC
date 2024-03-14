from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.retrieve_utils import TEXT_FORMATS
import chromadb
import Config

# Agent for retrieving documents
class RAGAgent:

    def __init__(self, name, termination_msg, config):
        assistantConfig = Config.GetAgentConfig(name)

        # This agent will be added into groupchat in 'ChatManager.py'
        self.assistant = RetrieveAssistantAgent(
            name = name,
            is_termination_msg = termination_msg,
            system_message = assistantConfig["prompt"],
            llm_config = config
        )

        # This agent is not added to the groupchat, but is responsible for retrieving the information. The agent is used in retrieve_content function on lien 43
        self.ragproxyagent = RetrieveUserProxyAgent(
            name = assistantConfig["proxy_name"],
            is_termination_msg = termination_msg,
            system_message = assistantConfig["proxy_prompt"],
            code_execution_config = {
                "use_docker": False
            },
            retrieve_config={
                "task": "qa",
                "docs_path": assistantConfig["paths"],
                "chunk_token_size": 1000,
                "model": config["config_list"][0]["model"],
                "client": chromadb.PersistentClient(path="/tmp/chromadb"),
                "collection_name": "groupchat",
                "get_or_create": True,
            },
        )

        self.ragproxyagent.reset()
    
    # Definition of content retrieving function
    def retrieve_content(self, message, n_results=3):
        self.ragproxyagent.n_results = n_results  # Set the number of results to be retrieved.
        # Check if we need to update the context.
        update_context_case1, update_context_case2 = self.ragproxyagent._check_update_context(message)
        if (update_context_case1 or update_context_case2) and self.ragproxyagent.update_context:
            self.ragproxyagent.problem = message if not hasattr(self.ragproxyagent, "problem") else self.ragproxyagent.problem
            _, ret_msg = self.ragproxyagent._generate_retrieve_user_reply(message)
        else:
            ret_msg = self.ragproxyagent.generate_init_message(message, n_results=n_results)
        return ret_msg if ret_msg else message
    
    def GetRetrieveAssistantAgent(self):
        return self.assistant

