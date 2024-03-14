import autogen
from UserProxyAgent import ProxyAgent
from AssistentAgent import AssistentAgent
from RAGAgent import RAGAgent
import FunctionsDef

class ChatManager:

    def __init__(self, config, termination_msg):
        self.config = config
        self.termination_msg = termination_msg

        # Create agents. Use only user_proxy and chat_manager for simple chat. Add function_caller for calling functions and RAG for retireving information from files
        self.user_proxy = ProxyAgent("User_proxy", self.termination_msg)
        self.chat_manager = AssistentAgent("Manager", self.termination_msg, self.config)
        self.function_caller = AssistentAgent("Function_caller", self.termination_msg, self.config)
        self.RAG = RAGAgent("Files_Retriever", self.termination_msg, self.config)
        
    # Run the groupchat with users question / input
    def start_chat(self, question): 
        # get chat agents 
        user_proxy = self.user_proxy.GetAgent()
        chat_manager = self.chat_manager.GetAgent()
        function_caller = self.function_caller.GetAgent()

        # Initialize groupchat
        groupchat = autogen.GroupChat(
            agents = [user_proxy, chat_manager, self.RAG.GetRetrieveAssistantAgent(), function_caller], 
            messages = [], 
            max_round = 120,
            speaker_selection_method = "auto",
            allow_repeat_speaker = False
        )

        for agent in groupchat.agents:
            agent.reset()

        # Delete function definition for manager config, while chat manager is not capable of function calling
        manager_config = self.config
        manager_config["functions"] = None
        manager = autogen.GroupChatManager(groupchat = groupchat, llm_config = manager_config)
        
        # Register functions to agents. For some reason retrieve_content function had to be registered for agents to work.
        # If you don't want to use the agents using these functions, remove the function registration and also erase the function definition from 'LLM_Config.json'

        self.RAG.GetRetrieveAssistantAgent().register_function(
            function_map={
                "retrieve_content": self.RAG.retrieve_content
            }
        )

        chat_manager.register_function(
            function_map={
                "retrieve_content": self.RAG.retrieve_content
            }
        )
        
        function_caller.register_function(
            function_map={
                "get_date_and_time": FunctionsDef.getDateAndTime
            }
        )
        
        # Start the chat
        user_proxy.initiate_chat(
            manager,
            message = question,
        )