multiplier = int(input())
nums = map(lambda x: x * multiplier, map(lambda x: int(x), input().split()))
print(*nums)