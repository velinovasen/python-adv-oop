nums = list(map(lambda x: round(x), map(float, input().split())))
print(min(nums))
print(max(nums))
nums = map(lambda x: x * 3, nums)
nums = sorted(set(nums))
print(*nums)