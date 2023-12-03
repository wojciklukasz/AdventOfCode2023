with open('day2/input.txt', 'r') as f:
    games = f.readlines()

red_limit = 12
green_limit = 13
blue_limit = 14

ids_sum = 0
sets_power_sum = 0
for game in games:
    game_id = int(game.split(':')[0].split(' ')[1].replace(':', ''))
    rounds = game.split(':')[1].split(';')

    failed = False
    r_min, g_min, b_min = 0, 0, 0
    for rd in rounds:
        r, g, b = 0, 0, 0
        colors = rd.split(',')

        for color in colors:
            color = color.strip()
            if 'red' in color:
                r += int(color.split(' ')[0])
            if 'green' in color:
                g += int(color.split(' ')[0])
            if 'blue' in color:
                b += int(color.split(' ')[0])
        
        if r > red_limit or g > green_limit or b > blue_limit:
            failed = True
        
        r_min = max(r_min, r)
        g_min = max(g_min, g)
        b_min = max(b_min, b)
    
    if not failed:
        ids_sum += game_id
    
    game_power = r_min * g_min * b_min
    sets_power_sum += game_power

print(f'Sum of valid games IDs:\n{ids_sum}')
print(f'Sum of the power of sets:\n{sets_power_sum}')
