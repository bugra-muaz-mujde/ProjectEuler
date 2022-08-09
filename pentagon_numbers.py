import math


def get_pentagonal_number(n):
    return int((n * (3 * n - 1)) * 0.5)


def find_perfect_pentagonal(pentagonal_number, pentagonal_list):
    number_index = 0
    index = 0
    term_list = []
    while True:
        term = pentagonal_list[number_index]
        while True:
            if pentagonal_number - term == pentagonal_list[index] and term != pentagonal_list[index]:
                term_list.append(term)
            elif pentagonal_number == pentagonal_list[index]:
                break
            index += 1
        index = 0
        number_index += 1
        if term == pentagonal_number:
            return term_list


def is_pentagonal(pentagonal):
    start_term = int(math.sqrt(pentagonal * 2) / 2)
    while True:
        if get_pentagonal_number(start_term) == pentagonal:
            return True
        elif get_pentagonal_number(start_term) > pentagonal:
            return False
        start_term += 1


pentagonals = [get_pentagonal_number(1), get_pentagonal_number(2)]
current_number = 3
index_counter = 0
while True:
    print(current_number)
    pentagonals.append(get_pentagonal_number(current_number))
    terms = find_perfect_pentagonal(pentagonals[len(pentagonals) - 1], pentagonals)
    if terms:
        for term in terms:
            if is_pentagonal(pentagonals[len(pentagonals) - 1] - term):
                if is_pentagonal(pentagonals[len(pentagonals) - 1] + term):
                    print(pentagonals[len(pentagonals) - 1])
                    break
    current_number += 1
