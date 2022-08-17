import math


def is_abundant(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n/i])
    return sum(list(set(divs))) > n


abundant_numbers = []
sum_of_two_abundants = []
for number in range(1, 28124):
    if is_abundant(number):
        abundant_numbers.append(number)

for abundant in abundant_numbers:
    for sub_abundant in abundant_numbers:
        if abundant + sub_abundant < 28123:
            sum_of_two_abundants.append(abundant + sub_abundant)


sum_of_two_abundants = list(set(sum_of_two_abundants))
sum_of_two_abundants.sort()

sum_of_positives = 0
index = 0
for positive in range(0, 28123):
    if positive == sum_of_two_abundants[index]:
        index += 1
    else:
        sum_of_positives += positive
print(sum_of_positives)
