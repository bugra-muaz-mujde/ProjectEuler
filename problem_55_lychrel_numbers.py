
def get_reverse(number):
    return int(str(number)[::-1])


def is_palindromic(number):
    if str(number) == str(number)[::-1]:
        return True
    return False


def is_lychrel_number(number):
    limit = 50
    iterate_number = 0
    while iterate_number < limit:
        number = number + get_reverse(number)
        if is_palindromic(number):
            return False
        iterate_number += 1
    return True


lychrel_number_count = 0

for num in range(1, 10001):
    if is_lychrel_number(num):
        lychrel_number_count += 1

print(lychrel_number_count)
