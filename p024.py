import math

def solution(i_digits = 10, position = 1000000):
    """calculate the lexicograical position of an word of k consecutive digigs starting at 0"""

    stack = []
    i = 0
    while i < i_digits:
        stack.append(i)
        i = i + 1

    digit = i_digits
    while digit > 0:
        digit_to_grab =  (position - 1) // math.factorial(digit - 1)
        x = stack.pop(digit_to_grab + i_digits - digit)
        stack.insert(i_digits - digit, x)
        position = ((position - 1) % math.factorial(digit - 1)) + 1
        digit = digit - 1

    return stack
