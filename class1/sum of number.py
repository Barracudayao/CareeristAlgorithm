'''
give a random number, then sum of all of each number plus together; For example: 345 => 3+4+5 = 12
'''

#
# def sum_numbers(num):
#     result = 0
#     while num != 0:
#         result = result + (num % 10)
#         num = num // 10
#         print(result)
#
#
# num = int(input("num is : "))
# sum_numbers(num)

# method2
def sum_numbers1(num):
    result = 0
    for i in str(num):
        result = result + int(i)
    print(result)

num = int(input("num is : "))
sum_numbers1(num)
