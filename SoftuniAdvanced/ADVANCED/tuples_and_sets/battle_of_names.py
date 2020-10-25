odd_nums = set()
even_nums = set()
counter = 0
for _ in range(int(input())):
    counter += 1
    name = input()
    name_sum = 0
    for x in name:
        name_sum += ord(x)
    name_sum //= counter
    if name_sum % 2 != 0:
        odd_nums.add(name_sum)
    else:
        even_nums.add(name_sum)

if sum(odd_nums) == sum(even_nums):
    new_set = list(odd_nums.union(even_nums))

elif sum(odd_nums) > sum(even_nums):
    new_set = list(odd_nums.difference(even_nums))

elif sum(odd_nums) < sum(even_nums):
    new_set = list(odd_nums.symmetric_difference(even_nums))

print(", ".join([str(x) for x in new_set]))

'''Battle of Names
You will receive a number N. On the next N lines, you will be receiving names. You must sum the ascii values of each letter in the name and integer devise the value (current index). Save the devised number to a set of either odd or even numbers, depending if it's an odd or even number. After that, sum the values of the odd and even numbers.
If the summed numbers are equal, print the union values, separated by ", ". 
If the odd sum is bigger than the even, print the different values, separated by ", ".
If the even sum is bigger than the odd, print the symmetric different values, separated by ", ".
NOTE: On every operation, the starting set should be the odd set
Examples
Input	Output
4
Pesho
Stefan
Stamat
Gosho	304, 128, 206, 511
6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan	733, 101
'''