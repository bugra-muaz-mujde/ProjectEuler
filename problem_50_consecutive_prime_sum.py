import math


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


primes = sieve_of_sundaram(10**6)
counter = 0
index = 1
sum_of_primes = 0
term_count = 0
max_term_count = 21
max_prime = 953
while index < len(primes):
    sum_of_primes += primes[counter]
    term_count += 1
    counter += 1
    if sum_of_primes in primes:
        if max_term_count < term_count:
            max_term_count = term_count
            max_prime = sum_of_primes
    if sum_of_primes >= primes[len(primes) - 1]:
        if max_term_count > term_count + 5:
            break
        sum_of_primes = 0
        counter = index
        index += 1
        term_count = 0

print(max_prime)