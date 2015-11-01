import itertools

def solution():

    return sum(base10palindromes()  & base2palindromes())

def base10palindromes():
    """returns a list of base 10 palindromes sub 1,000,000"""

    one_digit = set(range(1,10))
    even_digit = {int(str(a) + str(a)[::-1]) for a in range(1,1000)}
    odd_digit = {int(str(a) + str(b) + str(a)[::-1]) for a in range(1,100) for b in range(0,10)}

    return one_digit | even_digit | odd_digit

def base2palindromes():
    """returs a list of base 2 palindromes sub 1,000,000"""

    one_digit = {1}
    even_digit = {int(bin(a)[2:] + bin(a)[2:][::-1],2) for a in range(1,1024)} 
    odd_digit = {int(bin(a)[2:] + b + bin(a)[2:][::-1],2) for a in range(1,512) for b in ['0', '1']} 

    return one_digit | even_digit | odd_digit
