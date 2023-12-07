def get_type(hand):
    occurences = {}
    for card in hand:
        occurences[card] = occurences.get(card, 0) + 1
    occurences = sorted(occurences.values(), reverse=True)
    
    if occurences[0] == 5:
        return 7 # five of a kind
    elif occurences[0] == 4:
        return 6 # four of a kind
    elif occurences[0] == 3 and occurences[1] == 2:
        return 5 # full house
    elif occurences[0] == 3:
        return 4 # three of a kind
    elif occurences[0] == 2 and occurences[1] == 2:
        return 3 # two pairs
    elif occurences[0] == 2:
        return 2 # one pair
    else:
        return 1 # high card

with open('day7/input.txt', 'r') as f:
    lines = f.readlines()


cards_strength = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}
for i in range(2, 10):
    cards_strength[str(i)] = i


hands = [line.split(' ')[0].strip() for line in lines]
bids = [int(line.split(' ')[1].strip()) for line in lines]
bids_dict = {}
for hand, bid in zip(hands, bids):
    bids_dict[hand] = bid

types = {}
for hand in hands:
    types[hand] = get_type(hand)

sorted_hands = sorted(types.items(), key=lambda x: (x[1],
                                                    cards_strength.get(x[0][0]),
                                                    cards_strength.get(x[0][1]),
                                                    cards_strength.get(x[0][2]),
                                                    cards_strength.get(x[0][3]),
                                                    cards_strength.get(x[0][4])))

total_winnings = 0
rank = 1
for hand in sorted_hands:
    total_winnings += bids_dict[hand[0]] * rank
    rank += 1

print(f'Total winnings:\n{total_winnings}')
