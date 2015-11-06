primes = [17,13,11,7,5,3,2,1]

def valid_digit(i, x):
    """works out if i is a possible valid next digit"""

    if i in x:
        return False

    prime = primes[len(x)-2]
    print(prime)
    if int(i + x[:2]) % prime != 0:
        return False

    return True


def solution():

    current_set = [str(n) for n in range(100,1000) if n % 17 == 0 and str(n)[0]!=str(n)[1] and str(n)[0]!=str(n)[2] and str(n)[1]!=str(n)[2]] 
    for k in range(1,8):
        current_set = [str(i) + j for i in range(0,10) for j in current_set if valid_digit(str(i),j)]

    return sum(int(x) for x in current_set)



