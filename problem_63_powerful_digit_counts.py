

def is_powerful_digit(number):
    exponential = len(str(number))
    expo_list = []
    while True:
        powerful_number = number ** exponential
        if len(str(powerful_number)) == exponential:
            expo_list.append(exponential)
        else:
            break
        exponential += 1
    return expo_list


number = 1
how_many_powerful = 0
while number < 10:
    if is_powerful_digit(number):
        how_many_powerful += len(is_powerful_digit(number))
    number += 1
print(how_many_powerful)