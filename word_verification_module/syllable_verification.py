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
    if not syllables_dataset_audio_exist():
        print("Some syllables dataset audio files missing. Please run the syllables dataset audio generator.")
        syllables_dataset_audio_generator()
    syllable_dict = read_syllable_dataset_to_dictionary("test_syllable_Dataset.csv")
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
                syllable_dict[syllable] += 1
                if syllable_dict[syllable] == 5:  # 5 tries per syllable!!
                    break
        print(syllable_dict)
    return syllable_dict


# TODO: Build function that loops through the syllables and asks the user to pronounce them and record them

# then compare the recorded syllable to the syllable audio file
# if the user pronounces the syllable correctly, move to the next syllable
# if the user pronounces the syllable incorrectly, repeat the syllable 5 times
# if the user pronounces the syllable incorrectly 5 times, move to the next syllable

def syllables_dataset_audio_generator():
    syllable_dict = read_syllable_dataset_to_dictionary("syllable_Dataset.csv")
    for syllable in syllable_dict.keys():
        directory_path = "/word_verification_module/syllables_audio/"
        file_name = syllable + ".wav"
        syllables_audio_file_path = build_file_path(directory_path, file_name)
        if os.path.isfile(syllables_audio_file_path):
            continue
        else:
            print("Pronounce the syllable:", syllable)
            say_text("Please pronounce the syllable: " + syllable)
            input("Press Enter to record the syllable: ")
            record_audio(2, syllables_audio_file_path)
    return syllable_dict


# Check if all sylables from syllable dataset are recorded
def syllables_dataset_audio_exist():
    syllable_dict = read_syllable_dataset_to_dictionary("syllable_Dataset.csv")
    for syllable in syllable_dict.keys():
        directory_path = "/word_verification_module/syllables_audio/"
        file_name = syllable + ".wav"
        syllables_audio_file_path = build_file_path(directory_path, file_name)
        if not os.path.isfile(syllables_audio_file_path):
            return False
    return True