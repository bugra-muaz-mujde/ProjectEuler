import random
import numpy as np

def move_right(current_col):
    return current_col + 1


def move_down(current_row):
    return current_row + 1


def get_grid(grid_length):
    grid_list = []
    grid_row_list = []
    for grid_row in range(grid_length):
        for grid_col in range(grid_length):
            grid_row_list.append(0)
        grid_list.append(grid_row_list)
        grid_row_list = []
    return grid_list


grid = get_grid(21)
grid[0][0] = 1
move_list = []
row = 0
col = 0

counter = 0
while counter < 160000:
    move = random.randint(0, 1)
    if move % 2 == 0 and row < len(grid) - 1:
        row = move_down(row)
    elif move % 2 == 1 and col < len(grid[0]) - 1:
        col = move_right(col)
    grid[row][col] = 1
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        if grid not in move_list:
            move_list.append(grid)
        row = 0
        col = 0
        grid = get_grid(21)
        grid[0][0] = 1
        counter += 1
        print(counter)


print(len(move_list))


"""

1 1 1   00 01 02
0 0 1   10    12
0 0 1   20 21 22

1 1 0   00 01      00
0 1 1      11 12   10 11 
0 0 1         22      21 22

0 0 0
0 0 0
0 0 0

"""