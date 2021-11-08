'''
Two Lowest Elements
When given a list of elements, find the two lowest elements.
They can be equal to each other or different.
Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
'''

#method1     O(logn)


def lowest_elements(list):
    list1 = sorted(list)
    min1, min2 = list1[0:2]
    return min1, min2


list = [198, 3, 4, 9, 10, 9, 2]
print(lowest_elements(list))
