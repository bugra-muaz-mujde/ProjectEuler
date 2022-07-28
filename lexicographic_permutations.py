
lexicographic_permutations = []

first_permutation = "0123456789"
lexicographic_permutations.append(first_permutation)

for position in range(2, len(first_permutation)):
    print(first_permutation[1:position] + "0" + first_permutation[position:])

