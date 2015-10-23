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
