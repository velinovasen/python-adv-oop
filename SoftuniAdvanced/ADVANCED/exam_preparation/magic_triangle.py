def get_magic_triangle(num):
    matrix = [[1], [1, 1]]
    for row in range(2, num):
        matrix.append([0 for _ in range(row + 1)])
        for col in range(row + 1):
            if col - 1 >= 0:
                left = matrix[row - 1][col - 1]
                if col < row:
                    right = matrix[row - 1][col]
                else:
                    right = 0
                matrix[row][col] = left + right
            else:
                matrix[row][col] = 1
    return matrix

print(get_magic_triangle(10))