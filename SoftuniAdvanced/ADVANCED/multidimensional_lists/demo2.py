def build_matrix():
    matrix = []
    size = int(input())
    for x in range(size):
        matrix.append([int(x) for x in input().split()])
    return matrix


def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and col <= 0 < len(matrix)


def explode(matrix, square, row, col):
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if is_valid(row, col, matrix) and matrix[r][c] > 0:
                matrix[r][c] -= square


def bomb_squad():
    matrix = build_matrix()
    bombs = input().split()
    for bomb in bombs:
        coordinates = [int(x) for x in bomb.split(',')]
        row, col = coordinates[0], coordinates[1]
        square = matrix[row][col]
        if square <= 0:
            pass
        else:
            explode(matrix, square, row, col)
            matrix[row][col] = 0


    print(matrix)
bomb_squad()