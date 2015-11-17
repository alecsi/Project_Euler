import collections
import itertools

def digit_set(n):
    """good if you want the set, ie repeated elements are removed"""

    return set(map(int,(str(n)))) 

def digit_list(n):
    """returns a list of the digits of n"""

    return list(map(int,(str(n))))

def digit_sum(n): return sum(map(int,(str(n))))



def digit_multiset(n):
    """returns the multiset dict of n, good if you care about repeated digits"""

    return collections.Counter(map(int,(str(n))))


def is_palindrome(n):

    return (str(n) == str(n)[::-1])

def reverse(n):
    
    return int(str(n)[::-1])


def digit_counter(n):
    """good if you want to keep repeated elements but don't care about order"""

    n = int(n)
    d_counter = collections.Counter()
    while n > 0:
        d_counter[(n % 10)] += 1
        n = (n - (n % 10)) // 10

    return d_counter

def perms(n):
    """returns the set of permutations of n"""
    def f(x):
        return int(''.join(x))

    return map(f,itertools.permutations(str(n)))

    
def concat(n1, n2):

    return int(str(n1) + str(n2))
