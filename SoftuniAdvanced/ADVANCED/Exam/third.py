from collections import deque


def list_manipulator(*args):
    line = deque(args)
    nums = line.popleft()
    second_par = line.popleft()
    third_par = line.popleft()
    rest_num = []
    while line:
        rest_num.append(line.popleft())
    if second_par == 'add':
        if third_par == 'beginning':
            return rest_num + nums
        elif third_par == 'end':
            return nums + rest_num

    elif second_par == 'remove':
        if third_par == 'beginning':
            if rest_num:
                idx = int(rest_num.pop())
                return nums[idx:]
            return nums[1:]
        elif third_par == 'end':
            if rest_num:
                idx = int(rest_num.pop())
                return nums[:-idx]
            return nums[:-1]

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))