
def get_permutation(number):
    permutation = 1
    while number > 1:
        permutation *= number
        number -= 1
    return permutation


def get_pandigital(rank):
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pandigital = ""
    for counter in range(9, 0, -1):
        pandigital += str(number_list[int(rank // (get_permutation(counter) / counter))])
        del number_list[int(rank // (get_permutation(counter) / counter))]
        rank = rank % (get_permutation(counter) / counter)
    return int(pandigital)


def get_multipliers(product, overlaps):
    if int(str(product)[:2]) * int(str(product)[2:5]) == int(str(product)[5:]):
        if int(str(product)[5:]) not in overlaps:
            overlaps.append(int(str(product)[5:]))
    elif int(str(product)[:3]) * int(str(product)[3:5]) == int(str(product)[5:]):
        if int(str(product)[5:]) not in overlaps:
            overlaps.append(int(str(product)[5:]))
    elif int(str(product)[:1]) * int(str(product)[1:5]) == int(str(product)[5:]):
        if int(str(product)[5:]) not in overlaps:
            overlaps.append(int(str(product)[5:]))
    elif int(str(product)[:4]) * int(str(product)[4:5]) == int(str(product)[5:]):
        if int(str(product)[5:]) not in overlaps:
            overlaps.append(int(str(product)[5:]))
    return overlaps


pandigitals = []
overlaps_list = []
sum_of_all_divisible_properties = 0
for count in range(get_permutation(9)):
    pandigitals.append(get_pandigital(count))

for pandigital_number in pandigitals:
    overlaps_list = get_multipliers(str(pandigital_number), overlaps_list)
print(sum(overlaps_list))



