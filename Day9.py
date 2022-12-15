with open("M:\\Advent of code 22\\9.1.txt", 'r') as f:
    lines = f.readlines()

h_x = 0
h_y = 0
t_x = 0
t_y = 0
co_ords_list = []

for line in lines:
    line = line.strip()
    splitLine = line.split(" ")
    if splitLine[0] == "L":
        for move in range(int(splitLine[1])):
            h_x -= 1
            if h_x - 1 <= t_x <= h_x + 1:
                if [t_x, t_y] not in co_ords_list:
                    co_ords_list.append([t_x, t_y])
            else:
                t_x -= 1
                if t_y == h_y:
                    if [t_x, t_y] not in co_ords_list:
                        co_ords_list.append([t_x, t_y])
                else:
                    t_y = h_y
                    if [t_x, t_y] not in co_ords_list:
                        co_ords_list.append([t_x, t_y])
    elif splitLine[0] == "U":
        for move in range(int(splitLine[1])):
            h_y += 1
            if h_y - 1 <= t_y <= h_y + 1:
                if [t_x, t_y] not in co_ords_list:
                    co_ords_list.append([t_x, t_y])
            else:
                t_y += 1
                if t_x == h_x:
                    if [t_x, t_y] not in co_ords_list:
                        co_ords_list.append([t_x, t_y])
                else:
                    t_x = h_x
                    if [t_x, t_y] not in co_ords_list:
                        co_ords_list.append([t_x, t_y])
    elif splitLine[0] == "D":
        for move in range(int(splitLine[1])):
            h_y -= 1
            if h_y - 1 <= t_y <= h_y + 1:
                if [t_x, t_y] not in co_ords_list:
                    co_ords_list.append([t_x, t_y])
            else:
                t_y -= 1
                if t_x == h_x:
                    if [t_x, t_y] not in co_ords_list:
                        co_ords_list.append([t_x, t_y])
                else:
                    t_x = h_x
                    if [t_x, t_y] not in co_ords_list:
                        co_ords_list.append([t_x, t_y])
    else:
        for move in range(int(splitLine[1])):
            h_x += 1
            if h_x - 1 <= t_x <= h_x + 1:
                if [t_x, t_y] not in co_ords_list:
                    co_ords_list.append([t_x, t_y])
            else:
                t_x += 1
                if t_y == h_y:
                    if [t_x, t_y] not in co_ords_list:
                        co_ords_list.append([t_x, t_y])
                else:
                    t_y = h_y
                    if [t_x, t_y] not in co_ords_list:
                        co_ords_list.append([t_x, t_y])


print(len(co_ords_list))