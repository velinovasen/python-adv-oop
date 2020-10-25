def even_odd(*args):
    x = 0 if args[-1] == 'even' else 1
    return [y for y in args[:-1] if y % 2 == x]

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
print(even_odd(1, 2, 3, 4, 5, 6, "even"))


''''Even or Odd
Create a function called even_odd that can receive different amount of numbers and a command at the end. The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. Submit only the function in the judge system.
Examples
Test Code	Output
print(even_odd(1, 2, 3, 4, 5, 6, "even"))	[2, 4, 6]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))	[1, 3, 5, 7, 9]
'''