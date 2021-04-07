# pip install SpeechRecognition
# sudo apt-get install portaudio19-
# follow this link: https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error
import speech_recognition as sr



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



