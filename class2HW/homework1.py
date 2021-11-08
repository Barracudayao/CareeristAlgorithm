'''
Even First
Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
You are required to solve it without allocating additional storage (operate with the input array).
Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
'''

arry = [7, 3, 5, 6, 4, 10, 3, 2]
arry1 = []
arry2 = []


for i in arry:
    if i % 2 == 0: # it is an even number:
        arry1.append(i)
    else:
        arry2.append(i)

result = arry1 + arry2

print(result)







