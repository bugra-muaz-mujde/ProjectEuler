

f = open("p022_names.txt", "r")
names = f.readline().replace('"', "").split(',')
names.sort()
f.close()

alphabet_table = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
    "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
    "X": 24, "Y": 25, "Z": 26,
}

name_values_sum = 0
total = 0
for index, name in enumerate(names):
    for letter in name:
        name_values_sum += alphabet_table[letter]
    total += (index + 1) * name_values_sum
    name_values_sum = 0
print(total)