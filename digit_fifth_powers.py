
def is_digit_fifth_powers(digits):
    sum_of_digits_fifth_powers = 0
    for digit in digits:
        sum_of_digits_fifth_powers += int(digit)**5
    if sum_of_digits_fifth_powers == int(digits):
        return True
    return False


sum_of_numbers = 0
limit = 0
for power in range(10):
    limit += power**5


for number in range(2, limit * 2):
    if is_digit_fifth_powers(str(number)):
        sum_of_numbers += number

print(sum_of_numbers)