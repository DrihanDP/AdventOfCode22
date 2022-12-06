with open("M:\\Advent of code 22\\5.1.txt", 'r') as f:
    lines = f.readlines()

space_count = 0

crate_1 = []
crate_2 = []
crate_3 = []
crate_4 = []
crate_5 = []
crate_6 = []
crate_7 = []
crate_8 = []
crate_9 = []

for line in lines:
    splitLine = line.strip("\n").split(" ")
    # print(splitLine)
    if "move" not in splitLine:
        if splitLine[1] == '1' or len(splitLine) != 1:
            print(splitLine)
            if splitLine[1] == "":
                for i in range(3):
                    splitLine.remove(splitLine[1])
            if splitLine[2] == "":
                for i in range(3):
                    splitLine.remove(splitLine[2])
            if splitLine[3] == "":
                for i in range(3):
                    splitLine.remove(splitLine[3])
            if splitLine[4] == "":
                for i in range(3):
                    splitLine.remove(splitLine[4])
            if splitLine[5] == "":
                for i in range(3):
                    splitLine.remove(splitLine[5])
            if splitLine[6] == "":
                for i in range(3):
                    splitLine.remove(splitLine[6])
            if splitLine[7] == "":
                for i in range(3):
                    splitLine.remove(splitLine[7])
            if splitLine[8] == "":
                for i in range(3):
                    splitLine.remove(splitLine[8])
            print(splitLine)
            if splitLine[0] != "":
                crate_1.append(splitLine[0])
            if splitLine[1] != "":
                crate_2.append(splitLine[1])
            if splitLine[2] != "":
                crate_3.append(splitLine[2])
            if splitLine[3] != "":
                crate_4.append(splitLine[3])
            if splitLine[4] != "":
                crate_5.append(splitLine[4])
            if splitLine[5] != "":
                crate_6.append(splitLine[5])
            if splitLine[6] != "":
                crate_7.append(splitLine[6])
            if splitLine[7] != "":
                crate_8.append(splitLine[7])
            if splitLine[8] != "":
                crate_9.append(splitLine[8])
            else:
                if splitLine == " ":
                    space_count += 1

crate_1.reverse()
crate_2.reverse()
crate_3.reverse()
crate_4.reverse()
crate_5.reverse()
crate_6.reverse()
crate_7.reverse()
crate_8.reverse()
crate_9.reverse()
print(crate_1)
print(crate_2)
print(crate_3)
print(crate_4)
print(crate_5)
print(crate_6)
print(crate_7)
print(crate_8)
print(crate_9)