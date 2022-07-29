import math


def get_count_divisors(n):
    count_divisors = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            count_divisors += 1
    return count_divisors


triangle_number = 0
current_number = 1
lower_limit = 2**100
while True:
    triangle_number += current_number
    if triangle_number > 5000000:
        if get_count_divisors(triangle_number) + 1 > 500:
            print(triangle_number)
    current_number += 1
    print(current_number)
