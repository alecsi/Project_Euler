def factor_sum(max_number, factor):
    """Returns the sum of all multiples of factor that are strictly less than max_number."""

    return 0.5 * factor * ((max_number - 1) // factor) * ((max_number - 1) // factor + 1)



def answer(max_number=1000, factor1=3, factor2=5):
    """Returns the sum of all numbers strictly less than max_number, which have either (or both) of factor1 & factor2 as factors"""

    return factor_sum(max_number, factor1) + factor_sum(max_number, factor2) - factor_sum(max_number, factor1 * factor2)
