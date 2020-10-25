def build_matrix():
    matrix = []
    for x in range(int(input())):
        matrix.append([int(x) for x in input().split(' ')])
    return matrix


def find_diagonal():
    matrix = build_matrix()
    first_diag = 0
    second_diag = 0
    token = len(matrix) - 1
    for x in range(len(matrix)):
        first_diag += matrix[x][x]
        second_diag += matrix[x][token]
        token -= 1
    return abs(first_diag - second_diag)

print(find_diagonal())

'''⦁	Diagonal Difference
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
 
Input
⦁	On the first line, you are given the integer N - the size of the square matrix
⦁	The next N lines hold the values for every row - N numbers separated by a space
Output
⦁	Print the absolute difference between the sums of the primary and the secondary diagonal
Examples
Input	Output	Comments
3
11 2 4
4 5 6
10 8 -12	15	Primary diagonal: sum = 11 + 5 + (-12) = 4
Secondary diagonal: sum = 4 + 5 + 10 = 19
Difference: |4 - 19| = 15
'''