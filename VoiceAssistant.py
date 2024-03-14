import pyttsx3
from whisper_mic import WhisperMic

# Initializing pyttsx3
listening = True
engine = pyttsx3.init()

# Customizing The output voice
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
        
def listen_microphone():
    result = mic.listen()
    print (result)
    return result

def read_answer(assistant_reply):
    print(f"Assistant: {assistant_reply}")
    engine.setProperty('rate', 120)
    engine.setProperty('volume', volume)
    engine.setProperty(
        'voice', "Microsoft Zira Mobile")
    engine.say(assistant_reply)
    engine.runAndWait()
    
# You can find other models on WhisperMic github page.
mic = WhisperMic(model="small", dynamic_energy=1000)



