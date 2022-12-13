with open("M:\\Advent of code 22\\7.1.txt", 'r') as f:
    lines = f.readlines()

# for line in lines:
#     print(line.strip())

cwd = root = {} 
stack = []

for line in lines:
    line = line.strip()
    if line[0] == "$":
        if line[2] == "c":
            dir = line[5:]
            if dir == "/":
                cwd = root
                stack = []
            elif dir == "..":
                cwd = stack.pop()
            else:
                if dir not in cwd: # if dir is not a key in cwd set as new directory
                    cwd[dir] = {}
                stack.append(cwd)
                cwd = cwd[dir]
    else:
        x, y = line.split()
        if x == "dir":
            if y not in cwd:
                cwd[y] = {}
        else:
            cwd[y] = int(x)


def size(dir = root):
    if type(dir) == int:
        return(dir)
    return sum(map(size, dir.values()))


threshold = size() - 40000000

def solve(dir = root):
    ans = float("inf")
    if size(dir) >= threshold:
        ans = size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        smallest_val = solve(child)
        ans = min(ans, smallest_val)
    return ans

print(solve())