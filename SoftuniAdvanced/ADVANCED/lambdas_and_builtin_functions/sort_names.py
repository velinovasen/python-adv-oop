names = input().split()
names.sort(key=lambda x: x, reverse=True)
print(" ".join(names))

