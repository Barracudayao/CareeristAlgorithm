'''
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
'''


def reverse_num(num):
    if num == 0:
        return 0
    else:
        str_num = str(num)
        revere_number = int(str_num[::-1])
        return revere_number


print(reverse_num(123456789))