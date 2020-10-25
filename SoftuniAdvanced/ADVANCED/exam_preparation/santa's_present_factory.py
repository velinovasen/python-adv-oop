from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

presents_cost = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

ready_presents = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while len(materials) > 0 and len(magic_levels) > 0:
    curr_material = materials[-1]
    curr_magic_level = magic_levels[0]
    if curr_material == 0 or curr_magic_level == 0:
        if curr_material == 0:
            materials.pop()
        if curr_magic_level == 0:
            magic_levels.popleft()
        continue

    product = curr_material * curr_magic_level
    if product < 0:
        new_material = curr_material + curr_magic_level
        materials.pop()
        magic_levels.popleft()
        materials.append(new_material)

    if product not in presents_cost and product > 0:
        magic_levels.popleft()
        materials[-1] += 15

    if product in presents_cost:
        ready_presents[presents_cost[product]] += 1
        materials.pop()
        magic_levels.popleft()

if ready_presents["Doll"] > 0 and ready_presents["Wooden train"] > 0 or ready_presents["Teddy bear"] > 0 and ready_presents["Bicycle"] > 0:
    print(f'The presents are crafted! Merry Christmas!')
else:
    print(f'No presents this Christmas!')

materials = materials[::-1]
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

for k, v in sorted(ready_presents.items()):
    if v > 0:
        print(f'{k}: {v}')



