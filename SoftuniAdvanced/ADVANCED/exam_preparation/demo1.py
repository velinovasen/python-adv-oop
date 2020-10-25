from collections import deque

line = deque(input().split())

main_colors = ("red", "yellow", "blue")
secondary_colors = {"orange": ('red', 'yellow'), "purple": ('red', 'blue'), "green": ('yellow', 'blue')}
received_colors = []

while line:
    first_sub = line.popleft()
    if line:
        second_sub = line.pop()
        first_second = first_sub + second_sub
        second_first = second_sub + first_sub
        if first_second in main_colors or first_second in secondary_colors:
            received_colors.append(first_second)
        elif second_first in main_colors or second_first in secondary_colors:
            received_colors.append(second_first)
        else:
            line.insert(len(line) // 2, first_sub[:-1])
            line.insert(len(line) // 2, second_sub[:-1])

    else:
        if first_sub in main_colors or first_sub in secondary_colors:
            received_colors.append(first_sub)
        else:
            token = list(first_sub)
            try:
                token.pop()
            except IndexError:
                break
            line.append("".join(token))

for color in received_colors:
    if color in main_colors:
        pass
    elif color in secondary_colors:
        if secondary_colors[color][0] in received_colors and secondary_colors[color][1] in received_colors:
            pass
        else:
            received_colors.pop(received_colors.index(color))

print(received_colors)