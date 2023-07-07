import csv
import os
from tts_module.text_to_speech import say_text
from word_generator.random_word import select_random_word
from stt_module.stt import STT
from syllabify.syllable_utils import extract_syllables
from word_verification_module.audio_verification import record_audio, compare_audio_files
from word_verification_module.file_utils import build_file_path
from Learning_Recommendation.Learning_Recommendation import read_syllable_dataset_to_dictionary

def Syllable_verifaction():
    syllable_dict = read_syllable_dataset_to_dictionary()
    for syllable in syllable_dict.keys():
        while True:
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
                print("Correct syllable! Lets move to the next one..")
                break
            else:
                say_text("Incorrect syllable!")
                print("Incorrect syllable!")
                say_text("The correct syllable is: " + syllable)
                print("The correct syllable is: ", syllable)
                syllable_dict[syllable]+=1
                if syllable_dict[syllable] == 2: # 5 tries per syllable!!
                    break
        print(syllable_dict)
    return syllable_dict

# Syllable_verifaction()