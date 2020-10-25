from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0


while males and females:
    curr_male = males[-1]
    curr_female = females[0]

    if curr_male <= 0:
        males.pop()

    elif curr_female <= 0:
        females.popleft()

    elif curr_female % 25 == 0:
        females.popleft()
        if females:
            females.popleft()

    elif curr_male % 25 == 0:
        males.pop()
        if males:
            males.pop()

    elif curr_male == curr_female:
        matches += 1
        males.pop()
        females.popleft()

    else:
        females.popleft()
        males[-1] -= 2

print(f'Matches: {matches}')
print(f"Males left: {', '.join([str(x) for x in reversed(males)])}" if males else "Males left: none")
print(f"Females left: {', '.join(str(x) for x in females)}" if females else "Females left: none")