

def get_sum_of_divisors(amicable):
    sum_of_divisors = 0
    for divisor in range(1, amicable):
        if amicable % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors


amicable_dict = {}
for number in range(1, 10000):
    amicable_dict[number] = get_sum_of_divisors(number)

sum_of_amicables = 0
for key in amicable_dict:
    if amicable_dict[key] in amicable_dict.keys():
        if amicable_dict[amicable_dict[key]] == key and key != amicable_dict[key]:
            sum_of_amicables += amicable_dict[key]
            sum_of_amicables += key

print(int(sum_of_amicables/2))
