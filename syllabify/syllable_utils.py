import nltk
# nltk.download('punkt')
import speech_recognition as sr
import pyphen

# Initialize the NLTK syllable tokenizer
# nltk.download('punkt')
syllable_tokenizer = nltk.tokenize.SyllableTokenizer()
recognizer = sr.Recognizer()

def syllable_breakdown(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Break down each word into syllables
    syllables = []
    for word in words:
        syllables.extend(syllable_tokenizer.tokenize(word))

    # Interact with the user to pronounce the syllables
    for syllable in syllables:
        print("Pronounce the syllable:", syllable)


def extract_syllables(text):
    # Load the English hyphenation dictionary
    dic = pyphen.Pyphen(lang='en')

    # Tokenize text into words
    words = text.split()

    syllables = []
    for word in words:
        # Extract syllables for each word
        word_syllables = dic.inserted(word).split("-")
        syllables.extend(word_syllables)
    # print(syllables)
    return syllables


# input_text = input("Enter a text: ")
# syllable_breakdown(input_text)
# extract_syllables(input_text)
