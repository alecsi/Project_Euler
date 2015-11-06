import words

def word_value(word):
    if word == "":
        return 0
    else:
        return ord(word[:1]) - 64 + word_value(word[1:]) 


def triangle_set(n):
    """returns a set of the first n triangle numbers"""
   
    result = set() 
    for i in range(1,n+1):
        result.add((i*(i+1))//2)

    return result

def solution(input_file = 'p042_words.txt'):

    triangle_numbers = triangle_set(100)
    words_list = words.csv_to_list(input_file)

    return sum([(word_value(w) in triangle_numbers) for w in words_list])
