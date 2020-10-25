size = int(input())
matrix = []
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
row, col = 0, 0
food_eaten = 0
burrow_one = None
burrow_two = None
for x in range(size):
    line = list(input())
    if "S" in line:
        row, col = x, line.index("S")
    if "B" in line:
        if not burrow_one:
            burrow_one = [x, line.index("B")]
        else:
            burrow_two = [x, line.index("B")]
    matrix.append(line)

while food_eaten < 10:
    command = input()

    new_row = row + directions[command][0]
    new_col = col + directions[command][1]
    matrix[row][col] = '.'
    if 0 <= new_row < size and 0 <= new_col < size:
        if matrix[new_row][new_col] == '*':
            food_eaten += 1
        elif matrix[new_row][new_col] == 'B':
            matrix[new_row][new_col] = '.'
            if new_row == burrow_one[0] and new_col == burrow_one[1]:
                new_row = burrow_two[0]
                new_col = burrow_two[1]
            else:
                new_row = burrow_one[0]
                new_col = burrow_one[1]
        matrix[new_row][new_col] = 'S'
        row, col = new_row, new_col
    else:
        break

if food_eaten >= 10:
    print(f'You won! You fed the snake.')
else:
    print("Game over!")
print(f'Food eaten: {food_eaten}')
for x in matrix:
    print("".join(x))