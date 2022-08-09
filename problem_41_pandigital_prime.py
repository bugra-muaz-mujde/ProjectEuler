
def is_prime(n):
    if n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


def get_permutation(number):
    permutation = 1
    while number > 1:
        permutation *= number
        number -= 1
    return permutation


def get_pandigital_number(rank, number_list):
    pandigital_number = ""
    for counter in range(len(number_list), 0, -1):
        pandigital_number += str(number_list[int(rank // (get_permutation(counter) / counter))])
        del number_list[int(rank // (get_permutation(counter) / counter))]
        rank = rank % (get_permutation(counter) / counter)
    if int(pandigital_number[-1]) % 2 == 0:
        return 0
    return int(pandigital_number)


largest_prime = 0
numbers = [1, 2]
for digit_count in range(2, 10):
    for count in range(get_permutation(digit_count)):
        pandigital = get_pandigital_number(count, list.copy(numbers))
        if is_prime(pandigital):
            if largest_prime < pandigital:
                largest_prime = pandigital
    numbers.append(digit_count + 1)

print(largest_prime)