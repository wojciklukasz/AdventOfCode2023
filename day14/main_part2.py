def rotate(columns):
    rows = list(map(list, zip(*columns)))
    rotated_rows = list(map(list, zip(*rows[::-1])))
    columns = list(map(list, zip(*rotated_rows)))
    return columns


def find_fist_free_space(column, index):
    free_space = index
    while column[free_space] != '.':
        free_space += 1
        if free_space >= len(column):
            return len(column)
    return free_space


def make_cycle(rows, seen):
    columns = list(map(list, zip(*rows)))
    loop_found = False
    loop_at = -1
    for rotation in range(4):
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
        
        columns = rotate(columns)

    if columns in seen:
        print(f'Identical to {seen.index(columns)}')
        loop_found = True
        loop_at = seen.index(columns)
    else:
        seen.append(columns)

    rows = list(map(list, zip(*columns)))
    
    return rows, loop_found, loop_at


with open('day14/input.txt') as f:
    lines = f.read().splitlines()

rows = [[*line] for line in lines]
seen = []

loop_found = False
looped_cycle = -1
loop_at = -1
cycles = 1000000000
for cycle in range(cycles):
    rows, loop_found, loop_at = make_cycle(rows, seen)

    if loop_found:
        print(f'Loop in {cycle}')
        looped_cycle = cycle - loop_at
        break


rows = [[*line] for line in lines]

additional_cycles = cycles % looped_cycle
for cycle in range(looped_cycle + additional_cycles):
    rows, _, _ = make_cycle(rows, [])


for row in rows:
    print(row)

total_load = 0
for i, row in enumerate(rows):
    total_load += row.count('O') * (len(rows) - i)

print(f'Total load:\n{total_load}')
