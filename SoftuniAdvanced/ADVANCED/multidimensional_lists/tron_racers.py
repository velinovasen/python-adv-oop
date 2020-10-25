size = int(input())


def build_matrix():
    matrix = []
    first_player_pos = []
    second_player_pos = []
    for n in range(size):
        matrix.append([])
        for y in input():
            matrix[n].append(y)
            if y == 'f':
                first_player_pos = [n, matrix[n].index(y)]
            if y == 's':
                second_player_pos = [n, matrix[n].index(y)]
    return matrix, first_player_pos, second_player_pos


def track_down():
    tokens = build_matrix()
    matrix, first_player_pos, second_player_pos = tokens[0], tokens[1], tokens[2]
    p1_row, p1_col, p2_row, p2_col = tokens[1][0], tokens[1][1], tokens[2][0], tokens[2][1]

    while True:
        p1_move, p2_move = input().split()

        if p1_move == 'up':
            if first_player_pos[0] == 0:
                pass
            elif matrix[p1_row - 1][p1_col] == 's':
                matrix[p1_row - 1][p1_col] = 'x'
                break
            else:
                matrix[p1_row - 1][p1_col] = 'f'
                p1_row -= 1

        elif p1_move == 'right':
            if p1_col == len(matrix[p1_row]):
                pass
            elif matrix[p1_row][p1_col + 1] == 's':
                matrix[p1_row][p1_col + 1] = 'x'
                break
            else:
                matrix[p1_row][p1_col + 1] = 'f'
                p1_col += 1

        elif p1_move == 'down':
            if p1_row == len(matrix):
                pass
            elif matrix[p1_row + 1][p1_col] == 's':
                matrix[p1_row + 1][p1_col] = 'x'
                break
            else:
                matrix[p1_row + 1][p1_col] = 'f'
                p1_row += 1

        elif p1_move == 'left':
            if p1_col == 0:
                pass
            elif matrix[p1_row][p1_col - 1] == 's':
                matrix[p1_row][p1_col - 1] = 'x'
                break
            else:
                matrix[p1_row][p1_col - 1] = 'f'
                p1_col -= 1

        if p2_move == 'up':
            if p2_row == 0:
                pass
            elif matrix[p2_row - 1][p2_col] == 'f':
                matrix[p2_row - 1][p2_col] = 'x'
                break
            else:
                matrix[p2_row - 1][p2_col] = 's'
                p2_row -= 1

        elif p2_move == 'right':
            if p2_col == len(matrix[p2_row]):
                pass
            elif matrix[p2_row][p2_col + 1] == 'f':
                matrix[p2_row][p2_col + 1] = 'x'
                break
            else:
                matrix[p2_row][p2_col + 1] = 's'
                p2_col += 1

        elif p2_move == 'down':
            if p2_row == len(matrix):
                pass
            elif matrix[p2_row + 1][p2_col] == 'f':
                matrix[p2_row + 1][p2_col] = 'x'
                break
            else:
                matrix[p2_row + 1][p2_col] = 's'
                p2_row += 1

        elif p2_move == 'left':
            if p2_col == 0:
                pass
            elif matrix[p2_row][p2_col - 1] == 'f':
                matrix[p2_row][p2_col - 1] = 'x'
                break
            else:
                matrix[p2_row][p2_col - 1] = 's'
                p2_col -= 1

    for x in range(len(matrix)):
        print("".join([x for x in matrix[x]]))


track_down()