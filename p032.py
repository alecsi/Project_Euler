import itertools

one_to_nine = {1,2,3,4,5,6,7,8,9}

def tuple_to_number(input):

    output = 0
    for i in range(len(input)):
        output = output + input[i] * (10**(len(input)-i-1))

    return output


def digit_set(n):

    n = int(n)
    digits_set = set()
    while n > 0:
        digits_set.add(n % 10) 
        n = (n - (n % 10)) // 10

    return digits_set


def solution():

    set_of_products = set()
    for k in (set(itertools.permutations(one_to_nine, 2)) | set(itertools.permutations(one_to_nine, 1))):

        d_set = one_to_nine.difference(set(k))

        set_of_multiplicands = (set(itertools.permutations(d_set,3)) | set(itertools.permutations(d_set,4)))
        for m in set_of_multiplicands:
            p = tuple_to_number(m)*tuple_to_number(k)
            if (p < 10000) and (digit_set(p) == d_set.difference(set(m))):
                print(tuple_to_number(k), tuple_to_number(m), p)
                set_of_products.add(p)

    return  sum(set_of_products)





