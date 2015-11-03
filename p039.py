import math

def is_square(n):
    if int(math.sqrt(n)+0.5)**2 == n:
        return True
    else:
        return False


def set_of_pythagorean_triples(max_perim = 1000):

    triples = set()

    for a in range(2,int(max_perim/3.4)):
        for b in range(a, max_perim-a):
            c_squared = a**2 + b**2
            if is_square(c_squared):
                c = int(math.sqrt(c_squared) + 0.5)
                if (a+b+c) <= max_perim:
                    triples.add((a,b,c))

    return triples 

def solution(max_perim = 1000):

    triples = set_of_pythagorean_triples(max_perim)
    list_of_perims = [sum(x) for x in triples]
    
    return max(set(list_of_perims), key=list_of_perims.count)#an over clever way to find the most common element in a list



