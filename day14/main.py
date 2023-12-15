def find_fist_free_space(column, index):
    free_space = index
    while column[free_space] != '.':
        free_space += 1
        if free_space >= len(column):
            return len(column)
    return free_space


with open('day14/input_test.txt') as f:
    lines = f.read().splitlines()

columns = list(map(list, zip(*lines)))

for column in columns:
    free_space = len(column)

    for i, space in enumerate(column):
        if space == '.' and free_space > i:
            free_space = i
        elif space == 'O' and i > free_space:
            column[i] = '.'
            column[free_space] = 'O'
            free_space = find_fist_free_space(column, free_space)
        elif space == '#' and i > free_space:
            free_space = find_fist_free_space(column, i)

rows = list(map(list, zip(*columns)))

total_load = 0
for i, row in enumerate(rows):
    total_load += row.count('O') * (len(rows) - i)

print(f'Total load:\n{total_load}')
