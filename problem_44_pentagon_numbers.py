import time
import math
start = time.time()


def get_pentagonal_number(n):
    return int((n * (3 * n - 1)) * 0.5)


def check_difference(pentagon_list, cursor, start_index):
    if cursor > (pentagon_list[len(pentagon_list) - 1] / 2):
        for index in range(len(pentagon_list) - 2, 0, -1):
            if cursor > pentagon_list[index]:
                return False
            elif cursor == pentagon_list[index]:
                return True
    else:
        for index in range(start_index, len(pentagon_list)):
            if cursor < pentagon_list[index]:
                return False
            elif cursor == pentagon_list[index]:
                return True


def check_sum(pentagon_list, cursor):
    current_index = len(pentagon_list) + 1
    while True:
        pentagon = get_pentagonal_number(current_index)
        if pentagon > cursor:
            return False
        elif pentagon == cursor:
            return True
        current_index += 1

d_number = 0
pentagonals = [get_pentagonal_number(1), get_pentagonal_number(2)]
j_cursor = 0
k_cursor = 2
while d_number == 0:
    pentagonals.append(get_pentagonal_number(k_cursor + 1))
    while j_cursor < k_cursor:
        if check_difference(pentagonals, pentagonals[k_cursor] - pentagonals[j_cursor], int(math.sqrt(k_cursor + j_cursor))):
            if check_sum(pentagonals, pentagonals[k_cursor] + pentagonals[j_cursor]):
                d_number = get_pentagonal_number(k_cursor + 1) - get_pentagonal_number(j_cursor + 1)
        j_cursor += 1
    j_cursor = 0
    k_cursor += 1

print(d_number)
end = time.time()

total_time = end - start
print("\n"+ str(total_time))

#  start cursor might be root sum of k_cursor and j_cursor lkjasglkjaskgljaskjgaksljgkajlsk -1 second*
