tokens = input().split()
nums = filter(lambda x: x.isdigit(), tokens)
nums = sorted(filter(lambda x: x > len(tokens), map(int, nums)))
print(*nums)