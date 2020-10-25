bunker = {x: {} for x in input().split(', ')}
total_items = 0
total_quality = 0
for _ in range(int(input())):
    section, type_of, description = input().split(' - ')
    quant, qualit = description.split(';')

    if type_of not in bunker[section]:
        act_quantity = quant.split(':')[1]
        act_quality = qualit.split(':')[1]
        bunker[section][type_of] = [int(act_quantity), int(act_quality)]
        total_items += int(act_quantity)
        total_quality += int(act_quality)

    else:
        bunker[section][type_of][0] += quant
        bunker[section][type_of][1] += qualit

print(f'Count of items: {total_items}')
avg = total_quality / len(bunker)
print(f'Average quality: {avg:.2f}')
[print(f'{categorie} -> {", ".join(bunker[categorie].keys())}') for categorie in bunker]