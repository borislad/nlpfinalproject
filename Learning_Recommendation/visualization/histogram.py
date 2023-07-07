from matplotlib import pyplot as plt

my_dict = {
    'ac': 1,
    'com': 2,
    'mod': 3,
    'ate': 4,
    'ne': 5,
    'ces': 6,
    'sit': 7,
    'ex': 8,
    'ag': 9,
    'ger': 10,
    'mit': 11,
    'ig': 12,
    'in': 13,
    'teg': 14,
    'rate': 15,
    'con': 16,
    'science': 17,
    're': 18,
    'si': 19,
    'li': 20,
    'ence': 21,
    'pet': 22,
    'provid': 23,
    'el': 24,
    'eg': 25,
    'ance': 26,
    'plan': 27,
    'a': 28,
    'tion': 29,
    'as': 30,
    'so': 31,
    'ci': 32,
    'ation': 33,
    'ra': 34,
    'reg': 35,
    'u': 36,
    'la': 37,
    'found': 38,
    'beau': 39,
    'ti': 40,
    'ful': 41,
    'suc': 42,
    'cess': 43,
    'grate': 44,
    'source': 45,
    'play': 46,
    'de': 47,
    'vel': 48,
    'op': 49,
    'ment': 50,
    'achieve': 51,
    'move': 52,
    'sess': 53,
    'place': 54
}


#Visualize the data in a histogram to see ammount of syllables the user has to record

plt.hist(my_dict.values())
plt.show()


