with open("M:\\Advent of code 22\\4.1.txt", "r") as f:
    lines = f.readlines()

total = 0

for line in lines:
    splitLine = line.strip("\n").split(",")
    first_set = splitLine[0].split("-")
    second_set = splitLine[1].split("-")
    print(first_set, second_set)
    if int(first_set[0]) <= int(second_set[0]) and int(first_set[1]) >= int(second_set[1]):
        total += 1
    elif int(second_set[0]) <= int(first_set[0]) and int(second_set[1]) >= int(first_set[1]):
        total += 1

print(total)