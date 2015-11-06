import prime_numbers

def solution():

    primes = set(prime_numbers.default_seive)
    n = 3
    while n < 10000:

        if n not in primes:
            i = 1
            max_i = (n/2)**0.5
            while (n - 2*i**2) not in primes:
                if i >= max_i:
                    return n

                i = i + 1

        n = n+2

    return 'failed to find solution'
