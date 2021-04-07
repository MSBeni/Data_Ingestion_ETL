# pip install
# sudo apt-get update && sudo apt-get install espeak
import pyttsx3

engine = pyttsx3.init()

engine.say("hello friends how are you? Are you ready for a small game?")
engine.setProperty('rate', 120)
engine.setProperty('volume', 0.9)
engine.runAndWait()
