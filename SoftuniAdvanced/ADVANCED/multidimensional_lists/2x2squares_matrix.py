def build_matrix():
    matrix = []
    rows, cols = [int(x) for x in input().split(' ')]
    for x in range(rows):
        matrix.append([x for x in input().split(' ')])
    return matrix


def get_square():
    count = 0
    matrix = build_matrix()
    for x in range(len(matrix) - 1):
        for y in range(len(matrix[x]) - 1):
            if matrix[x][y] == matrix[x][y + 1] == matrix[x + 1][y] == matrix[x + 1][y + 1]:
                count += 1
    return count


print(get_square())

'''⦁	2X2 Squares in Matrix
Find the count of 2 x 2 squares of equal chars in a matrix.
Input
⦁	On the first line, you are given the integers rows and cols - the matrix's dimensions
⦁	Matrix characters come at the next rows lines (space separated)
Output
⦁	Print the number of all the square matrixes you have found
Examples
Input	Output	Comments
3 4
A B B D
E B B B
I J B B	2	Two 2 x 2 squares of equal cells:
A B B D	A B B D
E B B B	E B B B
I J B B	I J B B
2 2
a b
c d	0	No 2 x 2 squares of equal cells exist.
'''
