from collections import deque

first_box = deque([int(x) for x in input().split()])
second_box = [int(x) for x in input().split()]
my_collection = []

while first_box and second_box:
    first_item = first_box[0]
    second_item = second_box.pop()
    if (first_item + second_item) % 2 == 0:
        first_box.popleft()
        my_collection.append(first_item + second_item)
    else:
        first_box.append(second_item)

if not first_box:
    print('First lootbox is empty')
elif not second_box:
    print('Second lootbox is empty')

if sum(my_collection) >= 100:
    print(f'Your loot was epic! Value: {sum(my_collection)}')
else:
    print(f'Your loot was poor... Value: {sum(my_collection)}')
