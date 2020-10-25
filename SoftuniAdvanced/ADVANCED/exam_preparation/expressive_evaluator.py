from collections import deque

token = input().split()
numbers = deque()
for x in token:
    if x not in '*/+-':
        numbers.append(int(x))
    else:
        temp_res = numbers.popleft()
        while numbers:
            num = numbers.popleft()
            if x == '*':
                temp_res *= num
            if x == '/':
                temp_res //= num
            if x == '+':
                temp_res += num
            if x == '-':
                temp_res -= num
        numbers.append(temp_res)

print(*numbers)