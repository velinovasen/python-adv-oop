nums_dict = {}

line = input()

while line != 'Search':
    try:
        nums_dict.setdefault(line, int(input()))
    except ValueError:
        print(f'The variable number must be an integer')
    line = input()

line = input()
while line != 'Remove':
    try:
        print(f'{nums_dict[line]}')
    except:
        print(f'Number does not exist in dictionary')
    line = input()
line = input()

while line != 'End':
    try:
        del nums_dict[line]
    except:
        print(f'Number does not exist in dictionary')
    line = input()

print(nums_dict)