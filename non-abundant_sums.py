import math


def is_abundant(n):
    # Check if the number n is divisible by numbers from 2 to half of n
    sumOfDivisors = 1 # 1 is always a proper divisor
    for x in range(2, (n//2 + 1)):
        if n % x == 0:
            sumOfDivisors += x
    return sumOfDivisors > n


positives = [0] * 28124
abundants = []
for number in range(1, 28124):
    positives[number - 1] = number
    if is_abundant(number):
        abundants.append(number)
count = 0
for abundant_number in abundants:
    positives[abundant_number - 1] = 0
    count += 1
    for sub_abundant_number in abundants:
        sum_of_two_abundants = abundant_number + sub_abundant_number
        if sum_of_two_abundants < len(positives):
            positives[sum_of_two_abundants - 1] = 0
            count += 1

abundantSums = set([])
for numOne in abundants:
    for numTwo in abundants:
        abSum = numOne + numTwo
        if abSum > 28123:
            break
        else:
            abundantSums.add(abSum)

print(len(abundantSums))
print(count)

print(sum(positives))
