with open("M:\\Advent of code 22\\2.1.txt") as f:
    lines = f.readlines()

total = 0

for line in lines:
    splitLine = [x for x in line.strip("\n").casefold() if x != " "]
    for val in splitLine:
        if val == 'a' or val == 'b' or val == 'c':
            if val == 'a':
                elfChose = 1
            elif val == 'b':
                elfChose = 2
            else:
                elfChose = 3
        else:
            if val == 'x':
                myChose = 1
            elif val == 'y':
                myChose = 2
            else:
                myChose = 3
    if elfChose > myChose:
        total += myChose
    elif elfChose == myChose:
        total += myChose
        total += 3
    else:
        total += myChose
        total += 6

print(total)