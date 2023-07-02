import csv
import random

from word_generator.random_word import select_random_word
from stt_module.speech_to_text import speech_to_text
from syllabify.syllable_utils import extract_syllables

def word_verification_test():
    stt = speech_to_text()
    selected_word = select_random_word()
    while True:
        spoken_word = stt.speech_to_text(selected_word[0])

        if selected_word is None or spoken_word is None:
            print("Word comparison failed. Please try again.")
            continue

        if selected_word[0].lower() == spoken_word.lower():
            print("Correct word!")
            break
        else:
            print("Incorrect word!")
            print("lets split the word to syllables...")
            print(extract_syllables(selected_word[0]))
            for syllable in extract_syllables(selected_word[0]):
                print("Pronounce the syllable:", syllable)
                spoken_syllable = stt.speech_to_text(syllable)
                if spoken_syllable.lower() == syllable.lower():
                    print("Correct syllable!")
                else:
                    print("Incorrect syllable!")
                    print("The correct syllable is: ", syllable)

def word_verification(word_to_say):
    stt = speech_to_text()
    spoken_word = stt.speech_to_text(word_to_say)

    if word_to_say is None or spoken_word is None:
        print("Word comparison failed. Please try again.")
        return False

    if word_to_say.lower() == spoken_word.lower():
        print("Correct word!")
        return True
    else:
        print("Incorrect word!")
        return False

word_verification_test()