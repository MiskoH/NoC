import autogen
from autogen.retrieve_utils import TEXT_FORMATS
import Config
# Import MyProxyAgent to use Voice assistant function
#from MyProxyAgent import MyProxy

# Custom class for creating UserProxyAgent. 
# UserProxyAgent is mostly initiated with information passed from Agents.json config
# You can change the UserProxyAgent from autogen for our vesion of UserProxyAgent to use it as voice assistant
class ProxyAgent:

    def __init__(self, name, termination_msg):

        userProxyConfig = Config.GetAgentConfig(name)
        
        # Commnet this line to use Voice assistant function
        self.userProxyAgent = autogen.UserProxyAgent(
        # Uncommnet this line to use Voice assistant function
        #self.userProxyAgent = MyProxy(
            name=name,
            is_termination_msg = termination_msg,
            system_message = userProxyConfig["prompt"],
            code_execution_config = {
                "use_docker": False
            },
            human_input_mode = userProxyConfig["human_input_mode"],
            default_auto_reply = userProxyConfig["default_auto_reply"]
        )

    def GetAgent(self):
        return self.userProxyAgent