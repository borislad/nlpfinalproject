import csv
import os

def read_syllable_dataset_to_dictionary():
    syllable_dict = {}

    file_path = os.path.join(os.path.dirname(__file__), 'syllable_Dataset.csv')

    with open(file_path, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            if i == 0 and row[0].startswith('\ufeff'):
                # Remove BOM character from the first row, if present
                row[0] = row[0][1:]
            key = row[0]
            value = 0
            syllable_dict[key] = value

    print(syllable_dict)
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