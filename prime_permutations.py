
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


def sequences(sequence, prime_list):
    if sequence + 3330 in prime_list:
        if sequence + 3330 * 2 in prime_list:
            seq = list(str(sequence))
            seq1 = list(str(sequence + 3330))
            seq2 = list(str(sequence + 3330 * 2))
            seq.sort()
            seq1.sort()
            seq2.sort()
            if str(seq) == str(seq2) == str(seq1):
                return True
    return False


primes_to_10000 = sieve_of_sundaram(10**4)
primes_to_1000 = sieve_of_sundaram(10**3)
primes = list(set(primes_to_10000).difference(primes_to_1000))
primes.sort()
for prime in primes:
    if sequences(prime, primes):
        print(prime)
