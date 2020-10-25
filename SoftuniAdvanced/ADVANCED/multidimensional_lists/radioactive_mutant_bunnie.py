def build_matrix():
    rows, cols = [int(x) for x in input().split()]
    matrix = []
    for _ in range(rows):
        matrix.append([x for x in input().split()])
    commands = input().split()
    matrix.append(commands)
    return matrix

def lair():
    matrix = build_matrix()
    commands = matrix.pop()
    player_spot = []
    dead = False
    won = False
    for r in range(len(matrix)):
        rng = sum(1 for x in matrix[r]) + str(matrix[r]).count('.')
        for c in range(rng - 1):
            if matrix[r][c] == 'P':
                row = r
                col = c

    for command in commands:
        row, col = player_spot[0], player_spot[1]
        if command == 'U':
            if row - 1 >= 0:
                if matrix[row - 1][col] == 'B':
                    dead = True
                    break
                else:
                    matrix[row - 1][col] = 'P'
                    matrix[row][col] = '.'
                    row -= 1

            if dead:
                break
        elif command == 'D':
            if row + 1 < len(matrix):
                if matrix[row + 1][col] == 'B':
                    dead = True
                    break
                else:
                    matrix[row + 1][col] = 'P'
                    matrix[row][col] = '.'
                    row += 1

            if dead:
                break

        elif command == 'L':
            if col - 1 >= 0:
                if matrix[row][col - 1] == 'B':
                    dead = True
                    break
                else:
                    matrix[row][col - 1] = 'P'
                    matrix[row][col] = '.'
                    col -= 1

            if dead:
                break

        elif command == 'R':
            if col + 1 < len(matrix[0]):
                if matrix[row][col + 1] == 'B':
                    dead = True
                    break
                else:
                    matrix[row][col + 1] = 'P'
                    matrix[row][col] = '.'
                    col += 1
            if dead:
                break

    return print(matrix)

lair()