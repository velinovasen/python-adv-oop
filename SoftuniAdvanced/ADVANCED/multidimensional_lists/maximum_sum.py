import sys


def build_matrix():
    rows, cols = input().split()
    matrix = []
    for x in range(int(rows)):
        tokens = [int(y) for y in input().split()]
        matrix.append(tokens)
    return matrix


def calculate_matrix():
    matrix = build_matrix()
    best_rectangular = -sys.maxsize
    best_start = None

    for x in range(len(matrix) - 2):
        for y in range(len(matrix[x]) - 2):
            curr_rectangular = 0
            curr_rectangular += (
                        matrix[x][y] + matrix[x][y + 1] + matrix[x][y + 2] + matrix[x + 1][y] + matrix[x + 1][y + 1] +
                        matrix[x + 1][y + 2] + matrix[x + 2][y] + matrix[x + 2][y + 1] + matrix[x + 2][y + 2])
            if curr_rectangular > best_rectangular:
                best_rectangular = curr_rectangular
                rows, cols = x, y
                best_start = (rows, cols)
    rows, cols = best_start[0], best_start[1]

    best_matrix = []
    for n in range(3):
        col_upd = cols
        best_matrix.append([])
        for m in range(3):
            best_matrix[n].append(matrix[rows][col_upd])
            col_upd += 1

        rows += 1

    print(f'Sum = {best_rectangular}')
    for q in range(len(best_matrix)):
        print(' '.join([str(x) for x in best_matrix[q]]))


calculate_matrix()



'''⦁	Maximal Sum
Write a program that reads a rectangular integer matrix of size N x M and finds in it the square 3 x 3 that has maximal sum of its elements.
Input
⦁	On the first line, you will receive the rows N and columns M. On the next N lines you will receive each row with its columns
Output
⦁	Print the elements of the 3 x 3 square as a matrix, along with their sum
Examples
Input	Matrix	Output
4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4	 	Sum = 75
1 4 14
7 11 2
8 12 16
'''