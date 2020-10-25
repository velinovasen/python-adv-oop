size = int(input())
matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    tokens = input()
    if tokens == 'END':
        break
    action, row, col, num = tokens.split()
    if 0 <= int(row) < size and 0 <= int(col) < size:
        if action == 'Add':
            matrix[int(row)][int(col)] += int(num)
        if action == 'Subtract':
            matrix[int(row)][int(col)] -= int(num)
    else:
        print(f'Invalid coordinates')
[print(" ".join(map(str, row))) for row in matrix]