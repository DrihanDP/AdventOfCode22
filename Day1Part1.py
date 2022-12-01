with open("M:\\Advent of code 22\\1.1.txt", 'r') as f:
    lines = f.readlines()

total = 0
cal_list = []

for line in lines:
    if line != "\n":
        total += int(line.strip("\n"))
    else:
        cal_list.append(total)
        total = 0

print(max(cal_list))

cal_list.sort(reverse=True)

top3 = cal_list[0] + cal_list[1] + cal_list[2]
print(top3)