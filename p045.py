import geometric_numbers

def solution():

    n = 1
    number_of_solutions_found = 0 
    while number_of_solutions_found < 3:
        Hn = geometric_numbers.hexagonal(n)
        if geometric_numbers.is_pentagonal(Hn):
            number_of_solutions_found  = number_of_solutions_found  + 1
            print(Hn)

        n = n+ 1

    return n
