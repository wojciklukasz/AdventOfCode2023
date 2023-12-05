import re


def get_number(value, category):
    for line in category.split('\n')[1:]:
        ranges = [int(n) for n in re.findall(r'\d+', line)]
        if ranges[1] <= value < ranges[1] + ranges[2]:
            return value - ranges[1] + ranges[0]

    return value


with open('day5/input.txt', 'r') as f:
    data = f.read()

categories = data.split('\n\n')

seeds = [int(n) for n in re.findall(r'\d+', categories[0])]

locations = []
for seed in seeds:
    soil = get_number(seed, categories[1])
    fertilizer = get_number(soil, categories[2])
    water = get_number(fertilizer, categories[3])
    light = get_number(water, categories[4])
    temperature = get_number(light, categories[5])
    humidity = get_number(temperature, categories[6])
    location = get_number(humidity, categories[7])
    locations.append(location)

print(f'Lowest location number:\n{min(locations)}')
