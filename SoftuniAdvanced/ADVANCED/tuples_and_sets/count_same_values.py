tokens = tuple(map(float, input().split()))
my_dict = {}
for x in tokens:
    if x not in my_dict:
        my_dict[x] = 1
    else:
        my_dict[x] += 1

[print(f'{float(k)} - {v} times') for k, v in my_dict.items()]


'''Count Same Values
Write a program that counts in a given list of float values and prints the number of occurrences of each value. 
Examples
Input	Output
-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
	-2.5 - 3 times
4.0 - 2 times
3.0 - 4 times
-5.5 - 1 times
2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3
	2.0 - 3 times
4.0 - 6 times
5.0 - 4 times
3.0 - 7 times
'''