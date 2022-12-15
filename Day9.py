with open("M:\\Advent of code 22\\9.1.txt", 'r') as f:
    lines = f.read().strip().split("\n")

# researched

knots = [[0, 0] for i in range(10)]

# hx, hy = 0, 0
# tx, ty = 0, 0

def touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def move(dx, dy):
    global knots
    knots[0][0] += dx
    knots[0][1] += dy

    for i in range(1, 10):
        hx, hy = knots[i - 1]
        tx, ty = knots[i]

        if not touching(hx, hy, tx, ty):
            sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tx += sign_x
            ty += sign_y
        
        knots[i] = [tx, ty]

direction = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1],
}

tail_visited = set()
tail_visited.add(tuple(knots[-1]))

for line in lines:
    op, amount = line.split(" ")
    amount = int(amount)
    dx, dy = direction[op]

    for i in range(amount):
        move(dx, dy)
        tail_visited.add(tuple(knots[-1]))

print(len(tail_visited))

# h_x = 0
# h_y = 0
# t_x = 0
# t_y = 0
# co_ords_list = []

# for line in lines:
#     line = line.strip()
#     direction, val = line.split(" ")
#     for i in range(int(val)):
#         if direction == "L":
#             for move in range(int(val)):
#                 h_x -= 1
#                 if h_x - 1 <= t_x <= h_x + 1:
#                     if [t_x, t_y] not in co_ords_list:
#                         co_ords_list.append([t_x, t_y])
#                 else:
#                     t_x -= 1
#                     if t_y == h_y:
#                         if [t_x, t_y] not in co_ords_list:
#                             co_ords_list.append([t_x, t_y])
#                     else:
#                         t_y = h_y
#                         if [t_x, t_y] not in co_ords_list:
#                             co_ords_list.append([t_x, t_y])
#         elif direction == "U":
#             for move in range(int(val)):
#                 h_y += 1
#                 if h_y - 1 <= t_y <= h_y + 1:
#                     if [t_x, t_y] not in co_ords_list:
#                         co_ords_list.append([t_x, t_y])
#                 else:
#                     t_y += 1
#                     if t_x == h_x:
#                         if [t_x, t_y] not in co_ords_list:
#                             co_ords_list.append([t_x, t_y])
#                     else:
#                         t_x = h_x
#                         if [t_x, t_y] not in co_ords_list:
#                             co_ords_list.append([t_x, t_y])
#         elif direction == "D":
#             for move in range(int(val)):
#                 h_y -= 1
#                 if h_y - 1 <= t_y <= h_y + 1:
#                     if [t_x, t_y] not in co_ords_list:
#                         co_ords_list.append([t_x, t_y])
#                 else:
#                     t_y -= 1
#                     if t_x == h_x:
#                         if [t_x, t_y] not in co_ords_list:
#                             co_ords_list.append([t_x, t_y])
#                     else:
#                         t_x = h_x
#                         if [t_x, t_y] not in co_ords_list:
#                             co_ords_list.append([t_x, t_y])
#         else:
#             for move in range(int(val)):
#                 h_x += 1
#                 if h_x - 1 <= t_x <= h_x + 1:
#                     if [t_x, t_y] not in co_ords_list:
#                         co_ords_list.append([t_x, t_y])
#                 else:
#                     t_x += 1
#                     if t_y == h_y:
#                         if [t_x, t_y] not in co_ords_list:
#                             co_ords_list.append([t_x, t_y])
#                     else:
#                         t_y = h_y
#                         if [t_x, t_y] not in co_ords_list:
#                             co_ords_list.append([t_x, t_y])


# print(len(co_ords_list))