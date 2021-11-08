'''
Reverse a Statement
Build an algorithm that will print the given statement in reverse.
Example: Initial string = Everything is hard before it is easy
Reversed string = easy is it before hard is Everything
'''

def reverse_string(string):
    words = string.split()
    words = list(reversed(words))
    print(" ".join(words))

string = "Everything is hard before it is easy"
print(string)













'''
Permutations
Write a solution that will print all permutations of a string.
A permutation is an act of changing the arrangement of characters.
Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}
'''
'''
Count Characters
Create a program that will count vowels and consonants in a string.
Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}
'''


