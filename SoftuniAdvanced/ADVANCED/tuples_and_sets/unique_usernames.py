times_input = int(input())
unique_names = []
for _ in range(times_input):
    name = input()
    if name in unique_names:
        pass
    else:
        unique_names.append(name)
for person in set(unique_names):
    print(person)

    '''Unique Usernames
Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones. On the first line you will be given an integer N. On the next N lines, you will receive one username per line. Print the collection on the console (the order does not matter):
Examples
Input	Output
6
George
George
George
Peter
George
NiceGuy1234	George
Peter
NiceGuy1234
'''