# pip install SpeechRecognition
import speech_recognition as sr
# follow this link: https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error


def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("PLease Say Something ...")

        audio = r.listen(source)

        try:
            print("You Have Said: \n" + r.recognize_google(audio))
        except Exception as e:
            print("Error: " + str(e))


if __name__ == "__main__":
    main()



