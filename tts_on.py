from gtts import gTTS
import os

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    os.system("start speech.mp3")  # For Windows. Use 'afplay' on macOS, 'mpg123' on Linux

speak_text("Hello, this is a text-to-speech conversion using gTTS.remember that,you will be the one who cant be replaced by AI,so be the best version of yourself and be the best in your field.")  # Example text to convert to speech