
def get_divisor_count(number):
    divisor_count = 0
    divisor_array = [1]
    divisor_number = 2
    while number != 1:
        if number % divisor_number == 0:
            divisor_array.append(divisor_number)
            number /= divisor_number
        else:
            divisor_number += 1

    divisor_count_array = []
    setted_divisor_array = [*set(divisor_array)]
    for set_divisor in setted_divisor_array:
        if set_divisor != 1:
            divisor_count_array.append(divisor_array.count(set_divisor))

    print(divisor_count_array)
    print(len(divisor_array))

    index = 0

    while True:
        num = divisor_count_array[index]


    return divisor_count


get_divisor_count(784)




"""
number = 0
count = 1
while True:
    number += count
    count += 1
    if get_divisor_count(number) >= 500:
        print(number)
        break

"""