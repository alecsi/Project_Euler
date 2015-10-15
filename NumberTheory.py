def sum_of_divisors(n):
    """uses prime decomposition to construct all factors"""

    "returns the sum of a number's divisors, including itself"

    running_total = 1
    possible_factor = 2
    while possible_factor**2 <= n:
        p = 1
        while (n % possible_factor == 0):
            p = p * possible_factor + 1
            n = n / possible_factor

        running_total = running_total * p
        possible_factor = possible_factor + 1

    if n > 1:
        running_total = running_total * (1 + n)

    return running_total
