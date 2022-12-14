with open("M:\\Advent of code 22\\8.1.txt", 'r') as f:
    lines = f.readlines()

grid = [list(map(int, line)) for line in open("M:\\Advent of code 22\\8.1.txt").read().splitlines()]

list1 = []
total = 1

for row in range(len(grid)):
    for column in range(len(grid[row])):
        cur_tree = grid[row][column]
        left = right = up = down = 0
        for val in range(column - 1, -1, -1):
            left += 1
            if grid[row][val] >= cur_tree:
                break
        for val in range(column + 1, len(grid[row])):
            right += 1
            if grid[row][val] >= cur_tree:
                break
        for val in range(row - 1, -1, -1):
            up += 1
            if grid[val][column] >= cur_tree:
                break
        for val in range(row + 1, len(grid)):
            down += 1
            if grid[val][column] >= cur_tree:
                break
        total = max(cur_tree, left * right * up * down)
        list1.append(total)
                    # if all(grid[row][val] < cur_tree for val in range(column)) or all(grid[row][val] < cur_tree for val in range(column + 1, len(grid[row]))) or all(grid[val][column] < cur_tree for val in range(row)) or all(grid[val][column] < cur_tree for val in range(row + 1, len(grid))):
        #     total += 1
# total_max = max(list1)
# print(total_max)

# for val in total_max:
#     total = val * total
    # total = total * int(val)
scenic = max(list1)
print(scenic)
# print(total)

