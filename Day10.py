with open("M:\\Advent of code 22\\10.1.txt", 'r') as f:
    lines = f.readlines()

x = 1
cycle_count = 0
total = 0
val_list = []
sprite_position = 1

for line in lines:
    line = line.strip("\n").split(" ")
    for row in range(0, 241, 40):
        for val in range(40):
            print()
#     if line[0] == "addx":
#         for i in range(2):
#             cycle_count += 1
#             if cycle_count in range(20, 221, 40):
#                 val_list.append(x * cycle_count)
#         x += int(line[1])
#     else:
#         cycle_count += 1
#         if cycle_count in range(20, 221, 40):
#             val_list.append(x * cycle_count)

# for i in val_list:
#     total += i
# print(total)