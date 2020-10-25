tokens = list(input())
size = int(input())
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
matrix = []
row, col = 0, 0

for x in range(size):
    line = list(input())
    if "P" in line:
        row, col = x, line.index("P")
    matrix.append(line)

while True:
    command = input()
    if command == "end":
        print(f"{''.join(tokens)}")
        for x in matrix:
            print("".join(x))
        break
    matrix[row][col] = '-'
    next_row = row + directions[command][0]
    next_col = col + directions[command][1]
    if 0 <= next_row < size and 0 <= next_col < size:
        if matrix[next_row][next_col] != "-":
            tokens.append(matrix[next_row][next_col])

    else:
        next_row -= directions[command][0]
        next_col -= directions[command][1]
        if tokens:
            tokens.pop()
    matrix[next_row][next_col] = 'P'
    row, col = next_row, next_col