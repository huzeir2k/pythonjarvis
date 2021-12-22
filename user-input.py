import speech_recognition as sr
from random import choice
from utils import opening_text


def take_user_input():

#this will take in the user's input, then it recognizes the command via speech_recognition and then converts it back into text

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("I'm listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

try:
    print("Attempting to recognize command...")
    print("Searching through Google...")
    query = r.recognize_google(audio, language="en-us")
    if not 'exit' in query or 'stop' in query:
        speak(choice(opening_text))
    else:
        hour = datetime.now().hour
        if hour >= 21 and hour < 6:
            speak("Good night! Shutting off...")
        else:
            speak("Shutting off...")
        exit()
    except Exception:
        speak("I apologize; the command you've given to me is unrecognizable. Please try again!")
        query = "None"
        return query
