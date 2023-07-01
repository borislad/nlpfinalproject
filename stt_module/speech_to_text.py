import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def speech_to_text(self):

        with sr.Microphone() as source:
            print("Speak something...")
            audio = self.recognizer.listen(source, phrase_time_limit=5)  # Stop listening after 5 seconds

        try:
            text = self.recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            print("Speech recognition service is unavailable. Error: " + str(e))

stt = SpeechToText()
stt.speech_to_text()
