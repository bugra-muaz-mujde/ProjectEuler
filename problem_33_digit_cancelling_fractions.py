
two_digit_numbers = []

for number in range(10, 100):
    if number % 10 != 0:
        two_digit_numbers.append(number)

two_digit_numbers.reverse()
numerators = []
denominators = {}
num = 0
for denominator in two_digit_numbers:
    temp_denominator = denominator
    for i in range(2):
        num += (temp_denominator % 10) * 10**(1-i)
        temp_denominator //= 10
    while num > 10:
        if num != denominator and num < denominator:
            numerators.append(num)
        num -= 10
    denominators[denominator] = numerators
    numerators = []
    num = 0


def cancel_number(numerator, key):
    return (numerator // 10) / (key % 10)


terms = []

for key in denominators:
    for numerator in denominators[key]:
        if numerator / key == cancel_number(numerator, key):
            terms.append([numerator, key])

numerator_res = 1
denominator_res = 1
for fraction in terms:
    numerator_res *= fraction[0]
    denominator_res *= fraction[1]

result = numerator_res / denominator_res
result_denominator = 1
while result // 10 == 0:
    result = result * 10
    if result // 10 == 0:
        result_denominator *= 10
print(result_denominator)
