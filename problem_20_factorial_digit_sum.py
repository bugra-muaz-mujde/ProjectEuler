

def get_sum_of_digits(num):
    sum_of_digits = 0
    while num != 0:
        sum_of_digits += num % 10
        num //= 10
    return sum_of_digits


factorial_of_100 = 1

for number in range(1, 101):
    factorial_of_100 *= number

print(get_sum_of_digits(factorial_of_100))