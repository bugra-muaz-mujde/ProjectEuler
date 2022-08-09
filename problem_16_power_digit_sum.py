
number = 2**1000
sum_of_digits = 0
digit = 0

while number != 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10
print(sum_of_digits)