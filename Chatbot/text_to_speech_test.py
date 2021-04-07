# pip install gTTs
from gtts import gTTS

tts = gTTS(text="Hello Friends, How are you?", lang='en')
tts.save("converted_text.wav")
print("Text Converted Successfully ... ")