def is_prime(n):
    if n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


def replace(number):
    digits_of_number = ""
    digits_of_number += str(number)[:1]
    digits_of_number += "3"
    return int(digits_of_number)


numbers = set([])

for count in range(10, 100):
    numbers.add(replace(count))


numbers = list(numbers)
numbers.sort()
print(numbers)


primes = []

for i in range(56003, 56994, 10):
    if is_prime(i):
        print(i)