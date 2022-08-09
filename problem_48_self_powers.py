
sum_of_series = 0

for number in range(1, 1001):
    sum_of_series += number**number

last_ten_digits = 0
digit = 1
while len(str(last_ten_digits)) < 10:
    last_ten_digits += (sum_of_series % 10) * digit
    sum_of_series //= 10
    digit *= 10

print(last_ten_digits)