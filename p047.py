import prime_numbers

def solution(x = 4):

    running_total = 0
    n = 1
    while n < 1000000:
        if prime_numbers.number_of_distinct_prime_factors(n) == x:
            running_total = running_total + 1
            if running_total == x:
                return n - x + 1
        else:
            running_total = 0
            
        n = n + 1
