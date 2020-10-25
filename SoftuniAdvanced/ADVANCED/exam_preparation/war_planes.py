def build_matrix():
    matrix = []
    [matrix.append(input().split()) for _ in range(int(input()))]
    return matrix


def find_positions(matrix):
    player_position = []
    target_positions = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 'p':
                player_position = [x, y]
            elif matrix[x][y] == 't':
                target_positions.append([x, y])
    return player_position, target_positions


def move(matrix, direction, pos_count, pp):
    matrix = matrix
    pp = pp
    if direction == 'up':
        if 0 <= pp[0] - pos_count < len(matrix) and matrix[pp[0] - pos_count][pp[1]] == '.':
            matrix[pp[0]][pp[1]] = '.'
            pp = [pp[0] - pos_count, pp[1]]

    elif direction == 'right':
        if 0 <= pp[1] + pos_count < len(matrix) and matrix[pp[0]][pp[1] + pos_count] == '.':
            matrix[pp[0]][pp[1]] = '.'
            pp = [pp[0], pp[1] + pos_count]

    elif direction == 'down':
        if 0 <= pp[0] + pos_count < len(matrix) and matrix[pp[0] + pos_count][pp[1]] == '.':
            matrix[pp[0]][pp[1]] = '.'
            pp = [pp[0] + pos_count, pp[1]]

    elif direction == 'left':
        if 0 <= pp[1] - pos_count < len(matrix) and matrix[pp[0]][pp[1] - pos_count] == '.':
            matrix[pp[0]][pp[1]] = '.'
            pp = [pp[0], pp[1] - pos_count]
    matrix[pp[0]][pp[1]] = 'p'
    return matrix, pp


def shoot(matrix, direction, pos_count, pp, targets_left):
    matrix = matrix
    targets_left = targets_left
    if direction == 'up':
        if 0 <= pp[0] - pos_count < len(matrix) and matrix[pp[0] - pos_count][pp[1]] in 't.':
            if matrix[pp[0] - pos_count][pp[1]] == 't':
                targets_left -= 1
            matrix[pp[0] - pos_count][pp[1]] = 'x'

    elif direction == 'right':
        if 0 <= pp[1] + pos_count < len(matrix) and matrix[pp[0]][pp[1] + 1] in 't.':
            if matrix[pp[0]][pp[1] + pos_count] == 't':
                targets_left -= 1
            matrix[pp[0]][pp[1] + pos_count] = 'x'

    elif direction == 'down':
        if 0 <= pp[0] + pos_count < len(matrix) and matrix[pp[0] + pos_count][pp[1]] in 't.':
            if matrix[pp[0] + pos_count][pp[1]] == 't':
                targets_left -= 1
            matrix[pp[0] + pos_count][pp[1]] = 'x'

    elif direction == 'left':
        if 0 <= pp[1] - pos_count < len(matrix) and matrix[pp[0]][pp[1] - 1] in 't.':
            if matrix[pp[0]][pp[1] - pos_count] == 't':
                targets_left -= 1
            matrix[pp[0]][pp[1] - pos_count] = 'x'

    return matrix, targets_left


def play():
    matrix = build_matrix()
    player_position, target_positions = find_positions(matrix)
    targets_left = len(target_positions)
    targets_at_beg = len(target_positions)
    for x in range(int(input())):
        action, direction, pos_count = input().split()
        if action == 'move':
            matrix, player_position = move(matrix, direction, int(pos_count), player_position)

        elif action == 'shoot':
            matrix, targets_left = shoot(matrix, direction, int(pos_count), player_position, targets_left)

        if targets_left == 0:
            print(f'Mission accomplished! All {targets_at_beg} targets destroyed.')
            break
    if targets_left:
        print(f'Mission failed! {targets_left} targets left.')
    [print(" ".join(x)) for x in matrix]

play()