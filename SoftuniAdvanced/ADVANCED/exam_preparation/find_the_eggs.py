from collections import deque


def find_strongest_eggs(*numbers):
    sequence = deque(numbers[0])
    sub_lists_count = numbers[1]
    all_sub_lists = []
    strongest_eggs = []
    [all_sub_lists.append([]) for _ in range(sub_lists_count)]
    counter = 0
    while sequence:
        all_sub_lists[counter].append(sequence.popleft())
        counter += 1
        if counter == len(all_sub_lists):
            counter = 0

    for sublist in all_sub_lists:
        idx = len(sublist) // 2
        middle_num = sublist[idx]
        sublist = deque(sublist)
        valid = True
        while idx + 1 < len(sublist):
            idx += 1
            right_num = sublist.pop()
            left_num = sublist.popleft()
            if middle_num > right_num > left_num:
                pass
            else:
                valid = False
        if valid:
            strongest_eggs.append(middle_num)


    return strongest_eggs

'''
def find_strongest_eggs(*args):
    seq, num = args[0], args[1]
    sub_lists = [seq[i::num] for i in range(num)]
    strong_eggs = []
    for l in sub_lists:
        middle = int(len(l) / 2)
        first_half = l[:middle]
        second_half = l[middle + 1:]

        if l[middle - 1] < l[middle] > l[middle + 1]:
            if [True for i, j in zip(first_half, second_half) if i < j]:
                strong_eggs.append(l[middle])
    return strong_eggs
'''


test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))
test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))
test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))