import math


def is_prime(n):
    if n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


def is_conjecture(number):
    for possible_prime in range(number - 2, 2, -2):
        if is_prime(possible_prime):
            if number == possible_prime + 2 * (int((math.sqrt(((number - possible_prime) / 2)))) ** 2):
                return True
    return False


counter = 9

while True:
    if not is_prime(counter):
        if not is_conjecture(counter):
            print(counter)
            break
    counter += 2
