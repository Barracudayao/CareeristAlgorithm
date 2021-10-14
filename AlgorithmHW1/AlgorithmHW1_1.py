# Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

import time

#build in sum

def sumNum(n):
    result = sum(range(1, n+1))
    return result

print(sumNum(100))

# for loop

def sumNum1(n):
    theNum = 0
    for i in range(1, n+1):
        theNum = theNum + i
    return theNum
print(sumNum1(100))


#function
def sumNum2(n):
    theSum = n*(n+1)/2
    return theSum
print(sumNum2(100))

# def sumNum2(n):
#     start = time.time()
#     theNum = 0
#     for i in range(1, n+1):
#         theNum = theNum + i
#     end = time.time()
#     return theNum, end - start
#
# print("Sum is %d required %10.7f seconds" % sumNum2(100000))








