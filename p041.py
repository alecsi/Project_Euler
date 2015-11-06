import prime_numbers
import pandigital

def solution(n=9):
    """find the biggest pandigital prime of n digits or less"""

    while n>1:
        pds = pandigital.pandigital_list(n)[::-1]
        for x in pds:
            if prime_numbers.is_prime(x):
                return x

        n = n - 1

    return 'none'
