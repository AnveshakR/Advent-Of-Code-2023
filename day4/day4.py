file = 'day4/day4.txt'

# Part 1
total_score = 0
with open(file, 'r') as f:
    for line in f.readlines():
        line = line.split(":")[1]
        set1 = set([int(x.strip()) for x in line.split("|")[0].split()])
        set2 = set([int(x.strip()) for x in line.split("|")[1].split()])
        intersection = set1.intersection(set2)
        total_score += 2**(len(intersection)-1) if len(intersection) > 0 else 0

print("Part 1:", total_score)

# Part 2
card_counts = {}
for i in range(len(open(file, 'r').readlines())):
    card_counts[i+1] = 1

with open(file, 'r') as f:
    for num, line in enumerate(f.readlines()):
        line = line.split(":")[1]
        set1 = set([int(x.strip()) for x in line.split("|")[0].split()])
        set2 = set([int(x.strip()) for x in line.split("|")[1].split()])
        intersection = set1.intersection(set2)
        if len(intersection) > 0:
            for i in range(len(intersection)):
                card_counts[num+1+i+1] += 1*card_counts[num+1]

print("Part 2:", sum(card_counts.values()))
        