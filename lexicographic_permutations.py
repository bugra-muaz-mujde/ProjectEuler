
def get_permutation(number):
    permutation = 1
    while number > 1:
        permutation *= number
        number -= 1
    return permutation


number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
millionth_lexicographic_permutation = ""
rank = 999999
for counter in range(10, 0, -1):
    millionth_lexicographic_permutation += str(number_list[int(rank // (get_permutation(counter) / counter))])
    del number_list[int(rank // (get_permutation(counter) / counter))]
    rank = rank % (get_permutation(counter) / counter)

print(millionth_lexicographic_permutation)
