import math
import itertools
import base10
import collections

def factorial_sum(iterable):

    return sum(tuple(math.factorial(n) for n in iterable))


def  is_ascending(ordered_iterable):

    for i in range(1, len(ordered_iterable)):
        if ordered_iterable[i-1] > ordered_iterable[i]:
            return False

    return True


def check_candidates(candidates):

     return [factorial_sum(x) for x in candidates if base10.digit_counter(factorial_sum(x)) == collections.Counter(x)]

def solution_3():

    candidates = [sorted(n) for n in itertools.product(range(10), range(10), range(10)) if 10**(len(n)-1) <= factorial_sum(n) < 10**(len(n)) and is_ascending(n)]
#    return [factorial_sum(x) for x in candidates if base10.digit_set(factorial_sum(x)) == set(x)]
    return check_candidates(candidates)

def solution_4():

    candidates = [sorted(n) for n in itertools.product(range(10), range(10), range(10), range(10)) if 10**(len(n)-1) <= factorial_sum(n) < 10**(len(n)) and is_ascending(n)]
    return check_candidates(candidates)

def solution_5():

    candidates = [sorted(n) for n in itertools.product(range(10), range(10), range(10), range(10), range(10)) if 10**(len(n)-1) <= factorial_sum(n) < 10**(len(n)) and is_ascending(n)]
    return check_candidates(candidates)

def solution_6():

    candidates = [sorted(n) for n in itertools.product(range(10), range(10), range(10), range(10), range(10), range(10)) if 10**(len(n)-1) <= factorial_sum(n) < 10**(len(n)) and is_ascending(n)]
    return check_candidates(candidates)

def solution_7():

    candidates = [sorted(n) for n in itertools.product(range(10), range(10), range(10), range(10), range(10), range(10), range(10)) if 10**(len(n)-1) <= factorial_sum(n) < 10**(len(n)) and is_ascending(n)]
    return check_candidates(candidates)

def solution_8():

    candidates = [sorted(n) for n in itertools.product(range(10), range(10), range(10), range(10), range(10), range(10), range(10), range(10)) if 10**(len(n)-1) <= factorial_sum(n) < 10**(len(n)) and is_ascending(n)]
    return check_candidates(candidates)


def solution_9():

    candidates = [sorted(n) for n in itertools.product(range(10), range(10), range(10), range(10), range(10), range(10), range(10), range(10), range(10)) if 10**(len(n)-1) <= factorial_sum(n) < 10**(len(n)) and is_ascending(n)]
    return check_candidates(candidates)

