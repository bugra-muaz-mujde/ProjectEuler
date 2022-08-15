

def is_permuted_multiple(number):
    original_number = list(str(number))
    original_number.sort()
    for multiplier in range(2, 7):
        product = list(str(number * multiplier))
        product.sort()
        if not original_number == product:
            return False
    return True


number_counter = 10
while True:
    if is_permuted_multiple(number_counter):
        print(number_counter)
        break
    number_counter += 1

