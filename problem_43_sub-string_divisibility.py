
def is_pandigital(number):
    for digit_index, digit in enumerate(str(number)):
        for others_index, others in enumerate(str(number)):
            if digit == others and digit_index != others_index:
                return False
    return True


only_pandigital_numbers = []

for ten_digit_number in range(10**9, 10**10):
    if is_pandigital(ten_digit_number):
        only_pandigital_numbers.append(ten_digit_number)

print(only_pandigital_numbers)