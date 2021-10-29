# swap two numbers a = 10 , b = 5  to a = 5, b = 10

# non function
#
# a = int(input("a is number: "))
# b = int(input("b is number: "))
#
# # method1
# # a, b = b, a
#
# # method2
# # c = a  # a = 10 then c = 10
# # a = b  # b = 5 then a = 5
# # b = c  #
#
# # method3
# a = a + b  # a =10 b = 5 then a = 15
# b = a - b  # a = 15 b = 5 then b = 10
# a = a - b  # a = 15 b = 10 then a = 5
#
#
#
# print(f'a is the number of: {a} ')
# print(f'b is the number of: {b} ')

# function

def swap_ab(a, b):
    # method1
    # a, b = b, a
    # print(f'a = {a}, b = {b}')

    #method2
    # temp = a  # a = 10 then c = 10
    # a = b  # b = 5 then a = 5
    # b = temp
    # print(f'a = {a}, b = {b}')

    #method3
    a = a + b  # a =10 b = 5 then a = 15
    b = a - b  # a = 15 b = 5 then b = 10
    a = a - b  # a = 15 b = 10 then a = 5
    print(f'a = {a}, b = {b}')


a = int(input("a is number: "))
b = int(input("b is number: "))

# print(f'a = {a}, b = {b}')
swap_ab(a, b)




