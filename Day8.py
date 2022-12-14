with open("M:\\Advent of code 22\\8.1.txt", 'r') as f:
    lines = f.readlines()

grid = [list(map(int, line)) for line in open("M:\\Advent of code 22\\8.1.txt").read().splitlines()]
print(grid)

total = 0

for row in range(len(grid)):
    for column in range(len(grid[row])):
        cur_tree = grid[row][column]
        if all(grid[row][val] < cur_tree for val in range(column)) or all(grid[row][val] < cur_tree for val in range(column + 1, len(grid[row]))) or all(grid[val][column] < cur_tree for val in range(row)) or all(grid[val][column] < cur_tree for val in range(row + 1, len(grid))):
            total += 1

print(total)

# tree_list = []
# total = 0
# cur_pos_row = 0
# cur_pos_column = 0

# for line in lines:
#     line = line.strip()
#     row_split = [x for x in line]
#     tree_list.append(row_split)

# for row in tree_list:
#     biggest_left = 0
#     biggest_right = 0
#     biggest_up = 0
#     biggest_down = 0
#     cur_pos_column = 0
#     if cur_pos_row == 0 or cur_pos_row == len(tree_list):
#         total += len(row)
#         cur_pos_row += 1
#     else:
#         for val in row:
#             if cur_pos_column == 0:
#                 total += 1
#                 cur_pos_column += 1
#                 cur_val = val
#             else:
#                 for row in tree_list:
#                     if row[cur_pos_column] > biggest_down:
#                         biggest_down = row[cur_pos_column]

# print(total)