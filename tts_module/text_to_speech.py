import os

from gtts import gTTS
import tempfile
import pygame

def say_text(text):
    # Create a temporary file to save the generated audio
    temp_file = tempfile.NamedTemporaryFile(delete=True, dir=None, suffix=".mp3")

    # Initialize gTTS with the desired text
    tts = gTTS(text=text, lang="en")

    # Save the audio to the temporary file
    tts.save(temp_file.name)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(temp_file.name)

    # Play the audio file
    pygame.mixer.music.play()

    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        continue

    # Close the pygame mixer
    pygame.mixer.quit()


def build_file_path(directory, filename):
    # Create the full file path using os.path.join()
    file_path = os.path.abspath(os.getcwd()) + os.path.join(directory, filename)
    return file_path

# import pyttsx3


# def say_text(text):
#     # Initialize pyttsx3 TTS engine
#     engine = pyttsx3.init()
#
#     # Set the desired speech rate
#     engine.setProperty("rate", 150)  # Adjust the value as needed
#     # Say the text
#     engine.say(text)
#
#     engine.runAndWait()

# text = "Shabat Shalom!"
# say_text(text)
