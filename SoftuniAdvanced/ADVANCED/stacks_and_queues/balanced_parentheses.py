parentheses = input()
tokens = []
is_balanced = True
dict = {'{' : '}', '[' : ']', '(' : ')'}
for x in parentheses:
    if x in '[{(':
        tokens.append(x)
    else:
        if tokens:
            current = tokens[-1]
            if dict[current] == x:
                tokens.pop()
            else:
                is_balanced = False
                break
        else:
            is_balanced = False
            break
if is_balanced:
    print(f'YES')
else:
    print(f'NO')


    '''7. Balanced Parentheses
Given a sequence consisting of parentheses, determine whether the expression is balanced. A sequence of parentheses is balanced if every open parenthesis can be paired uniquely with a closed parenthesis that occurs after the former. Also, the interval between them must be balanced. You will be given three types of parentheses: (, {, and [.
{[()]} - This is a balanced parenthesis.
{[(])} - This is not a balanced parenthesis.
Input
Each input consists of a single line, the sequence of parentheses.
Output 
For each test case, print on a new line "YES" if the parentheses are balanced. 
Otherwise, print "NO". Do not print the quotes.
Constraints
1 ≤ lens ≤ 1000, where lens is the length of the sequence.
Each character of the sequence will be one of {, }, (, ), [, ].
Examples
Input	Output
{[()]}	YES
{[(])}	NO
{{[[(())]]}}	YES
'''