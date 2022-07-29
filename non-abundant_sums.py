import math


def get_sum_of_divisors(num):
    n = math.ceil(math.sqrt(num))
    sum_of_divisors = 1
    divisor = 2
    while divisor < n:
        if num % divisor == 0:
            sum_of_divisors += divisor
            sum_of_divisors += num // divisor
        divisor += 1
    return sum_of_divisors


def is_abundant(abundant):
    if get_sum_of_divisors(abundant) > abundant:
        return True
    else:
        return False


abundant_list = []
list_of_sum_of_two_abundant_numbers = []
for number in range(2, 28124):
    if is_abundant(number):
        abundant_list.append(number)

for x in range(0, len(abundant_list)):
    for y in range(x, len(abundant_list)):
        sum_of_two_abundant_nums = abundant_list[x] + abundant_list[y]
        if sum_of_two_abundant_nums <= 28123:
            list_of_sum_of_two_abundant_numbers.append(sum_of_two_abundant_nums)


all_integers = [0] * 28123
count = 1
for index in range(len(all_integers)):
    all_integers[index] = count
    count += 1

print(len(list_of_sum_of_two_abundant_numbers))
for index in range(len(list_of_sum_of_two_abundant_numbers)):
    try:
        all_integers.remove(list_of_sum_of_two_abundant_numbers[index])
    except:
        pass
    print(index)

print(sum(all_integers))