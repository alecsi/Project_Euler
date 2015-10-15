import NumberTheory

def solution():
    """calculate the sum of all numbers that cannot be written as the sum of two abundant numbers"""

#First calculate a list of abundant numbers up to 28123

    list_of_abundant_numbers = []
    n = 1
    while n <= 28123:
        if NumberTheory.sum_of_divisors(n) > 2 * n:
            list_of_abundant_numbers.append(n)

        n = n + 1
#Second calculate a dict where the keys are all possible abundant pair wise sums up to 28123

    dict_of_abundant_number_pair_sums = {}
    n = 0
    while n <= len(list_of_abundant_numbers):
        m = n
        while m < len(list_of_abundant_numbers):
            x = list_of_abundant_numbers[n] + list_of_abundant_numbers[m]
            if (x > 28123) : break
            dict_of_abundant_number_pair_sums[x] = True
            m = m + 1       
 
        n = n + 1
#Finally calculate the sum of numbers upto 28123 which are not keys in the dictionary

    n = 1
    running_total = 0
    while n <= 28123:
        if n not in dict_of_abundant_number_pair_sums:
            running_total = running_total + n
            
        n = n + 1

    return running_total
        
