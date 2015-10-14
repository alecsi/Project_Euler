import math

def solution(n = 1000):
    """returns i where the ith fibonacci number is the first one to contain n digits"""

    return math.ceil((math.log10(5 ** 0.5) + n - 1) / math.log10((1 + 5 ** 0.5) / 2 ))
