import pyphen

def syllable_breakdown(word):
    dic = pyphen.Pyphen(lang='en')  # Create a Pyphen instance for English language

    syllables = dic.inserted(word).split('-')
    return syllables

# Example usage:
word = "Prerequisite"
syllables = syllable_breakdown(word)
print(word)
print(syllables)
