import time


def function_s(s_number):
    digit_list = []
    mod = s_number % 9
    iteration = s_number // 9
    if mod != 0:
        digit_list.append(mod)
    if iteration != 0:
        digit_list.append(iteration)
    return digit_list


def function_S(limit):
    s_lists = []
    for number in range(1, limit + 1):
        s_lists.append(function_s(number))
    return s_lists


def get_fibonacci(iteration):
    tail = 0
    head = 1
    while iteration > 1:
        temp_head = head
        head = tail + head
        tail = temp_head
        iteration -= 1
    return head

10 19
15 69
25 799



100
1000

func_S_lists = []
func_S_lists.append(function_S(get_fibonacci(90)))
print(func_S_lists)
