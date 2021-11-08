'''
Below The Arithmetical Mean
When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
The arithmetical mean is the sum of all elements divided by the number of elements.
Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
'''


# list = [1, 3, 5, 6, 4, 10, 2, 3]
#
# sum_number = sum(list)
# length = len(list)
#
# arithmetical_mean = sum_number / length
#
# new_list = []
#
# for num in list:
#     if num < arithmetical_mean:
#         new_list.append(num)
#
# print(new_list)

def list_below_arithmetical_mean(list):  #o(n)
    sum_list = sum(list)
    length_list = len(list)
    arithmetical_mean = sum_list / length_list
    new_list = []
    for num in list:
        if num < arithmetical_mean:
            new_list.append(num)
    return new_list

list = [1, 3, 5, 6, 4, 10, 2, 3]
print(list_below_arithmetical_mean(list))

