import csv
import os
import random
from word_generator.random_word import select_random_word
from stt_module.stt import STT
from syllabify.syllable_utils import extract_syllables
from word_verification.audio_verification import record_audio, compare_audio_files


def word_verification_test():
    stt = STT()
    # selected_word = select_random_word()
    selected_word = "Exaggerate"
    while True:
        spoken_word = stt.speech_to_text(selected_word)

        if selected_word is None or spoken_word is None:
            print("Word comparison failed. Please try again.")
            continue

        if selected_word.lower() == spoken_word.lower():
            print("Correct word!")
            break
        else:
            print("Incorrect word!")
            print("lets split the word to syllables...")
            syllables = extract_syllables(selected_word)
            print("-".join(syllables))
            for syllable in syllables:
                print("Pronounce the syllable:", syllable)
                input("Press Enter to record the syllable: ")
                # TODO: add a recording for the syllable and validation against it
                directory_path = "/word_verification/syllable_recordings/"
                file_name = syllable + ".wav"
                recorded_syllable_file_path = build_file_path(directory_path, file_name)
                # recorded_syllable_file_path = r"C:\Users\shabi\PycharmProjects\nlpfinalproject\word_verification\syllable_recordings/" + syllable + ".wav"
                record_audio(2, recorded_syllable_file_path)
                directory_path = "/word_verification/syllables_audio/"
                syllables_audio_file_path = build_file_path(directory_path, file_name)
                # syllables_audio_file_path = r"C:\Users\shabi\PycharmProjects\nlpfinalproject\word_verification\syllables_audio/" + syllable + ".wav"
                if compare_audio_files(syllables_audio_file_path, recorded_syllable_file_path):
                    print("Correct syllable!")
                else:
                    print("Incorrect syllable!")
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


def build_file_path(directory, filename):
    # Create the full file path using os.path.join()
    file_path = os.path.abspath(os.getcwd()) + os.path.join(directory, filename)
    return file_path
