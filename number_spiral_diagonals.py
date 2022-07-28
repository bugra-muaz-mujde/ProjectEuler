
sum_of_diagonals = 1
current_diagonal_number = 1
for layer in range(2, 1001, 2):
    for corner in range(4):
        current_diagonal_number += layer
        sum_of_diagonals += current_diagonal_number
print(sum_of_diagonals)

