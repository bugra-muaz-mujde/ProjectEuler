
concatenating_positive_integers = ""
number = 1
while len(concatenating_positive_integers) <= 1000000:
    concatenating_positive_integers += str(number)
    number += 1

result = 1
for exp in range(7):
    result *= int(concatenating_positive_integers[10**exp - 1])
print(result)