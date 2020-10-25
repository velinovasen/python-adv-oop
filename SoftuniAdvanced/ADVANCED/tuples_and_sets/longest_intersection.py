times = int(input())
longest_intersection = set()
for x in range(times):
    tokens = input().split('-')
    first_range = [int(x) for x in tokens[0].split(',')]
    second_range = [int(x) for x in tokens[1].split(',')]
    first_set = set([x for x in range(first_range[0], first_range[1] + 1)])
    second_set = set([x for x in range(second_range[0], second_range[1] + 1)])
    intersection = first_set & second_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')