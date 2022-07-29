
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


#  13579 -> 57913 79135 91357 35791


def get_rotations(prime):
    current_index = 0
    rotation = ""
    rotations = [prime]
    for digit in str(prime):
        if int(digit) % 2 == 0:
            return False


print(get_rotations(197))


GOIRBY
