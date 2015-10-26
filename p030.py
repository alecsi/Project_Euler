def solution(i = 5):


    total = 0
    for n in range(9, 354295):
        if sum_of_digits_to_ith_power(n, i) == n:
#            print(n)
            total = total + n

    return total 

def convert_number_into_list_of_digits(n):
    """converts a number into a list of it's constituent digits base10"""

    n = int(n)
    digits_list = []
    while n > 0:    
        digits_list.append(n % 10)
        n = (n - (n % 10))//10

    digits_list.reverse()
    return digits_list

def sum_of_digits_to_ith_power(n,i):
    """decomposes n into it's consituent digits, raises them each to the power of i and returns the sum"""

    digits_list =  convert_number_into_list_of_digits(n)
    total = 0
    for x in digits_list:
        total = total + x**i

    return total



