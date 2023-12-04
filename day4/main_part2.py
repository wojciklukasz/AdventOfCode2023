def find_matches(present, numbers):
    matches = 0

    for number in numbers:
        if number == '':
            continue
        if int(number) in present.keys():
            matches += 1

    return matches


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

cards_num = {}
for card in range(len(cards)):
    cards_num[card] = 1

for card in range(len(present)):
    print(f'Card: {card}')
    if card in cards_num.keys():
        for i in range(cards_num[card]):
            matches = find_matches(present[card], cards_numbers[card][1])

            for match in range(matches):
                card_added = card + 1 + match
                if card_added not in cards_num.keys():
                    cards_num[card_added] = 1
                else:
                    cards_num[card_added] += 1


print(f'Total scratchcards:\n{sum(cards_num.values())}')
