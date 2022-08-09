import time

start_time = time.time()


def sieve_of_sundaram(n):
    k = (n - 2) // 2  # sınır belirliyor
    prime_list = []
    integers_list = [True] * (k + 1)  # sınır kadar dizi oluşturuyor

    for i in range(1, k + 1): # sınır kadar eleman dönüyor.
        j = i
        while i + j + 2 * i * j <= k: # 4 < 50 7 15
            integers_list[i + j + 2 * i * j] = False
            j += 1
    if n > 2:
        prime_list.append(2)
    for i in range(1, k + 1):
        if integers_list[i]:
            prime_list.append(2 * i + 1)
    return prime_list


def get_rotations(prime):
    rotations = [prime] * len(prime)
    for digit_position, digit in enumerate(prime):
        if int(digit) % 2 == 0 and prime != "2":
            return None
        index = digit_position
        for rotation in range(0, len(rotations)):
            prime = rotations[rotation]
            rotations[rotation] = prime[: index] + digit + prime[index + 1:]
            if index == 0:
                index = len(prime) - 1
            else:
                index -= 1
    return rotations


def is_circular_prime(rotations, prime_list):
    if rotations:
        for rotation in rotations:
            if int(rotation) not in prime_list:
                return False
    else:
        return False
    return True


primes = sieve_of_sundaram(1000000)
circular_prime_count = 0

for prime in primes:
    if is_circular_prime(get_rotations(str(prime)), primes):
        circular_prime_count += 1

print(circular_prime_count)
print("--- %s seconds ---" % (time.time() - start_time))