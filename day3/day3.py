import numpy as np
import re
import math

arr_2d = np.array([list(line.strip()) for line in open("day3/day3.txt", "r")])

def symbol_in_neighborhood(array, row, col, symbol=None):
    num_rows, num_cols = array.shape
    # multiple *s?
    for i in range(max(0, row - 1), min(num_rows, row + 2)):
        for j in range(max(0, col - 1), min(num_cols, col + 2)):
            if i != row or j != col:
                if symbol is not None:
                    if array[i, j] == symbol:
                        return True, (i, j)
                else:
                    if array[i, j] != "." and not (array[i, j]).isdigit():
                        return True, (i, j)
    return False, (None, None)

# Part 1

# find all numbers in a row
# check if any of the numbers have any symbol in their neighborhood by checking the neighborhood of each number
# if any has a symbol, add the number to the total sum
total_sum = 0
for row in range(arr_2d.shape[0]):
    number_matches = re.finditer(r"\d+", "".join(arr_2d[row]))
    for match in number_matches:
        number = match.group()
        if any([symbol_in_neighborhood(arr_2d, row, index)[0] for index in range(match.start(), match.end())]):
            total_sum += int(number)

print("Part 1: ", total_sum)

# Part 2

# find all numbers in a row
# check if any of the numbers have a * in their neighborhood by checking the neighborhood of each number
# if yes then add the number to a dictionary with the index of the * as the key
# each value in the dictionary is a set of numbers that have a * in their neighborhood
# if the length of the set is 2 then multiply the two numbers and add to the total sum
total_sum = 0
star_dict = {}
for row in range(arr_2d.shape[0]):
    number_matches = re.finditer(r"\d+", "".join(arr_2d[row]))
    for match in number_matches:
        number = match.group()
        for index in range(match.start(), match.end()):
            has_symbol, index = symbol_in_neighborhood(arr_2d, row, index, symbol="*")
            if has_symbol:
                if index not in star_dict:
                    star_dict[index] = set()
                star_dict[index].add(int(number))

for key in star_dict:
    if len(star_dict[key]) == 2:
        total_sum += math.prod(star_dict[key])

print("Part 2: ", total_sum)