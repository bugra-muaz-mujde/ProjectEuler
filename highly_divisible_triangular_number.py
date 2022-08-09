import time
import math

start_time = time.time()


def get_count_divisors(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                cnt = cnt + 1
            else:
                cnt = cnt + 2
    return cnt


def is_prime(n):
    if n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


limit = len(str(2**1 * 3**2 * 5**2 * 7**2 * 11**2 * 13*2)) - 1
number = 0
counter = 1

while True:
    number += counter
    if number > 10**limit:
        if get_count_divisors(number) > 500:
            print(number)
            break
    counter += 1
print("--- %s seconds ---" % (time.time() - start_time))