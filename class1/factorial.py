# Factorial of a non-negative integer, is multiplication of all
# integers smaller than or equal to n.
# For example factorial of 6 is 6*5*4*3*2*1


# method1

#  o(n)
# import math
#
#
# def factorial(number):
#     return math.factorial(number)
#
# number = int(input('Input your number: '))
# print(factorial(number))

# method2

def factorial1(n):
    result = 1
    if n > 0:
        for i in range(1, n + 1):
            result = result * i
        return(result)

n = int(input('Input your number: '))

print(factorial1(n))


