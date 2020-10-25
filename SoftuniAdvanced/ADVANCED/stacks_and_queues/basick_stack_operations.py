(num_elements, elements_to_pop, look_for_element) = [int(x) for x in input().split()]
elements = [int(x) for x in input().split()]

for _ in range(elements_to_pop):
    elements.pop()

if look_for_element in elements:
    print(f'True')
else:
    if len(elements) == 0:
        print('0')
    else:
        print(int(min(elements)))


        '''1. Basic Stack Operations
Play around with a stack. You will be given an integer N representing the number of elements to push into the stack, an integer S representing the number of elements to pop from the stack and finally an integer X, an element that you should look for in the stack. If it's found, print "True" on the console. If it isn't, print the smallest element currently present in the stak.
Input
On the first line you will be given N, S and X, separated by a single space
On the next line you will be given N number of integers
Output
On a single line print either "True" if X is present in the stack, otherwise print the smallest element in the stack. If the stack is empty, print "0".
Examples
Input	Output	Comments
5 2 13
1 13 45 32 4	True	We have to push 5 elements. Then we pop 2 of them. Finally, we have to check whether 13 is present in the stack. Since it is we print True.
4 1 666
420 69 13 666	13	
'''