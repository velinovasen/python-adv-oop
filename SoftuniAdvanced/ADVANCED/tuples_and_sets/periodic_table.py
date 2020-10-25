times_input = int(input())
unique_elements = []
for x in range(times_input):
    tokens = input().split()
    for y in range(len(tokens)):
        if tokens[y] in unique_elements:
            pass
        else:
            unique_elements.append(tokens[y])
unique_elements = set(unique_elements)
for y in unique_elements:
    print(f'{y}')


'''Periodic Table
Write a program that keeps all the unique chemical elements. On the first line you will be given a number n - the count of input lines that you are going to receive. On the next n lines, you will be receiving chemical compounds, separated by a single space. Your task is to print all the unique ones on a separate lines (order does not matter):
Examples
Input	Output
4
Ce O
Mo O Ce
Ee
Mo	Ce
Ee
Mo
O
3
Ge Ch O Ne
Nb Mo Tc
O Ne	Ch
Ge
Mo
Nb
Ne
O
Tc
'''