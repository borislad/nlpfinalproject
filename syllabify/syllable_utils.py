import nltk
import speech_recognition as sr

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



# Example usage
input_text = input("Enter a text: ")
syllable_breakdown(input_text)