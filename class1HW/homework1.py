# Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits
# in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# method1 use formula (1+n)*n/2

from random import randint


def sum_of_numbers(n):
    result = (1 + n) * n/2  # time complexity is o(1)
    return result


n = randint(1, 101)
print(n)
print(f'sum of number is : {sum_of_numbers(n)}')


#  method2 use for loop

def sum_of_numbers1(n):
    if n <= 0:
        print("not a valid number")

    result = 0
    for i in range(1, n+1):  # time complexity is o(n)
        result = result + i
    return result


n = randint(1, 101)
print(n)
print(f'sum of number1 is : {sum_of_numbers1(n)}')

