import csv
import os

import syllabify.syllable_utils


def read_syllable_dataset_to_dictionary(filename):
    syllable_dict = {}

    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            if i == 0 and row[0].startswith('\ufeff'):
                # Remove BOM character from the first row, if present
                row[0] = row[0][1:]
            key = row[0]
            value = 1
            syllable_dict[key] = value

    # print(syllable_dict)
    return syllable_dict

def find_highest_value(dictionary):
    highest_key = None
    highest_value = float('-inf')

    for key, value in dictionary.items():
        if value > highest_value:
            highest_key = key
            highest_value = value
    print(highest_key, highest_value)
    return highest_key

# syllable_dict = read_syllable_dataset_to_dictionary()
# find_highest_value(syllable_dict)

# Build function to read from the Test_Dataset.csv file the first column and return a list of words


def read_test_dataset_to_list():
    words_list = []

    file_path = os.path.join(os.path.dirname(__file__), '../word_generator/Test_Dataset.csv')

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            if i == 0 and row[0].startswith('\ufeff'):
                # Remove BOM character from the first row, if present
                row[0] = row[0][1:]
            #read the first column and append it to the words_list
            words_list.append(row[0])
    #remove the first row
    words_list.pop(0)
    # print(words_list)
    return words_list

# Build function that going through the words list and writing each syllable of word to syllable_Dataset.csv file
def write_syllable_dataset(words_list):
    for word in words_list:
        extracted_syllables = syllabify.syllable_utils.extract_syllables(word)
        for word_syllable in extracted_syllables:
            #check if syllable is already in the syllable_Dataset.csv file
            syllable_dataset = read_syllable_dataset_to_dictionary()
            if word_syllable.lower() not in syllable_dataset:
                file_path = os.path.join(os.path.dirname(__file__), 'syllable_Dataset.csv')
                with open(file_path, 'a+', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([word_syllable.lower()])


# write_syllable_dataset(read_test_dataset_to_list())