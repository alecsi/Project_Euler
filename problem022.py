def solution(csv_file = 'p022_names.txt'):
    """returns sumproduct of alphabetical value and alphabetical position of a list of names"""

    f = open(csv_file, 'r')
    g = f.read()
    g = g.replace('"','')
    names = g.split(',')
    names.sort(key = str.upper)
    running_total, i = 0, 1
    for name in names:
        running_total = running_total + i * string_to_number(name)
        i = i + 1

    return running_total


def string_to_number(input_string):
    """converts letters to numbers and then sums over the numbers"""

    running_total =  0
    for letter in input_string:
        running_total = running_total + letter_score(letter)

    return running_total

def letter_score(input_letter):
    """converts a letter to it's integer position in the alphabet"""

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.index(input_letter) + 1
