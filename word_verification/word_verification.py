import csv
import random

from word_generator.random_word import select_random_word
from stt_module.speech_to_text import speech_to_text

def word_verification_test():
    selected_word = select_random_word()
    spoken_word = speech_to_text()

    if selected_word is None or spoken_word is None:
        print("Word comparison failed. Please try again.")

    if selected_word[0].lower() == spoken_word.lower():
        print("Correct word!")
    else:
        print("Incorrect word!")

word_verification_test()