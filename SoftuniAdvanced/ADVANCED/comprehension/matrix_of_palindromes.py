row, col = [int(x) for x in input().split()]
matrix = [[f'{chr(row)}{chr(row + col)}{chr(row)}' for col in range(col)] for row in range(97, 97 + row)]
[print(" ".join(row)) for row in matrix]
