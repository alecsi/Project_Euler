import collections

def is_pandigital(x):
    """checks if a number, or a set of iterable group of numbers, is pandigital"""

    if isinstance(x, int):
        return is_pandigital_number(x)
    elif isinstance(x, collections.Iterable):
        concat = ''
        for y in x:
            concat = concat + str(y)
            
        return is_pandigital_number(int(concat))

def is_pandigital_number(x):

    x = sorted(list(str(x)))
    return x == ['1','2','3','4','5','6','7','8','9'][:len(x)] 
    

