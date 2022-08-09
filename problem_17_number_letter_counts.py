

numbers_dict = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
    100: ["one", "hundred"], 1000: "onethousand"
}


def get_all_digits(number):
    digit_list = []
    while number != 0:
        digit = number % 10
        digit_list.append(digit)
        number = number // 10
    return digit_list


def get_number_letters(number):
    if number % 100 == 0 and number != 1000:
        letters = numbers_dict[100]
        letters[0] = numbers_dict[number / 100]
        return str(letters[0]) + str(letters[1])
    else:
        return numbers_dict[number]


def parse_digits_and_get_number_letters(digits):
    digit_exp = 0
    index = 0
    letters = ""
    if len(digits) > 1:
        if digits[1] == 1:
            letters += get_number_letters((digits[0] * 10**digit_exp) + (digits[1] * 10**(digit_exp + 1)))
            digit_exp = 2
            index = 2
    while index < len(digits):
        if digits[index] != 0:
            letters += get_number_letters(digits[index] * 10 ** digit_exp)
        index += 1
        digit_exp += 1
    return letters


sum_of_number_letters = 0

for number in range(1, 1001):
    sum_of_number_letters += len(parse_digits_and_get_number_letters(get_all_digits(number)))
    if number % 100 != 0 and number >= 100:
        sum_of_number_letters += 3
print(sum_of_number_letters)