phonebook = {}

while True:
    token = input()
    if token.isdigit():
        for _ in range(int(token)):
            name_search = input()
            if name_search in phonebook:
                print(f'{name_search} -> {phonebook[name_search]}')
            else:
                print(f'Contact {name_search} does not exist.')
        break

    tokens = token.split('-')
    phonebook[tokens[0]] = tokens[1]


'''Phonebook
Write a program that receives info from the console about people and their phone numbers.
You are free to choose the way the data is entered; each entry should have a name and a number (both strings). If you receive a name that already exists in the phonebook, update its number.
After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of a contact by name and print her details in format "{name} -> {number}". In case the contact isn't found, print "Contact {name} does not exist."
Examples
Input	Output
Adam-0888080808
2
Mery
Adam	Contact Mery does not exist.
Adam -> 0888080808
Adam-+359888001122
Ralf-666
George-5559393
Silvester-02/987665544
4
Silvester
silvester
Rolf
Ralf	Silvester -> 02/987665544
Contact silvester does not exist.
Contact Rolf does not exist.
Ralf -> 666
'''