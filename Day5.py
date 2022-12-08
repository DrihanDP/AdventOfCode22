with open("M:\\Advent of code 22\\5.1.txt", 'r') as f:
    lines = f.readlines()

space_count = 0
n = 4
pop_list = []
answer_list = []

crate_dict = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": []
}

for line in lines:
    stripLine = line.strip("\n")
    splitLine = [stripLine[i:i+n] for i in range(0, len(stripLine), n)]
    if "move" not in splitLine:
        if len(splitLine) != 0:
            if " 1  " not in splitLine:
                if splitLine[0] != "    ":
                    crate_dict["1"].append(splitLine[0])
                if splitLine[1] != "    ":
                    crate_dict["2"].append(splitLine[1])
                if splitLine[2] != "    ":
                    crate_dict["3"].append(splitLine[2])
                if splitLine[3] != "    ":
                    crate_dict["4"].append(splitLine[3])
                if splitLine[4] != "    ":
                    crate_dict["5"].append(splitLine[4])
                if splitLine[5] != "    ":
                    crate_dict["6"].append(splitLine[5])
                if splitLine[6] != "    ":
                    crate_dict["7"].append(splitLine[6])
                if splitLine[7] != "    ":
                    crate_dict["8"].append(splitLine[7])
                if splitLine[8] != "   ":
                    crate_dict["9"].append(splitLine[8] + " ")
            else:
                break

crate_dict["1"].reverse()
crate_dict["2"].reverse()
crate_dict["3"].reverse()
crate_dict["4"].reverse()
crate_dict["5"].reverse()
crate_dict["6"].reverse()
crate_dict["7"].reverse()
crate_dict["8"].reverse()
crate_dict["9"].reverse()


for line in lines:
    if "move" in line:
        splitLine = [x for x in line.strip("\n").split(" ")]
        for num in range(int(splitLine[1])):
            pop_list.append(crate_dict[splitLine[3]].pop(-1))
        pop_list.reverse()
        for val in range(len(pop_list)):
            crate_dict[splitLine[5]].append(pop_list[val])
        pop_list = []

for key in crate_dict:
    dict_list = crate_dict.get(key)
    answer_list.append(dict_list[len(dict_list) - 1][1])
print("".join(answer_list))