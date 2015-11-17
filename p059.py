def XOR_list(input_list, code):
    """works with two lists of numbers, whereby if the code is shorter than the input list, it is applied cyclically"""

    return  [input_list[n]^code[n % len(code)] for n in range(0,len(input_list))]


def intlist_to_string(int_list):

    return ''.join([chr(i) for i in int_list])


def XOR_and_convert(input_list, code):

    return intlist_to_string(XOR_list(input_list, code)


# the code is [103,111,100], found by assuming space is the most common character
