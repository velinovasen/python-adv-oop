def build_matrix():
    matrix = []
    for x in range(int(input())):
        matrix.append([int(x) for x in input().split()])
    return matrix

def explode(matrix, square, row, col):
    if len(matrix) > row > 0:
        if 0 < col < len(matrix[row]):
            if matrix[row - 1][col] > 0:
                matrix[row - 1][col] -= square
            if matrix[row - 1][col - 1] > 0:
                matrix[row - 1][col - 1] -= square
            if matrix[row - 1][col + 1] > 0:
                matrix[row - 1][col + 1] -= square
            if matrix[row][col - 1] > 0:
                matrix[row][col - 1] -= square
            if matrix[row][col + 1] > 0:
                matrix[row][col + 1] -= square
            if matrix[row + 1][col] > 0:
                matrix[row + 1][col] -= square
            if matrix[row + 1][col] > 0:
                matrix[row + 1][col] -= square


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

bomb_squad()