def hash(input):
    value = 0

    for character in input:
        ascii = ord(character)
        value += ascii
        value *= 17
        value %= 256
    
    return value

with open('day15/input.txt', 'r') as f:
    data = f.read()

boxes = {}
for step in data.split(','):
    if '=' in step:
        label = step.split('=')[0]
        focal_length = step.split('=')[1]
        box = hash(label)

        present_values = boxes.get(box, [])
        if any(label in pairs for pairs in present_values):
            for i, item in enumerate(present_values):
                    if item[0] == label:
                        boxes.get(box)[i] = [label, focal_length]
                        break
        else:
            present_values.append([label, focal_length])
        boxes[box] = present_values
    else:
        label = step.split('-')[0]
        box = hash(label)
        present_values = boxes.get(box, [])
        if any(label in pairs for pairs in present_values):
            if len(present_values) < 2:
                del boxes[box]
            else:
                for i, item in enumerate(present_values):
                    if item[0] == label:
                        boxes.get(box).pop(i)
                        break

total_power = 0
for box, values in boxes.items():
    for i, value in enumerate(values):
        total_power += (box + 1) * (i + 1) * int(value[1])

print(f'Total power:\n{total_power}')