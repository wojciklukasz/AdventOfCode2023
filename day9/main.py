import re


def extrapolate(sequence):
    levels = [sequence]
    while sum(levels[-1]) != 0:

        new_level = []
        for i in range(len(levels[-1]) - 1):
            new_level.append(levels[-1][i + 1] - levels[-1][i])
        levels.append(new_level)

    levels[-1].append(0)
    for i in range(len(levels) - 1, 0, -1):
        levels[i - 1].append(levels[i - 1][-1] + levels[i][-1])

    return levels[0][-1]


with open('day9/input.txt', 'r') as f:
    lines = f.readlines()

sequences = [re.findall(r'-?\d+', line) for line in lines]
sequences = [list(map(int, s)) for s in sequences]

values_sum = 0
for sequence in sequences:
    values_sum += extrapolate(sequence)

print(f'Sum of extrapolated values:\n{values_sum}')
