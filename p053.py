import math

def nCr(n,r):
    f = math.factorial
    return f(n)//f(r)//f(n-r)

def solution(max_value = 10**6):

    return sum([1 for n in range(1,101) for r in range(1, n+1) if (nCr(n,r)>max_value)])

