from gtts import gTTS
import tempfile
import pygame

def say_text(text):
    # Create a temporary file to save the generated audio
    temp_file = tempfile.NamedTemporaryFile(delete=True)

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


text = "ate"
say_text(text)
