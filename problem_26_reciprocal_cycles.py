
def reduce_zeros(number):
    while True:
        if number % 10 == 0:
            number //= 10
        else:
            return number


def division(dividend, divisor, iterate=2000):
    divisor = reduce_zeros(divisor)
    number_string = ""
    while dividend != 0 and iterate > 0:
        while dividend < divisor:
            dividend *= 10
            if dividend < divisor:
                number_string += "0"
                iterate -= 1
        number_string += str(dividend // divisor)
        dividend = dividend % divisor
        iterate -= 1
    return number_string


def recurring_cycle(number):
    index = 0
    cycle = ""
    max_cycle = 0
    while index < len(number):
        cycle += number[index]
        if cycle == number[index + 1: index + 1 + len(cycle)]:
            max_cycle = len(cycle)
            cycle = ""
        index += 1
    return max_cycle


longest_cycle = 0
number_contains_longest_cycle = 0
for i in range(2, 1000):
    cycle = recurring_cycle(division(1, i))
    if longest_cycle < cycle:
        longest_cycle = cycle
        number_contains_longest_cycle = i
print(number_contains_longest_cycle)


