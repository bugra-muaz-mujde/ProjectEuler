def sieve_of_sundaram(n):
    k = (n - 2) // 2  # sınır belirliyor
    prime_list = []
    integers_list = [True] * (k + 1)  # sınır kadar dizi oluşturuyor

    for i in range(1, k + 1):  # sınır kadar eleman dönüyor.
        j = i
        while i + j + 2 * i * j <= k:  # 4 < 50 7 15
            integers_list[i + j + 2 * i * j] = False
            j += 1
    if n > 2:
        prime_list.append(2)
    for i in range(1, k + 1):
        if integers_list[i]:
            prime_list.append(2 * i + 1)
    return prime_list


def is_odd(prime_number):
    for prime_digit in str(prime_number):
        if int(prime_digit) % 2 == 0:
            return False
    return True


def is_all_prime(prime_list, primes):
    prime_index = 0
    for prime in prime_list:
        while True:
            if prime == primes[prime_index]:
                break
            if prime < primes[prime_index]:
                return False
            prime_index += 1
        prime_index = 0
    return True


primes = sieve_of_sundaram(10**7)

left_list = []
right_list = []
sum_of_primes = 0
for prime in primes:
    if is_odd(prime):
        if prime > 10:
            for digit in range(len(str(prime)) - 1):
                left_list.append(
                    prime % 10 ** (len(str(prime)) - digit - 1)
                )
                right_list.append(
                    prime // 10 ** (digit + 1)
                )
            left_list.reverse()
            if is_all_prime(left_list, primes) and is_all_prime(right_list, primes):
                sum_of_primes += prime
    left_list = []
    right_list = []
print(sum_of_primes)
