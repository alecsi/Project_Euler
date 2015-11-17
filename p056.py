def solution(max_i = 1000):

    i = 1
    numerator = 3
    denominator = 2
    running_total = 0

    while i <= max_i:
        if len(str(numerator))>len(str(denominator)):
            running_total += 1

        numerator = numerator + 2 * denominator
        denominator = numerator - denominator
        i = i + 1

    return running_total
