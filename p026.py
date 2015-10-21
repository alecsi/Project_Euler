def solution(n = 1000):
 
    max_value = 0
    i = 2
    answer = 2
    while i < n:
        x =  number_of_recurring_digits_in_reciprocal(i) 
        if x > max_value:
            max_value = x
            answer = i

        i = i + 1

    return answer

def number_of_recurring_digits_in_reciprocal(n,previous_carry = 1, remainders = None):


    if remainders == None: remainders = []
    next_carry = (previous_carry * 10) % n
    if next_carry == 0: return 0
    if remainders.count(next_carry)==1: return len(remainders)
    remainders.append(next_carry)
    return number_of_recurring_digits_in_reciprocal(n, next_carry, remainders)
 

def test_number_of_recurring_digits_in_reciprocal():


    print("test number_of_recurring_digits:")
    print("2:", number_of_recurring_digits_in_reciprocal(2) == 0)
    print("3:", number_of_recurring_digits_in_reciprocal(3) == 1)
    print("4:", number_of_recurring_digits_in_reciprocal(4) == 0)
    print("5:", number_of_recurring_digits_in_reciprocal(5) == 0)
    print("6:", number_of_recurring_digits_in_reciprocal(6) == 1)
    print("7:", number_of_recurring_digits_in_reciprocal(7) == 6)
    print("8:", number_of_recurring_digits_in_reciprocal(8) == 0)
    print("9:", number_of_recurring_digits_in_reciprocal(2) == 1)


def test_solution():

    print("test solution:")
    print("2:", solution(2) == 0)
    print("3:", solution(3) == 1)
    print("4:", solution(4) == 1)
    print("5:", solution(5) == 1)
    print("6:", solution(6) == 1)
    print("7:", solution(7) == 6)
    print("8:", solution(8) == 6)
    print("9:", solution(2) == 6)


