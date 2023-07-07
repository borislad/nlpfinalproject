import csv
import os
import random

from tts_module.text_to_speech import say_text
from word_generator.random_word import select_random_word
from stt_module.stt import STT
from syllabify.syllable_utils import extract_syllables
from word_verification_module.audio_verification import record_audio, compare_audio_files
from word_verification_module.syllable_verification import Syllable_verifaction
from word_verification_module.file_utils import build_file_path
from Learning_Recommendation.Learning_Recommendation import find_highest_value

def word_verification_test():
    syllable_dict= Syllable_verifaction()
    Syllable_To_Practice= find_highest_value(syllable_dict)
    #NOW NEED TO ADD WITCH FAMILY OF WORDS TO TAKE BASED ON THE Syllable_To_Practice key!!

    stt = STT()
    # selected_word = select_random_word()
    selected_word = "Exaggerate"
    while True:
        print("Please pronounce the word: " + selected_word)
        say_text("Please pronounce the word: " + selected_word)
        spoken_word = stt.speech_to_text(selected_word)

        if selected_word is None or spoken_word is None:
            print("Word comparison failed. Please try again.")
            say_text("Word comparison failed. Please try again.")
            continue

        if selected_word.lower() == spoken_word.lower():
            print("Correct word! Lets continue to the next word")
            say_text("Correct word! Lets continue to the next word")
            selected_word = select_random_word()
            break
        else:
            print("Incorrect word! \nlets split the word to syllables...")
            say_text(text="Incorrect word! Please try again. lets split the word to syllables...")
            syllables = extract_syllables(selected_word)
            print("-".join(syllables))
            for syllable in syllables:
                print("Pronounce the syllable:", syllable)
                say_text("Please pronounce the syllable: " + syllable)
                input("Press Enter to record the syllable: ")
                directory_path = "/word_verification_module/syllable_recordings/"
                file_name = syllable + ".wav"
                recorded_syllable_file_path = build_file_path(directory_path, file_name)
                # recorded_syllable_file_path = r"C:\Users\shabi\PycharmProjects\nlpfinalproject\word_verification_module\syllable_recordings/" + syllable + ".wav"
                record_audio(2, recorded_syllable_file_path)
                directory_path = "/word_verification_module/syllables_audio/"
                syllables_audio_file_path = build_file_path(directory_path, file_name)
                # syllables_audio_file_path = r"C:\Users\shabi\PycharmProjects\nlpfinalproject\word_verification_module\syllables_audio/" + syllable + ".wav"
                if compare_audio_files(syllables_audio_file_path, recorded_syllable_file_path):
                    say_text("Correct syllable!")
                    print("Correct syllable!")
                else:
                    say_text("Incorrect syllable!")
                    print("Incorrect syllable!")
                    say_text("The correct syllable is: " + syllable)
                    print("The correct syllable is: ", syllable)


def word_verification(word_to_say):
    stt = STT()
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


