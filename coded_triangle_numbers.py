import math


def is_triangle(number):
    triangle_number = int(math.sqrt((number * 2)))
    return int(triangle_number * (triangle_number + 1) * 0.5)


words_txt = open("p042_words.txt", "r")
words = words_txt.read().replace('"', '').split(',')
words_txt.close()

alphabet_table = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
    "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
    "X": 24, "Y": 25, "Z": 26,
}

word_value = 0
triangle_word_count = 0
for word in words:
    for letter in word:
        word_value += alphabet_table[letter]
    if word_value == is_triangle(word_value):
        triangle_word_count += 1
    word_value = 0
print(triangle_word_count)