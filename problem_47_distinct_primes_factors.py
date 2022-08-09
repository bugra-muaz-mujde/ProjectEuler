import math


def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def get_prime_divisors(num):
    n = math.ceil(math.sqrt(num))
    divisors = []
    prime_divisors = []
    divisor = 2
    while divisor < n:
        if num % divisor == 0:
            divisors.append(divisor)
            divisors.append(num // divisor)
        divisor += 1
    divisors.sort()
    if divisors:
        for divisor_number in divisors:
            if is_prime(divisor_number):
                prime_divisors.append(divisor_number)
    return prime_divisors


number = 2
while True:
    if len(get_prime_divisors(number)) == 4:
        if len(get_prime_divisors(number + 1)) == 4:
            if len(get_prime_divisors(number + 2)) == 4:
                if len(get_prime_divisors(number + 3)) == 4:
                    print(number)
                    break
    number += 1


