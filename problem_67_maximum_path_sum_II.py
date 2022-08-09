
triangle = []
temp_row = []
f = open("p067_triangle.txt", "r")
for line in f:
    for element in line.split(" "):
        if "\n" in element:
            temp_row.append(int(element.split("\n")[0]))
        else:
            temp_row.append(int(element))
    triangle.append(temp_row)
    temp_row = []
f.close()

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

print(triangle[len(triangle) -1][53])

for row in range(1, len(triangle)):
    for p in range(len(triangle[row])):
        if p == 0:
            triangle[row][p] += triangle[row - 1][0]
        elif p == len(triangle[row]) - 1:
            triangle[row][p] += triangle[row - 1][p - 1]
        else:
            if triangle[row - 1][p - 1] > triangle[row - 1][p]:
                triangle[row][p] += triangle[row - 1][p - 1]
            else:
                triangle[row][p] += triangle[row - 1][p]

print(max(triangle[len(triangle) - 1]))

for i in triangle:
    print(i)