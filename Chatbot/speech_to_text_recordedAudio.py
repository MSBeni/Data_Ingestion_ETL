# pip install SpeechRecognition
# sudo apt-get install portaudio19-
# follow this link: https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error
import speech_recognition as sr


def main():
    # recorded_audio.wav
    sound = 'converted_text.wav'
    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)

        print("Converting Audio File to Text ...")

        audio = r.listen(source)

        try:
            print("Converted Audio is: \n" + r.recognize_google(audio))
        except Exception as e:
            print("Error: " + str(e))


if __name__ == "__main__":
    main()



