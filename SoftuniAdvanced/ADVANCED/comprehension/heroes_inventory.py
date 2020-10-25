heroes = {x: {} for x in input().split(', ')}

while True:
    token = input().split('-')
    name = token[0]

    if name == 'End':
        [print(f"{name} -> Items: {len(heroes[name])}, Cost: {sum(heroes[name].values())}") for name in heroes]
        break

    item = token[1]
    cost = int(token[2])

    if item not in heroes[name]:
        heroes[name][item] = cost

