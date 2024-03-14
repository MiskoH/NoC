from ChatManager import ChatManager
import Config
# Import voice assistant if you want to try the functionality of starting the chat by voice. 
#import VoiceAssistant

# Set the question for starting the Chat. This definition is not used with assistant
#PROBLEM = "What is the date today?"
PROBLEM = "What time is it now?"
#PROBLEM = "Hey. I'd like to ask, what Accenture is?"

# Definition of termination message. It's inly used when UserProxyAgent is set for TERMINATE human_input mode
termination_msg = lambda x: isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()

# Initiate groupchat class
groupChat = ChatManager(Config.GetLLMConfig(), termination_msg)

# Start the chat. Comment this line if you want to use voice assistant
groupChat.start_chat(PROBLEM)

# Uncomment this code to use voide assistant
"""
def runListener():
    # Listen until wake word (Frank or Frankie) is used
    while True:
        print("Listening for 'Hey Frank'...")
        # Listen for microphone input
        wake_word = VoiceAssistant.listen_microphone().lower()
        if "frank" in wake_word or "frankie" in wake_word:
            # Start the chat with user input
            groupChat.start_chat(wake_word)
            
runListener()
"""