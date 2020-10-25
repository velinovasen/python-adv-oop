from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casing = [int(x) for x in input().split(", ")]

materials = {40: "Datura Bombs", 60: "Cherry Bombs", 120: "Smoke Decoy Bombs"}
ready_bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
rdy = False

while bomb_effects and bomb_casing and not rdy:
    bomb_eff = bomb_effects.popleft()
    bomb_cas = bomb_casing.pop()
    if bomb_eff + bomb_cas in materials:
        key_dic = bomb_eff + bomb_cas
        ready_bombs[materials[key_dic]] += 1
        counter_rdy = 0
        for key, value in ready_bombs.items():
            if value >= 3:
                counter_rdy += 1
        if counter_rdy >= 3:
            rdy = True
            break

    else:
        bomb_effects.appendleft(bomb_eff)
        bomb_casing.append(bomb_cas - 5)

if rdy:
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print(f"You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print(f"Bomb Effects: empty")
if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casing])}")
else:
    print(f"Bomb Casings: empty")

for key, value in sorted(ready_bombs.items()):
    print(f"{key}: {value}")