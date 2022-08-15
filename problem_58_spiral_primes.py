
def is_prime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


prime_counter = 0
number_counter = 1
current_diagonal_number = 1
layer = 2
while True:
    for corner in range(4):
        current_diagonal_number += layer
        number_counter += 1
        if is_prime(current_diagonal_number):
            prime_counter += 1
    if float(prime_counter) / number_counter < 0.1:
        print(layer + 1)
        break
    layer += 2
