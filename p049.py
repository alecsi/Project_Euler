import prime_numbers
import base10

def solution():

    primes =  [p for p in prime_numbers.primes(10000) if p > 1000]

    for p in primes:
        p_set = set(base10.perms(p)) & set(primes)
        p_list = sorted(list(x for x in p_set if x > p))

        for q in p_list:
            if (2*q-p) in p_list:
                print(p,q,2*q-p)

    return 'done'
