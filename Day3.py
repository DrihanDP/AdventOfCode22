with open("M:\\Advent of code 22\\3.1.txt", "r") as f:
    lines = f.readlines()

letter_values = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

total = 0

# for line in lines:
#     middle_index = len(line) // 2
#     first_half = line.strip("\n")[:middle_index]
#     second_half = line.strip("\n")[middle_index:]
#     common_list = set(first_half).intersection(second_half)
#     for val in common_list:
#         total += letter_values.get(val)

first_line = []
second_line = []
third_line = []

for line in lines:
    if first_line == []:
        first_line = line.strip("\n")
    elif second_line == []:
        second_line = line.strip("\n")
    else:
        third_line = line.strip("\n")
        first_and_second = set(first_line).intersection(second_line)
        common_list = set(first_and_second).intersection(third_line)
        print(common_list)
        first_line = []
        second_line = []
        third_line = []
        for val in common_list:
            total += letter_values.get(val)
            
print(total)