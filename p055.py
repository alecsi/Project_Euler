import base10

def solution(max_n = 10000):

    running_total = 0
    for n in range(1,max_n):
        running_total += is_lychrel(n)

    return running_total

def is_lychrel(n, counter = 50):

    if counter <= 0:
        return True
    else:
        x = n + base10.reverse(n)
        if base10.is_palindrome(x):
            return False

        return is_lychrel(x, counter - 1)

