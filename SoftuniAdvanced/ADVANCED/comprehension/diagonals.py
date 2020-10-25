size = int(input())
matrix = [[x for x in input().split(', ')] for y in range(size)]
first_diag = [int(matrix[x][x]) for x in range(len(matrix))]
second_diag = [int(matrix[len(matrix) - 1 - x][x]) for x in range(len(matrix) - 1, - 1, -1)]
print(f'First diagonal: {", ".join(map(str, first_diag))}. Sum: {sum(first_diag)}')
print(f'Second diagonal: {", ".join(map(str, second_diag))}. Sum: {sum(second_diag)}')