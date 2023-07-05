import speech_recognition as sr

from tts_module.text_to_speech import say_text


class STT:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    # def speech_to_text(self):
    #
    #     with sr.Microphone() as source:
    #         print("Speak something...")
    #         audio = self.recognizer.listen(source, phrase_time_limit=10)  # Stop listening after 5 seconds
    #
    #     try:
    #         text = self.recognizer.recognize_google(audio)
    #         print("You said: " + text)
    #         # Extract the first word
    #         first_word = text.split()[0]
    #         return first_word
    #     except sr.UnknownValueError:
    #         print("Sorry, I could not understand your speech.")
    #     except sr.RequestError as e:
    #         print("Speech recognition service is unavailable. Error: " + str(e))

    def speech_to_text(self, word_to_say):

        with sr.Microphone() as source:
            # print("Say " + word_to_say + "...")
            audio = self.recognizer.listen(source, phrase_time_limit=5)  # Stop listening after 5 seconds

        try:
            text = self.recognizer.recognize_google(audio)
            say_text("You said: " + text)
            # print("You said: " + text)
            # Extract the first word
            first_word = text.split()[0]
            return first_word
        except sr.UnknownValueError:
            say_text("Sorry, I could not understand your speech.")
            # print("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            print("Speech recognition service is unavailable. Error: " + str(e))
