names = map(str, input().split())
names = filter(lambda x: x[0].isupper() and x[1:].islower(), names)
print(sum(map(lambda x: len(x), names)))
