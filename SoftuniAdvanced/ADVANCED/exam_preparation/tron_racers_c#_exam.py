directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
size = int(input())
matrix = []
[matrix.append(input()) for _ in range(size)]
f_p_pos = [0, 0]
s_p_pos = [0, 0]
winner = False
for x in range(len(matrix)):
    if "f" or "s" in matrix[x]:
        if "f" in matrix[x]:
            f_p_pos = (x, matrix[x].index('f'))
        if "s" in matrix[x]:
            s_p_pos = (x, matrix[x].index('s'))


def check_real_idx(row, col):
    if row < 0:
        row = size - 1
    elif row >= size:
        row = 0
    if col < 0:
        col = size - 1
    elif col >= size:
        col = 0
    return row, col


while not winner:
    f_p_command, s_p_command = input().split()
    new_row_1, new_col_1 = f_p_pos[0] + directions[f_p_command][0], f_p_pos[1] + directions[f_p_command][1]
    new_row_2, new_col_2 = s_p_pos[0] + directions[s_p_command][0], s_p_pos[1] + directions[s_p_command][1]
    new_row_1, new_col_1 = check_real_idx(new_row_1, new_col_1)
    new_row_2, new_col_2 = check_real_idx(new_row_2, new_col_2)
    if matrix[new_row_1][new_col_1] != 's':
        token = list(matrix[new_row_1])
        token[new_col_1] = 'f'
        matrix[new_row_1] = "".join(token)
    else:
        token = list(matrix[new_row_1])
        token[new_col_1] = 'x'
        matrix[new_row_1] = "".join(token)
        winner = True
        break
    if matrix[new_row_2][new_col_2] != 'f':
        token = list(matrix[new_row_2])
        token[new_col_2] = 's'
        matrix[new_row_2] = "".join(token)
    else:
        token = list(matrix[new_row_2])
        token[new_col_2] = 'x'
        matrix[new_row_2] = "".join(token)
        winner = True
        break

    f_p_pos = [new_row_1, new_col_1]
    s_p_pos = [new_row_2, new_col_2]

[print(x) for x in matrix]