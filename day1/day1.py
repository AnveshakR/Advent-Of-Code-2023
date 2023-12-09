import re

number_dict = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four" : '4',
    "five" : '5',
    "six" : '6',
    "seven" : '7',
    "eight" : '8',
    "nine" : '9'
}

sum = 0
with open("day1/day1.txt") as f:
    for line in f.readlines():
        line = line.strip()
        line = " " + line + " "
        match_index = []
        
        for pattern in list(number_dict.keys()):
            if [m.start() for m in re.finditer(pattern, line) if m.start() != 0] != []:
                match_index.extend([[m.start()-1, number_dict[m.group()]] for m in re.finditer(pattern, line) if m.start() != 0])
        
        match_index.extend([index-1, char] for index, char in enumerate(line) if char.isdigit())
        
        match_index.sort(key=lambda x: x[0])
        
        line = "".join([i[1] for i in match_index])
        line = int(line)

        if line//10 == 0:
            sum += 11*line
        elif line//10 > 9:
            line = str(line)
            sum += int(line[0] + line[-1])
        else:
            sum += line

print(sum)
