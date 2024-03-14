import autogen
import VoiceAssistant

# Overriding of UserProxyAgent for using as voice assistant.
class MyProxy(autogen.UserProxyAgent):
    
    # The only function we need to override is get_human_input
    def get_human_input(self, prompt: str) -> str:
        # Read the last message from the chat. It should be the answer for users question
        VoiceAssistant.read_answer(self.last_message())

        # Listne for microphone input
        reply = VoiceAssistant.listen_microphone()

        self._human_input.append(reply)
        return reply