import itertools
import prime_numbers

def candidates(n):
    """create a list of n digit trucatable prime candidates. A number is a candiate if it start and ends with a 3 or 7 and contains only the digits 1,3,7 and 9"""

    if n == 2:
        return {23,37,53,73}
    else:
        return {int(a+b+c) for a in {'3','7'} for b in {''.join(x) for x in list(itertools.product('1379', repeat = n - 2))} for c in {'3','7'}}

def t_set(p):
    """returns the set of numbers obtained by removing digits from p either left to right or right to left"""
    output_set = {p}
    for i in range(1,len(str(p))):
        output_set.add(int(str(p)[i:]))
        output_set.add(int(str(p)[:i]))
        i = i + 1

    return output_set

def solution():


    primes = set(prime_numbers.primes(10000000))
    count = 0
    running_total = 0
    i = 2
    while (count < 11 and i < 12):
        
        ndigit_candidates = candidates(i)
        for x in ndigit_candidates:
            if prime_numbers.is_prime(t_set(x)):
                print(x)
                count = count + 1
                running_total = running_total + x
        i = i + 1

    return running_total

