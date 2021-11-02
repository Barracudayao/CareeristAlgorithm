# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


def count_odd_even_numbers(num):
    odd_num = []
    even_num = []
    st = str(num)
    stl = list(st)
    for i in stl:
        if int(i) % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)
    print(f'There are {len(odd_num)}, {odd_num} odd numbers and {len(even_num)}, {even_num} even numbers')

num = int(input("number is : "))
count_odd_even_numbers(num)













#     odd_num = []
#     even_num = []
#     st = str(num)
#     stl = list(st)
#     for int(i) in stl:
#         if i % 2 == 0:
#             even_num.append(i)
#             # print(odd_num)
#         else:
#             odd_num.append(i)
#             # print(even_num)
#
# print(f'There are {len(odd_num)} odd numbers and {len(even_num)} even numbers')
# count_odd_even_numbers(12345)


#   odd_num = []
#     even_num = []
#     st = str(num)
#     stl = list(st)
#     for i in stl:
#         if int(i) % 2 == 0:
#             even_num.append(i)
#             # print(odd_num)
#         else:
#             odd_num.append(i)
#             # print(even_num)
#     print(f'There are {len(odd_num)} odd numbers and {len(even_num)} even numbers')
# count_odd_even_numbers(12345)





# print(type(stl))
# print(stl)
#




#     # Converting integer to string
#     st = str(n)
#     even_count = 0
#     odd_count = 0
#
#     # Looping till length of string
#     for i in range(len(st)):
#         if ((int(st[i]) % 2) == 0):
#             # digit is even so increment even count
#             even_count += 1
#             print(even_count)
#         else:
#             odd_count += 1
#             print(odd_count)
#
# count_odd_even_numbers(12345)
#     odd = 0
#     even = 0
#
#     while (num != 0):
#         rem = num % 10
#         if (rem % 2 == 1):
#             odd += 1
#             print(odd)
#         else:
#             even += 1
#             print(even)
#         num //= 10
#
#     print("even digits = ", even)
#     print("odd digits = ", odd)
#
#
#
# count_odd_even_numbers(4455667788)


