# this is offline version using pyttsx3
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed (words per minute)
    engine.setProperty('volume', 1)  # Max volume
    engine.say(text)
    engine.runAndWait()

speak_text("Hello, this is a text-to-speech conversion using pyttsx3.")