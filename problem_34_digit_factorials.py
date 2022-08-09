
def get_factorial(num):
    factorial = 1
    for count in range(1, num + 1):
        factorial *= count
    return factorial


curious_numbers = []
total = 0
for number in range(3, 100000):
    for digit in str(number):
        total += get_factorial(int(digit))
    if number == total:
        curious_numbers.append(number)
    total = 0

print(sum(curious_numbers))