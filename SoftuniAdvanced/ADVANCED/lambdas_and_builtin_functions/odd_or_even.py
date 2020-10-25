command = input()
nums = list(map(int, input().split()))
if command == 'Even':
    even_nums = sum(list(filter(lambda x: x % 2 == 0, nums)))
    print(f'{even_nums * len(nums)}')

elif command == 'Odd':
    odd_nums = sum(list(filter(lambda x: x % 2 != 0, nums)))
    print(f'{odd_nums * len(nums)}')