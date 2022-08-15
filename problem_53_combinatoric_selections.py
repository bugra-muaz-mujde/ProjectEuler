
def get_factorial(n):
    if n == 0:
        return 1
    else:
        product = 1
        for number in range(1, n + 1):
            product *= number
        return product


def get_combinatorics(n, r):
    return get_factorial(n) // (get_factorial(r) * get_factorial(n - r))


counter = 0
for n_value in range(1, 101):
    for sub_n_value in range(1, n_value + 1):
        if get_combinatorics(n_value, sub_n_value) > 10**6:
            counter += 1
print(counter)
