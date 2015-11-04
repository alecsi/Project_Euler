def solution():

    return d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000) 



def d(n):
    """return the ith decimal digit of Champernowne's constant"""

    total = 0
    i = 0
    while total < n/9:
        i = i + 1
        total = total + i*(10**(i-1))
    
    total = total - i*(10**(i-1))
    p = n-total*9
    number_position = (p+i-1)//i
    digit_position = (p-1) % i + 1

    number = 10**(i-1) + number_position - 1

    return int(str(number)[digit_position-1]) 
