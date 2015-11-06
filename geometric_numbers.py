def triangle(n):
    return n*(n+1)//2

def pentagonal(n):
    return n*(3*n-1)//2

def hexagonal(n):
    return n*(2*n-1)

def is_triangle(n):
    return is_square(1+8*n)

def is_square(n):
    return n == int(n**0.5 + 0.5)**2

def is_pentagonal(n):
    if is_square(1+24*n):
        return int((1+24*n)**0.5+0.5) % 6 == 5
    else:
        return False
