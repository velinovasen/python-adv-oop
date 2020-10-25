presents_count = int(input())
size = int(input())
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
matrix = []
row, col = 0, 0
happy_nice_kids = 0

for x in range(size):
    line = input().split()
    if "S" in line:
        row, col = x, line.index("S")
    matrix.append(line)

command = input()
while presents_count and command in directions:
    matrix[row][col] = '-'
    new_row = row + directions[command][0]
    new_col = col + directions[command][1]
    if 0 <= new_row < size and 0 <= new_col < size:
        if matrix[new_row][new_col] == 'V':
            presents_count -= 1
            happy_nice_kids += 1
        elif matrix[new_row][new_col] == 'X':
            pass
        elif matrix[new_row][new_col] == 'C':
            for direct in directions:
                row_c = new_row + directions[direct][0]
                col_c = new_col + directions[direct][1]
                if matrix[row_c][col_c] in 'VX':
                    presents_count -= 1
                    happy_nice_kids += 1
                    matrix[row_c][col_c] = '-'
                    if presents_count == 0:
                        break
    else:
        new_row -= directions[command][0]
        new_col -= directions[command][1]

    row, col = new_row, new_col
    matrix[new_row][new_col] = 'S'
    if presents_count:
        command = input()
    else:
        break

nice_kids_left = 0
for y in matrix:
    for x in y:
        if x == 'V':
            nice_kids_left += 1
if not presents_count:
    print('Santa ran out of presents!')
for x in matrix:
    print(" ".join(x))
if nice_kids_left:
    print(f'No presents for {nice_kids_left} nice kid/s.')
else:
    print(f'Good job, Santa! {happy_nice_kids} happy nice kid/s.')