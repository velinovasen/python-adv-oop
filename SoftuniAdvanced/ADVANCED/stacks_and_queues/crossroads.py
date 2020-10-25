from collections import deque
green_light_time = int(input())
free_window = int(input())
total_time = green_light_time + free_window
crossroad = deque([])
car_inside = deque([])
cars_passed = 0
while True:
    command = input()
    if command == 'END':
        break

    elif command == 'green':
        while green_light_time > 0:
            car_inside = crossroad.popleft()


    else:
        crossroad.append(command)