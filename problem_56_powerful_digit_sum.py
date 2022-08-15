

def get_exponential(a, b):
    return a**b


def get_sum_of_digits(number):
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)
    return sum_of_digits


maximum_digital_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        current_digital_sum = get_sum_of_digits(get_exponential(a, b))
        if maximum_digital_sum < current_digital_sum:
            maximum_digital_sum = current_digital_sum

print(maximum_digital_sum)

