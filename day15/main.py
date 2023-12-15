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

hash_sum = 0
for step in data.split(','):
    hash_sum += hash(step)

print(f'Sum of hashes:\n{hash_sum}')