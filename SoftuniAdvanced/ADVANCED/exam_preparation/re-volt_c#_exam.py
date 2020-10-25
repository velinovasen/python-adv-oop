size = int(input())
commands_count = int(input())
directions = {"up": (-1, 0), "right": (0, 1), "down": (+1, 0), "left": (0, -1)}
winner = False
matrix = []
start_pos = (0, 0)
[matrix.append(input()) for x in range(size)]
for x in range(len(matrix)):
    if 'f' in matrix[x]:
        start_pos = x, matrix[x].index("f")

row, col = start_pos[0], start_pos[1]


def check_row_col(row, col):
    if row < 0:
        row = size - 1
    elif row == size:
        row = 0
    elif col < 0:
        col = size - 1
    elif col == size:
        col = 0
    return row, col


for _ in range(commands_count):
    command = input()
    row_2, col_2 = row, col

    token = list(matrix[row])
    for x in range(len(token)):
        if token[x] == 'f':
            token[x] = '-'
    matrix[row] = "".join(token)

    row += directions[command][0]
    col += directions[command][1]

    row, col = check_row_col(row, col)

    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'F':
            winner = True

        elif matrix[row][col] == 'B':
            row += directions[command][0]
            col += directions[command][1]
            row, col = check_row_col(row, col)
            if matrix[row][col] == 'F':
                winner = True

        elif matrix[row][col] == 'T':
            row = row_2
            col = col_2

    token_2 = list(matrix[row])
    for y in range(len(token_2)):
        if y == col:
            token_2[y] = 'f'
    matrix[row] = "".join(token_2)

    if winner:
        break

if winner:
    print('Player won!')
else:
    print(f'Player lost!')

[print(x) for x in matrix]

