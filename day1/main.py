import re

spelled_letters = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("day1/input.txt") as f:
    lines = f.readlines()
total = 0

for line in lines:
    line = line.strip()
    for sp in spelled_letters.items():
        line = line.replace(sp[0], sp[0][0] + sp[1] + sp[0][-1])

    numbers = [number for number in re.findall(r"\d", line)]
    total += int(numbers[0] + numbers[-1])

print(f"The sum in the file:\n{total}")
