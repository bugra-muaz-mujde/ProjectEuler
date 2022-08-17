
def get_square(n):
    return n**2


def is_chain_89(member):
    while True:
        if member == 89:
            return True
        elif member == 1:
            return False
        else:
            member = get_next_chain_number(member)


def get_next_chain_number(number):
    sum_of_squares = 0
    for digit in str(number):
        sum_of_squares += get_square(int(digit))
    return sum_of_squares


count_of_89_loops = 0
for positives in range(1, 10**7):
    if is_chain_89(positives):
        count_of_89_loops += 1
    print(positives)
print(count_of_89_loops)