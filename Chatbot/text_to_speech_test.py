# pip install gTTs
from gtts import gTTS

tts = gTTS(text="Hello Friends, How are you?", lang='en')
tts.save("convertedTEXT.mp3")
print("Text Converted Successfully ... ")