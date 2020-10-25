(first, second) = input().split(' ')
set_one = [] * int(first)
set_two = [] * int(second)
[set_one.append(int(input())) for x in range(int(first))]
[set_two.append(int(input())) for v in range(int(second))]
tokens = set(set_one).intersection(set(set_two))
for person in tokens:
    print(person)


    '''Sets of Elements
Write a program that prints a set of elements. On the first line you will receive two numbers - n and m, which represent the lengths of two separate sets. On the next n + m lines you will receive n numbers, which are the numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that appear in both of them and print them on separate lines (the order does not matter).
For example:
Set with length n = 4: {1, 3, 5, 7}
Set with length m = 3: {3, 4, 5}
Set that contains all the elements that repeat in both sets -> {3, 5}
Examples
Input	Output
4 3
1
3
5
7
3
4
5	3
5
2 2
1
3
1
5	1
'''