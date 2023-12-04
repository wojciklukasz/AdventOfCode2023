with open('day4/input.txt') as f:
    lines = f.readlines()

cards = [line.split(':')[1:] for line in lines]
cards_split = [card[0].strip().split('|') for card in cards]
cards_numbers = [[c[0].strip().split(' '), c[1].strip().split(' ')] for c in cards_split]

present = []
for cn in cards_numbers:
    present_dic = {}
    for number in cn[0]:
        if number == '':
            continue
        present_dic[int(number)] = True

    present.append(present_dic)

points_total = 0

for i, cn in enumerate(cards_numbers):
    points = 0
    for number in cn[1]:
        if number == '':
            continue
        if int(number) in present[i].keys():
            if points == 0:
                points = 1
            else:
                points *= 2
    points_total += points

print(f'Sum of points:\n{points_total}')

