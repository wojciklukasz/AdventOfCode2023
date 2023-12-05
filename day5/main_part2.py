import re
from multiprocessing import Pool

"""
    Unoptimized, should give the correct result after it finishes though.
"""


locations = []

def worker(pair, locations):
    print(f'Working on {pair[0]} {pair[1]}')
    locations.append(get_lowest_location(pair))


def get_number(value, category):
    for line in category.split('\n')[1:]:
        ranges = [int(n) for n in re.findall(r'\d+', line)]
        if ranges[1] <= value < ranges[1] + ranges[2]:
            return value - ranges[1] + ranges[0]

    return value


def get_lowest_location(pair):
    print(f'Working on {pair[0]} {pair[1]}')
    seed = pair[0]
    min_loc = 999999999999999999
    while seed < pair[0] + pair[1]:
        soil = get_number(seed, categories[1])
        fertilizer = get_number(soil, categories[2])
        water = get_number(fertilizer, categories[3])
        light = get_number(water, categories[4])
        temperature = get_number(light, categories[5])
        humidity = get_number(temperature, categories[6])
        location = get_number(humidity, categories[7])
        if min_loc > location:
            min_loc = location

        seed += 1

    locations.append(min_loc)
    print(locations)


with open('day5/input.txt', 'r') as f:
    data = f.read()

categories = data.split('\n\n')

seeds_raw =[int(n) for n in re.findall(r'\d+', categories[0])]
seeds_pairs = [seeds_raw[i:i+2] for i in range(0, len(seeds_raw), 2)]

with Pool(5) as pool:
    pool.map(get_lowest_location, seeds_pairs)

print(f'Lowest location number:\n{min(locations)}')
