import pyttsx3
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine pyttsx3.init('sapi5')

# set rate
engine.setProperty('rate', 190)

# set volume
engine.setProperty('volume', 1.0)

# set voice

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


# tts conversion

def speak(text):
    #this is used to output audio whenever a string of text is passed into it

    engine.say(text)
    engine.runAndWait()

