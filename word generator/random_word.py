import csv
import random

import csv
import random


def select_random_word():
    # Open the CSV file
    with open('Test_Dataset.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Check if the data list has enough rows
    if len(data) <= 1:
        return None

    # Generate a random number between 1 and the number of rows in the CSV file
    random_number = random.randint(1, len(data) - 1)

    # Select the row based on the random number
    selected_word = data[random_number]
    selected_word_string = ', '.join(selected_word)
    print(selected_word_string)
    return selected_word

select_random_word()