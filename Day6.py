with open("M:\\Advent of code 22\\6.1.txt", 'r') as f:
    lines = f.readlines()

buffer = ""
total = 3
start = 0
end = 4


for line in lines:
    buffer = line

for letter in range(len(buffer)):
    check = set(line[start:end])
    start += 1
    end += 1
    total += 1
    if len(check) == 4:
        break
    else:
        check = set()

print(total)