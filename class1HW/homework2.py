# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.

from random import randint

# method1, use if , elif, else

from random import randint


def max_num(a, b, c):
    if a > b and a > c:  # time complexity is o(1)
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)


a = randint(1, 1000)
b = randint(1, 1000)
c = randint(1, 1000)

print(f"a, b, c : {a}, {b}, {c}")
max_num(a, b, c)


# method2 build_in function max

def max_number(a, b, c):
    result = max(a, b, c)  # time complexity is o(n)
    return result


a = randint(1, 1000)
b = randint(1, 1000)
c = randint(1, 1000)


print(f"a, b, c : {a}, {b}, {c}")
print(max_number(a, b, c))

