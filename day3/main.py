from functools import reduce


def is_valid_part(schematic, number_row, column_start, column_end, number, gears):
    row = number_row - 1
    for row in range(row, row + 3):
        if row < 0:
            continue

        column = column_start - 1
        while column <= column_end + 1:
            if column < 0:
                column += 1
                continue

            try:
                character = schematic[row][column]
            except IndexError:
                break

            if character != '.' and not character.isdigit():
                key = f'{row},{column}'
                if character == '*':
                    if key in gears:
                        gears[key].append(int(number))
                    else:
                        gears[key] = [int(number)]
                return True

            column += 1

    return False


with open('day3/input.txt', 'r') as f:
    lines = f.readlines()

schematic = [list(l.strip()) for l in lines]

parts_sum = 0
gears = {}
for row in range(len(schematic)):
    column = 0
    number = ''
    while column < len(schematic[row]):
        ch = schematic[row][column]
        if ch.isdigit():
            column_start = column
            column_end = column
            number = number + ch
            column += 1

            while column < len(schematic[row]):
                ch = schematic[row][column]
                if ch.isdigit():
                    number = number + ch
                    column_end += 1
                    column += 1
                else:
                    if is_valid_part(schematic, row, column_start, column_end, number, gears):
                        parts_sum += int(number)
                    number = ''
                    break

            if number != '':
                if is_valid_part(schematic, row, column_start, column_end, number, gears):
                    parts_sum += int(number)
                number = ''
        else:
            column += 1

gears_ratio_sum = 0
for gear, parts in gears.items():
    if len(parts) > 1:
        ratio = reduce(lambda x, y: x * y, parts)
        gears_ratio_sum += ratio


print(f'Sum of all part numbers in the engine:\n{parts_sum}')
print(f'Sum of all gear ratios in the engine:\n{gears_ratio_sum}')
