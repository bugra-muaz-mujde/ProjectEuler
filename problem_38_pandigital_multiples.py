
def is_pandigital(n):
    for digit in str(n):
        if digit == "0":
            return False
        if str(n).count(digit) > 1:
            return False
    return True


largest_product = 0
product = ""
count = 1
for number in range(1, 10**5):
    while len(product) < 9:
        product += str(number * count)
        count += 1
    if len(product) == 9:
        if is_pandigital(int(product)):
            if largest_product < int(product):
                largest_product = int(product)
    product = ""
    count = 1

print(largest_product)