import numpy as np

map_dict = {}
with open("day5/test.txt") as f:
    lines = f.read()
    for line in lines.split("\n\n"):
        line = line.split(":")
        map_dict[line[0].strip()] = [[int(y.strip()) for y in x.split(" ")] if isinstance(x, str) else x for x in line[1].strip().split("\n")]
map_dict["seeds"] = map_dict["seeds"][0]

# Part 1
lowest_location = float("inf")

for seed in map_dict["seeds"]:
    soil = 0
    for map in map_dict["seed-to-soil map"]:
        if seed >= map[1] and seed < map[1] + map[2]:
            soil = map[0] + (seed - map[1])
    if soil == 0:
        soil = seed

    fertilizer = 0
    for map in map_dict["soil-to-fertilizer map"]:
        if soil >= map[1] and soil < map[1] + map[2]:
            fertilizer = map[0] + (soil - map[1])
    if fertilizer == 0:
        fertilizer = soil

    water = 0
    for map in map_dict["fertilizer-to-water map"]:
        if fertilizer >= map[1] and fertilizer < map[1] + map[2]:
            water = map[0] + (fertilizer - map[1])
    if water == 0:
        water = fertilizer

    light = 0
    for map in map_dict["water-to-light map"]:
        if water >= map[1] and water < map[1] + map[2]:
            light = map[0] + (water - map[1])
    if light == 0:
        light = water

    temperature = 0
    for map in map_dict["light-to-temperature map"]:
        if light >= map[1] and light < map[1] + map[2]:
            temperature = map[0] + (light - map[1])
    if temperature == 0:
        temperature = light

    humidity = 0
    for map in map_dict["temperature-to-humidity map"]:
        if temperature >= map[1] and temperature < map[1] + map[2]:
            humidity = map[0] + (temperature - map[1])
    if humidity == 0:
        humidity = temperature

    location = 0
    for map in map_dict["humidity-to-location map"]:
        if humidity >= map[1] and humidity < map[1] + map[2]:
            location = map[0] + (humidity - map[1])
    if location == 0:
        location = humidity

    if location < lowest_location:
        lowest_location = location

print("Part 1:", lowest_location)

# Part 2
lowest_location = float("inf")

# for num in (range(len(map_dict["seeds"]), step=2)):
#     print(map_dict["seeds"][num], map_dict["seeds"][num + 1])

# for seed_range in [map_dict["seeds"][i:i+2] for i in range(0, len(map_dict["seeds"]), 2)]:
#     seed = seed_range[0]
