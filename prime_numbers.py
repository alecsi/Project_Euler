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

    if x < max_precalc:
        return x in primes_set
    else:
        root_x = int(x**0.5)

        for p in default_seive:
            if p > root_x:
                return True
            elif x % p == 0:
                return False

    return 'error: prime too big' 

max_precalc = 10**7
primes_iter = primes(max_precalc)
default_seive = sorted(list(primes_iter))
primes_set = set(default_seive)
"""use a seive up to 10 million as a default, as this calcs fast enough to be useful"""

def number_of_distinct_prime_factors(n, prime_position = 0, set_of_factors = None):

    if set_of_factors == None:
        set_of_factors = set()

    if n == 1:
        return len(set_of_factors)
    else:
        p = default_seive[prime_position]
        if p > n ** 0.5 + 0.1:
            set_of_factors.add(n)
            return len(set_of_factors)
        elif n % p == 0:
            set_of_factors.add(p)
            return number_of_distinct_prime_factors(n//p, prime_position, set_of_factors)
        else:
            return number_of_distinct_prime_factors(n, prime_position+1,set_of_factors)


    

def prime_sum(n):
    """returns the sum of the first n primes"""

    return sum(default_seive[:n])

