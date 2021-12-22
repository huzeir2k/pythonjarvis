from datetime import datetime

def greet_user():

#this will "greet" the user according to the time it is right now

hour = datetime.now().hour

if (hour >= 6) and (hour < 12):
        speak(f"Good morning, {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon, {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening, {USERNAME}")
speak(f"I am {}. How may I assist you?")