import math


def get_pentagonal_number(n):
    return int((n * (3 * n - 1)) * 0.5)


j_cursor = 1
k_cursor = 3
while True:
