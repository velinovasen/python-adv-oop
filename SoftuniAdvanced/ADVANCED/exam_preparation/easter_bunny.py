def build_matrix():
    size = int(input())
    matrix = []
    [matrix.append(input().split()) for _ in range(size)]
    return matrix


def check_start_pos(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'B':
                return [row, col]


def find_direction(matrix, bunny_start):
    directions = {
        "up": [-1, 0],
        "right": [0, +1],
        "down": [+1, 0],
        "left": [-1, 0]
    }
    score = {
        "up": 0,
        "right": 0,
        "down": 0,
        "left": 0
    }
    eggs_collected = {
        "up": [],
        "right": [],
        "down": [],
        "left": []
    }

    for key in directions:
        row, col = bunny_start[0], bunny_start[1]
        while True:
            next_pos = row + directions[key][0], col + directions[key][1]
            while 0 <= next_pos[0] < len(matrix) and 0 <= next_pos[1] < len(matrix):
                row, col = next_pos[0], next_pos[1]
                if matrix[next_pos[0]][next_pos[1]] != "X":
                    score[key] += int(matrix[row][col])
                    eggs_collected[key].append([row, col])
                else:
                    break

    return directions, score, eggs_collected


def action():
    matrix = build_matrix()
    directions, score, eggs_collected = find_direction(matrix, check_start_pos(matrix))
    best_dir = max([(value, key) for key, value in score.items()])
    print(best_dir[1])
    for x in directions[best_dir[1]]:
        print(x)
    print(best_dir[0])


action()