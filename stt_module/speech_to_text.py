import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source, phrase_time_limit=5)  # Stop listening after 5 seconds

    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print("Speech recognition service is unavailable. Error: " + str(e))

speech_to_text()
