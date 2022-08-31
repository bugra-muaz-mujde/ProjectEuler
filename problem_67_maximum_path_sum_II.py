
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
current_total_list = [int(triangle[0][0])]
proxy_total_list = []

while row_index < len(triangle):
    for index, col in enumerate(triangle[row_index]):
        if index == 0:
            proxy_total_list.append(current_total_list[0] + col)
        elif index == len(triangle[row_index]) - 1:
            proxy_total_list.append(current_total_list[len(current_total_list) - 1] + col)
        else:
            if current_total_list[index - 1] + col < current_total_list[index] + col:
                proxy_total_list.append(current_total_list[index] + col)
            else:
                proxy_total_list.append(current_total_list[index - 1] + col)
    current_total_list = proxy_total_list
    proxy_total_list = []
    row_index += 1


max_total = 0
for total in current_total_list:
    if max_total < total:
        max_total = total
print(max_total)










