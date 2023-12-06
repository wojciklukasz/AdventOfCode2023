import re


def calculate_distance(time_limit, hold_time):
    return (time_limit - hold_time) * hold_time


with open('day6/input.txt', 'r') as f:
    lines = f.readlines()

times = [int(x) for x in re.findall(r'\d+', lines[0])]
records = [int(x) for x in re.findall(r'\d+', lines[1])]

ways_mult = 1
for time, record in zip(times, records):
    middle_dist = calculate_distance(time, time // 2)
    count = 0
    while middle_dist > record:
        count += 1
        middle_dist = calculate_distance(time, time // 2 - count)
    
    if time % 2 == 0:
        ways_mult *= count * 2 - 1
    else:
        ways_mult *= count * 2

print(f'Result:\n{ways_mult}')