import base10

def solution():

    n = 2

    while n < 7:
        for i in range(10**n, (10**(n+1))//6):
            if base10.digit_multiset(i) == base10.digit_multiset(2*i)==base10.digit_multiset(3*i)==base10.digit_multiset(4*i)==base10.digit_multiset(5*i)==base10.digit_multiset(6*i):
                return i,2*i,3*i,4*i,5*i,6*i

        n = n + 1

    return 'fail'
