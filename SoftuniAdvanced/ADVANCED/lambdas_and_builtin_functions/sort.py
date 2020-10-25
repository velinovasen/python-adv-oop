
negative_nums = filter(lambda x: x < 0, map(int, input().split()))
print(abs(sum(negative_nums)))