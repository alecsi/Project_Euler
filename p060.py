import prime_numbers

max_ = 10000

primes_list147 = [p for p in prime_numbers.default_seive if (p == 3 or p % 3 == 1) and p < max_]
primes_list258 = [p for p in prime_numbers.default_seive if (p == 3 or p % 3 == 2) and p < max_ and p != 2]

def concat(n1,n2):

    return int(str(n1) + str(n2))

def concat_are_prime(set_of_primes, n):
    for p in set_of_primes:
        if prime_numbers.is_prime_number(concat(p,n)) == False or prime_numbers.is_prime_number(concat(n,p)) == False:
            return False

    return True

def solution(current_set = set(), max_prime_in_set = 0):

    if len(current_set) == 5:
        print(sorted(list(current_set)), sum(current_set))

    gen = [p for p in primes_list147 if p > max_prime_in_set]
    for p in gen:
        if concat_are_prime(current_set, p):
            x = current_set.copy()
            x.add(p)
            solution(x, p) 

