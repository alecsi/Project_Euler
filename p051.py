import prime_numbers
from collections import Counter
import base10
import operator
import itertools

def number_of_shared_digits(n1, n2):
    n1s = str(n1)
    n2s = str(n2)

    running_total = 0
    for i in range(0, len(n1s)):
        if n1s[i] == n2s[i]:
            running_total = running_total + 1

    return running_total

def replace_n_common(x, n):
    """ replaces numbers with strings where n common digits are replaced by xx"""

    return str(x).replace(most_common(str(x)),'x')

def equiv(p1,p2):
    """checks if two numbers differ only by three of their digits and that those digits are the same"""

    p1lst = base10.digit_list(p1)
    p2lst = base10.digit_list(p2)

    listdiff = list(map(operator.add,p1lst,map(operator.neg,p2lst)))

    if listdiff.count(0) == len(listdiff) - 3 and len(set(listdiff)) == 2:
        return True
    else:
        return False

def familly_count(p,i):
    """returns the max number of primes in the same familly, by replacing the i similar digits"""

    

 
def equiv_count(p, lst):

    equiv_count = sum([1 for l in lst if equiv(p,l)])




def most_common(lst):
    return max(set(lst), key=lst.count)

def most_common_count(lst):
    return lst.count(max(set(lst), key=lst.count))

def solution():
    """by casting out the nines it's easy to see that the solution must require 3 or a multiple of 3 numbers to be replaced. Will focus on replacing just 3 as I think that will give a solution"""

    primes_set = prime_numbers.primes_set
    i = 6
    idigitprimes = {p for p in primes_set if 10**(i-1) < p < 10**i}
    candidates = {p for p in idigitprimes if most_common_count(str(p)) >= 3}
    d = {key:set() for key in itertools.combinations(range(0, i),3)}

    for p in candidates:
        for x in d:
            if str(p)[x[0]] == str(p)[x[1]] == str(p)[x[2]]:
                d[x].add(p)
    
    d_new = {}

    for key in d:
        d_new[key] =[] 
        for p in d[key]:
            d_new[key].append(int(str(p)[:key[0]] + str(p)[key[0]+1:key[1]]+str(p)[key[1]+1:key[2]]+str(p)[key[2]+1:]))
    


#    seed_candidates = {p for p in candidates if most_common_count(str(p)) == 3}

#    good_seeds = {p for p in seed_candidates if equiv_count(p, candidates) == 7}

    return d_new
