import collections

#seive of eratosthenes




def primes(n):
    """returns a range object of primes up to and including n caluclated using a seive of Eratosthenes"""

    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtm = sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s) #the filter here with a None as the function argument removes all zero or false elements from the list) 


#create a set from the fuction return and use the 'in primes_set' to create a fast prime check.

def is_prime(x):

    if isinstance(x, int):
        return is_prime_number(x)
    elif isinstance(x, collections.Iterable):
        output = True
        for y in x:
           if is_prime_number(y) == False:
                return False
            
        return True 


def is_prime_number(x):
    """tests for primality using a seive up to root x"""

#    seive = primes(int(x**0.5))
    root_x = int(x**0.5)
   
    for p in default_seive:
        if p > root_x:
#            print(p)
            return True
        elif x % p == 0:
#            print(p)
            return False

    return


default_seive = list(primes(10000000))
"""use a seive up to 10 million as a default, as this calcs fast enough to be useful"""
