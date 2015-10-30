import prime_numbers

def solution(n =  1000000):
    """returns the number of circular primes below n"""

    primes = set(prime_numbers.primes(n))
    output_set = set()
    for p in primes:
        if circular_numbers(p).issubset(primes):
            output_set.add(p)

    return len(output_set)




def test():
    print(solution(100) == 13)
    
    return




def circular_numbers(n):
    """returns the set of circular numbers of a number, eg 1091 would return 1091, 911, 9110, 1109"""

    output_set = set()
    i = 0
    while i <  len(str(n))+1:
        output_set.add(int(n))
        n = str(n)[1:] + str(n)[:1]
        i = i + 1 

    return output_set
