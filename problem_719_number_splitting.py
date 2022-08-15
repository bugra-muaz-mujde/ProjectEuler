import math


def get_products(product):
    products = []
    for digit_count in range(1, len(product)):
        for cursor in range(len(product) - digit_count + 1):
            products.append(product[cursor: cursor + digit_count])
    return products


def reduce_product(product_digit_list, number):
    for digit in number:
        product_digit_list.remove(digit)
    for i in range(len(product_digit_list)):
        product_digit_list[i] = int(product_digit_list[i])
    return product_digit_list


def is_splitting(product_string, products):
    for product in products:
        s_number_digits = reduce_product(list(product_string), product)
        if int(product_string) == (sum(s_number_digits) + int(product))**2:
            return True
    return False


total = 0
for number in range(10, 10**4 + 1):
    if is_splitting(str(number), get_products(str(number))):
        total += number
        print(number)

print(total)
