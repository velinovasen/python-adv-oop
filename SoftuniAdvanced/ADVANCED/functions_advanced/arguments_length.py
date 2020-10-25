def args_length(*args):
    count = 0
    for _ in args:
        count += 1
    return count



''''Arguments Length
Create a function called args_length that returns the number of arguments. Submit only the function in the judge system.
Examples
Test Code	Output
print(args_length(1, 32, 5))	3
print(args_length("john", "peter"))	2
print(args_length([1, 2, 3]))	1
'''