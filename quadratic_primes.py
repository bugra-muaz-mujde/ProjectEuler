
def is_prime(n):
    if n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


def quadratic_formula(n, a, b):
    return int(n**2 + (a * n) + b)


def count_primes(a, b):
    count = 0
    consecutive = True
    n = 0
    while consecutive:
        if consecutive:
            if is_prime(quadratic_formula(n, a, b)):
                count += 1
            else:
                consecutive = False
        n += 1
    return count


for n in range(70):
    print(is_prime(quadratic_formula(n, 67, 997)))

max_number_of_primes = 0
max_a = 0
max_b = 0
for a in range(0, -1000, -1):
    for b in range(1000, 1, -1):
        incredible = count_primes(a, b)
        if a == -61 and b == 997:
            print(incredible)
        if max_number_of_primes < incredible:
            max_number_of_primes = incredible
            max_a = a
            max_b = b

