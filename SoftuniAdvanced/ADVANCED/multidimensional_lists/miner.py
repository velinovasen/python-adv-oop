def build_matrix():
    rows = int(input())
    matrix = []
    commands = input().split()
    for _ in range(rows):
        matrix.append([x for x in input().split()])
    matrix.append(commands)
    return matrix


def check_for_coal(matrix):
    coal = False
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 'c':
                coal = True
    return coal


def start_position(matrix):
    start_pos = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 's':
                start_pos.append(row)
                start_pos.append(col)
    return start_pos


def coals_left(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 'c':
                count += 1
    return count


def mining():
    matrix = build_matrix()
    commands = matrix.pop()
    coal_count = 0
    start_pos = start_position(matrix)
    row, col = start_pos[0], start_pos[1]
    coal_left = coals_left(matrix)
    curr_pos = [row, col]
    row, col = curr_pos[0], curr_pos[1]
    com_count = 0
    final_stat = ''
    for command in commands:
        com_count += 1
        if check_for_coal(matrix):
            token = ''
            if command == 'up':
                if row - 1 >= 0:
                    token = matrix[row - 1][col]
                    row -= 1
            elif command == 'right':
                if col + 1 < len(matrix):
                    token = matrix[row][col + 1]
                    col += 1
            elif command == 'down':
                if row + 1 < len(matrix):
                    token = matrix[row + 1][col]
                    row += 1
            elif command == 'left':
                if col - 1 >= 0:
                    token = matrix[row][col - 1]
                    col -= 1

            if token == 'e':
                final_stat = f'Game over!'
                break

            elif token == 'c':
                coal_count += 1
                coal_left -= 1
                matrix[row][col] = '*'

    if coal_left > 0:
        final_stat = f'{coal_left} coals left.'
    else:
        final_stat = f'You collected all coals!'

    return print(f'{final_stat} ({row}, {col})')

mining()


'''⦁	*Miner
We get as input the size of the field in which our miner moves. The field is always a square. After that we will receive the commands which represent the directions in which the miner should move. The miner starts from position - 's'. The commands will be: left, right, up and down. If the miner has reached a side edge of the field and the next command indicates that he has to get out of the field, he must remain on his current possition and ignore the current command. The possible characters that may appear on the screen are:
⦁	* - a regular position on the field.
⦁	e - the end of the route. 
⦁	c  - coal
⦁	s - the place where the miner starts
Each time when the miner finds a coal, he collects it and replaces it with '*'. Keep track of the count of the collected coals. If the miner collects all of the coals in the field, the program stops and you have to print the following message: "You collected all coals! ({rowIndex}, {colIndex})".
If the miner steps at 'e' the game is over (the program stops) and you have to print the following message: "Game over! ({rowIndex}, {colIndex})".
If there are no more commands and none of the above cases had happened, you have to print the following message: "{remainingCoals} coals left. ({rowIndex}, {colIndex})".
Input
⦁	Field size - an integer number.
⦁	Commands to move the miner - an array of strings separated by " ".
⦁	The field: some of the following characters (*, e, c, s), separated by whitespace (" ");
Output
⦁	There are three types of output:
⦁	If all the coals have been collected, print the following output: "You collected all coals! ({rowIndex}, {colIndex})"
⦁	If you have reached the end, you have to stop moving and print the following line: "Game over! ({rowIndex}, {colIndex})"
⦁	If there are no more commands and none of the above cases had happened, you have to print the following message: "{totalCoals} coals left. ({rowIndex}, {colIndex})"
Constraints
⦁	The field size will be a 32-bit integer in the range [0 … 2 147 483 647].
⦁	The field will always have only one's'.
⦁	Allowed working time for your program: 0.1 seconds.
⦁	Allowed memory: 16 MB.
Examples
Input	Output
5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *	Game over! (1, 3)
4
up right right right down
* * * e
* * c *
* s * c
* * * *	You collected all coals! (2, 3)
6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *	3 coals left. (5, 0)
'''