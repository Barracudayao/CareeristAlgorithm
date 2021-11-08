'''
Fibonacci sequence

The equation for the Fibonacci sequence:
φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.

The task is to display all the numbers from start to n of the Fibonacci sequence φn

Examples:
F1 = 1
F2 = F1 + 0 = 1
F3 = F2 + F1 = 1 + 1 = 2
F4 = F3 + F2 = 2 + 1 = 3
F5 = F4 + F3 = 3 + 2 = 5
F6 = F5 + F4 = 5 + 3 = 8

1, 1, 2, 3, 5, 8, 13,	21,	34,	55,	89,	144,	233,	377,	610 ...


'''

# method1
def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(9))

# method2
# Function for nth fibonacci
# number - Dynamic Programming
# Taking 1st two fibonacci numbers as 0 and 1


FibArray = [0, 1]


def fibonacci(n):
    # Check is n is less
    # than 0
    if n <= 0:
        print("Incorrect input")

    # Check is n is less
    # than len(FibArray)
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)

    FibArray.append(temp_fib)
    return temp_fib


# Driver Program
print(fibonacci(9))





# method3
def fibonacci(n):
    a = 0
    b = 1

    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is equal
    # to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


# Driver Program
print(fibonacci(9))




