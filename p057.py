import prime_numbers

def solution(target_ratio = 0.1):

    set_of_diagonal_primes = set()
    set_of_diagonal_numbers = {1}

    n = 0
    while n < 10**5:

        n += 1
        new_diagonal_numbers = {(2 * n + 1)**2, (2 * n + 1)**2 - 2*n, (2 * n + 1)**2 - 4*n, (2 * n + 1)**2 - 6*n}
        new_diagonal_primes = prime_numbers.prime_subset(new_diagonal_numbers)
        set_of_diagonal_numbers = set_of_diagonal_numbers | new_diagonal_numbers
        set_of_diagonal_primes = set_of_diagonal_primes | new_diagonal_primes

        ratio = len(set_of_diagonal_primes)/(4*n + 1)

        if ratio < target_ratio:
            return ratio, 2*n + 1


    return ratio, 2*n + 1
