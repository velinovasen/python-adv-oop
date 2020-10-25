(elements_to_add, num_to_deque, num_to_look) = [int(x) for x in input().split()]
elements = [int(x) for x in input().split()]
[elements.pop(0) for _ in range(num_to_deque)]

if num_to_look in elements:
    print(f'True')
else:
    if len(elements) > 0:
        print(int(min(elements)))
    else:
        print(f'0')


        '''2. Basic Queue Operations
Play around with a queue. You will be given an integer N representing the number of elements to enqueue (add), an integer S representing the number of elements to dequeue (remove) from the queue and finally an integer X, an element that you should look for in the queue. If it is, print "True" on the console. If it's not print the smallest element currently present in the queue. If there are no elements in the sequence, print 0 on the console.
Examples
Input	Output	Comments
5 2 32
1 13 45 32 4	True 
	We have to enqueue 5 elements. Then we dequeue 2 of them. Finally, we have to check whether 32 is present in the queue. Since it is we print True.
4 1 666
666 69 13 420	13	
3 3 90
90 0 90	0	
'''