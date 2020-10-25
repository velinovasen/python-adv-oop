token = input()
my_dict = {}
for n in token:
    if n in my_dict:
        my_dict[n] += 1
    else:
        my_dict[n] = 1
tokens = sorted(my_dict.items(), key=lambda x: x[0])
for z in tokens:
    print(f'{z[0]}: {z[1]} time/s')

    '''Count Symbols
Write a program that reads some text from the console and counts the occurrences of each character in it. Print the results in alphabetical (lexicographical) order. 
Examples
Input	Output
SoftUni rocks	 : 1 time/s
S: 1 time/s
U: 1 time/s
c: 1 time/s
f: 1 time/s
i: 1 time/s
k: 1 time/s
n: 1 time/s
o: 2 time/s
r: 1 time/s
s: 1 time/s
t: 1 time/s
'''