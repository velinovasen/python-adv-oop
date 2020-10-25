def palindrome(*args):
    idx = args[-1]
    word = args[0]
    mirrored = word[::-1]
    for x in range(len(word)):
        if word[x] != mirrored[x]:
            idx = 1
    if idx == 0:
        return f'{word} is a palindrome'
    else:
        return f'{word} is not a palindrome'

print(palindrome("peter", 0))
print(palindrome("abcba", 0))


'''Recursion Palindrome
Write a recursive function called palindrome which will receive a word and an index (always 0). Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome" if the word is not a palindrome using recursion. Submit only the function in the judge system.
Examples
Test Code	Output
print(palindrome("abcba", 0))	abcba is a palindrome
print(palindrome("peter", 0))	peter is not a palindrome
'''