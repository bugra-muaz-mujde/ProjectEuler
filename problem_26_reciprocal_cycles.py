
def is_cycle(string, letter):
    for char in string:
        if char == letter:
            return False
    return True


decimals = {}

for decimal in range(2, 1000):
    if len(str(1/decimal).split(".")[1]) > 4:
        decimals[decimal] = str(1/decimal).split(".")[1]

print(len(decimals[1000]))
decimal_string = ""

cycle_digit = 0
longest_cycle = 0
longest_decimal = ""
for decimal in decimals:
    for index, digit in enumerate(decimals[decimal]):
        if is_cycle(decimal_string, digit):
            decimal_string += digit
        else:
            if decimal_string == decimals[decimal][index: index + len(decimal_string)]:
                cycle_digit = len(decimal_string)
                if cycle_digit > 7:
                    print(cycle_digit)
                    print(decimal)
            else:
                decimal_string = digit
    if longest_cycle < cycle_digit:
        longest_cycle = cycle_digit
        longest_decimal = decimal
    decimal_string = ""


print(longest_cycle)
print(longest_decimal)








