import sys
import re

sys.setrecursionlimit(50000)


def sanitize(maze):
    connects_to_north = ['S', '|', '7', 'F']
    connects_to_south = ['S', '|', 'L', 'J']
    connects_to_east = ['S', '-', 'J', '7']
    connects_to_west = ['S', '-', 'L', 'F']

    sanitized_maze = [['.'] * len(maze[i]) for i in range(len(maze))]

    for row in range(len(maze)):
        for col in range(len(maze[0])):
            try:
                if maze[row][col] == '.':
                    continue
                if maze[row][col] == 'S':
                    sanitized_maze[row][col] = 'S'
                elif maze[row][col] == '|':
                    if maze[row - 1][col] in connects_to_north and maze[row + 1][col] in connects_to_south:
                        sanitized_maze[row][col] = '|'
                elif maze[row][col] == '-':
                    if maze[row][col - 1] in connects_to_west and maze[row][col + 1] in connects_to_east:
                        sanitized_maze[row][col] = '-'
                elif maze[row][col] == 'L':
                    if maze[row - 1][col] in connects_to_north and maze[row][col + 1] in connects_to_east:
                        sanitized_maze[row][col] = 'L'
                elif maze[row][col] == 'J':
                    if maze[row - 1][col] in connects_to_north and maze[row][col - 1] in connects_to_west:
                        sanitized_maze[row][col] = 'J'
                elif maze[row][col] == '7':
                    if maze[row + 1][col] in connects_to_south and maze[row][col - 1] in connects_to_west:
                        sanitized_maze[row][col] = '7'
                elif maze[row][col] == 'F':
                    if maze[row + 1][col] in connects_to_south and maze[row][col + 1] in connects_to_east:
                        sanitized_maze[row][col] = 'F'
            except IndexError:
                sanitized_maze[row][col] = '.'

    # changed = True
    # while changed:
    #     changed = False
    #     for row in range(len(sanitized_maze)):
    #         for col in range(len(sanitized_maze[0])):
    #             try:
    #                 if sanitized_maze[row][col] == '.' or sanitized_maze[row][col] == 'S':
    #                     continue
    #                 elif sanitized_maze[row][col] == '|':
    #                     if sanitized_maze[row - 1][col] not in connects_to_north or sanitized_maze[row + 1][col] not in connects_to_south:
    #                         changed = True
    #                         sanitized_maze[row][col] = '.'
    #                 elif sanitized_maze[row][col] == '-':
    #                     if sanitized_maze[row][col - 1] not in connects_to_west or sanitized_maze[row][col + 1] not in connects_to_east:
    #                         changed = True
    #                         sanitized_maze[row][col] = '.'
    #                 elif sanitized_maze[row][col] == 'L':
    #                     if sanitized_maze[row - 1][col] not in connects_to_north or sanitized_maze[row][col + 1] not in connects_to_east:
    #                         changed = True
    #                         sanitized_maze[row][col] = '.'
    #                 elif sanitized_maze[row][col] == 'J':
    #                     if sanitized_maze[row - 1][col] not in connects_to_north or sanitized_maze[row][col - 1] not in connects_to_west:
    #                         changed = True
    #                         sanitized_maze[row][col] = '.'
    #                 elif sanitized_maze[row][col] == '7':
    #                     if sanitized_maze[row + 1][col] not in connects_to_south or sanitized_maze[row][col - 1] not in connects_to_west:
    #                         changed = True
    #                         sanitized_maze[row][col] = '.'
    #                 elif sanitized_maze[row][col] == 'F':
    #                     if sanitized_maze[row - 1][col] not in connects_to_south or sanitized_maze[row][col + 1] not in connects_to_east:
    #                         changed = True
    #                         sanitized_maze[row][col] = '.'
    #             except IndexError:
    #                 changed = True
    #                 sanitized_maze[row][col] = '.'

    return sanitized_maze


def get_order(maze, row, col, visited, order=[]):
    if row < 0 or col < 0:
        order.remove((row, col))
        return
    if row > len(maze) - 1 or col > len(maze[0]) - 1:
        order.remove((row, col))
        return

    if not visited[row][col]:
        visited[row][col] = True
    else:
        return

    order.append((row + 1, col))
    order.append((row - 1, col))
    order.append((row, col + 1))
    order.append((row, col - 1))

    get_order(maze, row + 1, col, visited, order)  # look to the south
    get_order(maze, row - 1, col, visited, order)  # look to the north
    get_order(maze, row, col - 1, visited, order)  # look to the west
    get_order(maze, row, col + 1, visited, order)  # look to the east

    return order


def flood(maze, order, result):
    for row, col in order:
        if maze[row][col] == '.':
            continue
        if isinstance(result[row][col], int):
            continue
        if maze[row][col] not in ['|', '-', 'L', 'J', '7', 'F', 'S']:
            continue

        try:
            # check to the north if needed
            if maze[row][col] in ['|', 'L', 'J']:
                if isinstance(result[row - 1][col], int):
                    result[row][col] = result[row - 1][col] + 1

            # check to the south if needed
            if maze[row][col] in ['|', '7', 'F']:
                if isinstance(result[row + 1][col], int):
                    result[row][col] = result[row + 1][col] + 1

            # check to the west if needed
            if maze[row][col] in ['-', 'J', '7']:
                if isinstance(result[row][col - 1], int):
                    result[row][col] = result[row][col - 1] + 1

            # check to the east if needed
            if maze[row][col] in ['-', 'L', 'F']:
                if isinstance(result[row][col + 1], int):
                    result[row][col] = result[row][col + 1] + 1

        except IndexError:
            result[row][col] = '.'
            continue


with open('day10/input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

sanitized_lines = sanitize(lines)
for i in range(len(sanitized_lines)):
    sanitized_lines[i] = ''.join(sanitized_lines[i])

start = ()
for i, line in enumerate(sanitized_lines):
    if 'S' in line:
        start = (i, line.find('S'))

visited = [[False] * len(sanitized_lines[0])
           for i in range(len(sanitized_lines))]
order = get_order(sanitized_lines, start[0], start[1], visited)

result = [['.'] * len(sanitized_lines[i]) for i in range(len(sanitized_lines))]
result[start[0]][start[1]] = 0
flood(sanitized_lines, order, result)

# for line in result:
#     print(line)

# max_steps = 0
# for line in result:
#     values = [x for x in line if type(x) == int]
#     if values != []:
#         print(line[20:40])
#         highest = max(values)
#         if highest > max_steps:
#             max_steps = highest

# print(f'Maximum number of steps:\n{max_steps}')

for i in range(len(result)):
    for j in range(len(result[0])):
        if result[i][j] == '.':
            result[i][j] = -1

for line in result:
    print(line[25:45])