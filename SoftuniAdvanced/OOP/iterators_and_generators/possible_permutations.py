from itertools import permutations

def possible_permutations(elements):
    for per in permutations(elements):
        yield list(per)

[print(n) for n in possible_permutations([1, 2, 3])]