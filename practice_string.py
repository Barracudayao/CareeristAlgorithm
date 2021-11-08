'''
Split in Half
Given a string. Split it into two equal parts. Swap these parts and return the result.
If the string has odd characters, the first part should be one character greater than the second part.
Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.
'''


def split_half_str(s):

    first_half = s[:len(s) // 2]
    second_half = s[len(s)//2 if len(s) % 2 == 0 else ((len(s)//2)+1):]
    first_half, second_half = second_half, first_half
    result = second_half + first_half
    print(sorted(result))

split_half_str('ccccdddaaaaaabbbb')









'''
Unique Characters in String
Given a string, determine if it consists of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False.
Hint: https://www.w3schools.com/python/python_sets.asp
'''

