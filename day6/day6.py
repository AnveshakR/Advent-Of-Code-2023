import math

file = 'day6/day6.txt'

with open(file, 'r') as f:
    file = f.readlines()
    race_times = file[0].split(':')[1].strip()
    record_dists = file[1].split(':')[1].strip()

# Part 1
race_times_list = [int(time.strip()) for time in race_times.split()]
record_dists_list = [int(dist.strip()) for dist in record_dists.split()]

number_of_ways = [0]*len(race_times_list)
for race in range(len(race_times_list)):
    press = 0
    while press <= race_times_list[race]:
        dist = press*(race_times_list[race] - press)
        if dist > record_dists_list[race]:
            number_of_ways[race] += 1
        press += 1

print("Part 1: ", math.prod(number_of_ways))


# Part 2
race_time = int(race_times.replace(' ', ''))
record_dist = int(record_dists.replace(' ', ''))

# ax^2 + bx + c = 0
# press(race_time - press) - record_dist = 0
# a = -1
# b = race_time
# c = -record_dist

determinant = race_time**2 - 4*(record_dist)

root1 = (-race_time + math.sqrt(determinant))/(-2)
root2 = (-race_time - math.sqrt(determinant))/(-2)

print("Part 2: ", math.floor(max(root1, root2) - min(root1, root2)))