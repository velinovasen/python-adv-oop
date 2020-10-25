def build_matrix():
    matrix = []
    rows, cols = [int(x) for x in input().split(' ')]
    for x in range(rows):
        matrix.append([x for x in input().split(' ')])
    return matrix


def shuffle_matrix():
    matrix = build_matrix()
    while True:
        tokens = input().split(' ')
        if tokens[0] == 'END':
            break
        if tokens[0] == 'swap' and len(tokens) == 5:
            r1, c1, r2, c2 = int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[4])
            try:
                matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
                for x in range(len(matrix)):
                    print(" ".join([str(x) for x in matrix[x]]))
            except IndexError:
                print(f'Invalid input!')


        else:
            print(f'Invalid input!')

shuffle_matrix()

'''⦁	Matrix Shuffling
Write a program which reads a string matrix from the console and performs certain operations with its elements. User input is provided in a similar way like in the problems above - first you read the dimensions and then the data. 
Your program should then receive commands in format: "swap row1 col1 row2c col2" where row1, row2, col1, col2 are coordinates in the matrix. For a command to be valid, it should start with the "swap" keyword along with four valid coordinates (no more, no less). You should swap the values at the given coordinates (cell [row1, col1] with cell [row2, col2]) and print the matrix at each step (thus you'll be able to check if the operation was performed correctly). 
If the command is not valid (doesn't contain the keyword "swap", has fewer or more coordinates entered or the given coordinates do not exist), print "Invalid input!" and move on to the next command. Your program should finish when the string "END" is entered.

Examples
Input	Output
2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END	5 2 3
4 1 6
Invalid input!
5 4 3
2 1 6
1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END	Invalid input!
World Hello
Hello World
'''