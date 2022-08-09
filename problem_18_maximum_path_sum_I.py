
triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 94, 38, 53, 60, 4, 23, 24]
]

row_index = 1
col_index = 0
current_number = triangle[0][0]
path = {}
chosen_list = [current_number]
path_list = []

while row_index < len(triangle):
    path[col_index] = [col_index, col_index + 1]
    path[col_index + 1] = [col_index + 1, col_index + 2]
    for key in path:
        if triangle[row_index + 1][path[key][0]] > triangle[row_index + 1][path[key][1]]:
            path_list.append(key)
            path_list.append(path[key][0])
        else:
            path_list.append(key)
            path_list.append(path[key][1])
    left_sum = triangle[row_index][path_list[0]] + triangle[row_index + 1][path_list[1]]
    right_sum = triangle[row_index][path_list[2]] + triangle[row_index + 1][path_list[3]]
    if left_sum < right_sum:
        del path_list[0]
        del path_list[0]
    else:
        del path_list[2]
        del path_list[2]
    chosen_list.append(triangle[row_index][path_list[0]])
    chosen_list.append(triangle[row_index + 1][path_list[1]])

    col_index = path_list[1]
    row_index += 2
    if row_index == len(triangle) - 1:
        if triangle[row_index][col_index] < triangle[row_index][col_index + 1]:
            chosen_list.append(triangle[row_index][col_index + 1])
        else:
            chosen_list.append(triangle[row_index][col_index])
        break
    path_list = []
    path = {}


print(sum(chosen_list))

