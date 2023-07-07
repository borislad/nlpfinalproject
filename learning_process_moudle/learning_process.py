import csv
import os
from word_verification_module.file_utils import build_file_path
from Learning_Recommendation.Learning_Recommendation import find_highest_value
from word_verification_module.syllable_verification import Syllable_verifaction
from word_generator.random_word import find_words_by_syllable
from word_verification_module.word_verification import word_verification_test

def learning_steps():
    syllable_dict = Syllable_verifaction()
    Syllable_To_Practice = find_highest_value(syllable_dict)
    # NOW NEED TO ADD WITCH FAMILY OF WORDS TO TAKE BASED ON THE Syllable_To_Practice key!!
    Words_to_practice = find_words_by_syllable(Syllable_To_Practice)
    print('The words to practice are:', ', '.join(Words_to_practice))
    word_verification_test(Words_to_practice)
    #ADD plots to show the learning rate...
    print('ADD plots to show the learning rate...')
# learning_steps()