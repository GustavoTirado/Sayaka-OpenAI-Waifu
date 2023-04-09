import openai
import speech_recognition as sr
from pyttsx3 import init
import json

with open('config.json', 'r') as f:
    config = json.load(f)

# Set OpenAI API key
openai.api_key = config['openai_api_key']

conversation = ""

# Initialize text-to-speech engine
def speak(message):
    engine = init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[config['language']].id)
    engine.say(message)
    engine.runAndWait()

mode = input("How do you want to interact with Sayaka? (Type 'text' or 'voice'): ")
while mode not in ["text", "voice"]:
    print("Invalid option, please try again.")
    mode = input("How do you want to interact with Sayaka? (Type 'text' or 'voice'): ")
print("Selected interaction mode:", mode)

i=1
while(i != 0):
    answer = ""
    question = ""
    conversation  = ""
    
    if mode == "text":
        question = input("YOU:")
        if "switch to voice mode" in question:
            mode = "voice"
            print("Interaction mode switched to voice")
            continue
        conversation += "YOU:" + question + "\nSayaka:"
    elif mode == "voice":
        # Initialize speech recognition engine
        r = sr.Recognizer()
        
        # Use default microphone as audio source
        with sr.Microphone() as source:
            print("Speak what you want to say to Sayaka...")
            # Adjust microphone energy threshold to ambient noise level
            r.adjust_for_ambient_noise(source)
            # Capture speech from microphone
            audio = r.listen(source)
            print("Processing...")
            try:
                # Recognize speech using Google Speech Recognition API
                question = r.recognize_google(audio, language='en-US')
                print("YOU: " + question)
                if "switch to text mode" in question:
                    mode = "text"
                    print("Interaction mode switched to text")
                    continue
                conversation += "YOU: " + question + "\nSayaka:"
            except sr.UnknownValueError:
                print("Sorry, I could not understand what you said")
                continue
    
    response = openai.Completion.create(
        model=config['language_model'],
        prompt=config['personality'] + conversation,
        temperature=config['temperature'],
        max_tokens=config['max_tokens'],
        top_p=1,
        n=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n","YOU:","Sayaka:"]
    )
    answer = response.choices[0].text.strip()
    speak(answer)
    conversation += answer
    print("Sayaka:" + answer + "\n")