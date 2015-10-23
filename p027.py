import prime_numbers
import itertools

primes = set(prime_numbers.primes(2100000))

def number_of_consecutive_primes(a,b):
    """returns the number of consecutive primes produced by the polynomial n^2 + an + b"""

    n = 0
    while (n**2 + a * n + b) in primes:
        n = n + 1

    return n


def solution(m = 1000):
    """returns the maximum number of consecutive primes returned by a quadratic polynomial with x and number coefficents of modulus less than m"""

    n = 0
    for (a,b) in itertools.product (range(-m + 1, m), primes.intersection(range(2,m))):
        x = number_of_consecutive_primes(a,b)
        if x > n:
            n = x
            max_a = a
            max_b = b


    print(max_a, max_b)
    return max_a * max_b


def test_number_of_consecutive_primes():

    print("n^2 + n + 41:", number_of_consecutive_primes(1,41) == 40)
    print("n^2 - 79n + 1601:", number_of_consecutive_primes(-79,1601) == 80)

