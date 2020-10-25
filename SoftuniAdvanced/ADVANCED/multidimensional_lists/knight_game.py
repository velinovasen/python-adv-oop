def get_damage(row, col, matrix):
    counter = 0
    if row - 2 >= 0 and col - 1 >= 0:
        if matrix[row - 2][col - 1] == 'K':
            counter += 1
    if row - 2 >= 0 and col + 1 < len(matrix):
        if matrix[row - 2][col + 1] == 'K':
            counter += 1
    if row - 1 >= 0 and col - 2 >= 0:
        if matrix[row - 1][col - 2] == 'K':
            counter += 1
    if row - 1 >= 0 and col + 2 < len(matrix):
        if matrix[row - 1][col + 2] == 'K':
            counter += 1
    if row + 1 < len(matrix) and col - 2 >= 0:
        if matrix[row + 1][col - 2] == 'K':
            counter += 1
    if row + 1 < len(matrix) and col + 2 < len(matrix):
        if matrix[row + 1][col + 2] == 'K':
            counter += 1
    if row + 2 < len(matrix) and col - 1 >= 0:
        if matrix[row + 2][col - 1] == 'K':
            counter += 1
    if row + 2 < len(matrix) and col + 1 < len(matrix):
        if matrix[row + 2][col + 1] == 'K':
            counter += 1
    return counter


def build_chessboard():
    rows = int(input())
    matrix = []
    for _ in range(rows):
        matrix.append([x for x in input()])
    return matrix


def clear_horses():
    matrix = build_chessboard()
    most_dmg_position = None
    horses_removed = 0
    while True:
        max_dmg = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 'K':
                    damage = get_damage(row, col, matrix)
                    if damage > max_dmg:
                        max_dmg = damage
                        most_dmg_position = [row, col]
        if max_dmg == 0:
            break
        else:
            rr = most_dmg_position[0]
            cc = most_dmg_position[1]
            matrix[rr][cc] = 'O'
            horses_removed += 1
    return print(horses_removed)


clear_horses()



'''⦁	Knight Game
Chess is the oldest game, but it is still popular these days. For this task we will use only one chess piece - the Knight. 
The knight moves to the nearest square but not on the same row, column, or diagonal. (This can be thought of as moving two squares horizontally, then one square vertically, or moving one square horizontally then two squares vertically - i.e. in an "L" pattern.) 
The knight game is played on a board with dimensions N x N and a lot of chess knights 0 <= K <= N2. 
You will receive a board with K for knights and '0' for empty cells. Your task is to remove a minimum of the knights, so there will be no knights left that can attack another knight. 
Input
⦁	On the first line, you will receive the N size of the board
⦁	On the next N lines, you will receive strings with Ks and 0s.
Output
Print a single integer with the minimum number of knights that needs to be removed
Constraints
⦁	Size of the board will be 0 < N < 30
⦁	Time limit: 0.3 sec. Memory limit: 16 MB.
Examples
Input	Output
5 
0K0K0
K000K
00K00
K000K
0K0K0	1

2
KK
KK	0
8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK	12
'''