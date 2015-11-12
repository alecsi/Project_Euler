import collections 

def solution():

    f = open('p054_poker.txt')
    x = f.readlines()
    hands = [z[:29].split(' ') for z in x]

    player1_score = 0
    for hand in hands:
        if (score(hand[:5]) > score(hand[5:])):
            player1_score = player1_score + 1

    return player1_score

def score(hand):
    """returs a twelve digit number, the first digit represents the type of hand, the remain digits represent how high the cards are"""
    total = 0

    isflush = is_flush(hand)

    handnumbers = hand_numbers(hand)

    isstraight =  is_straight(handnumbers)

    numbersmultiset = collections.Counter(handnumbers)

    if (isflush and isstraight):
        total = 9* 10**11 + max(handnumbers)
    elif is_4ofakind(numbersmultiset):
        total = 8 * 10**11 + handnumbers[2]
    elif is_fullhouse(numbersmultiset):
        total = 7 * 10**11 + handnumbers[2]
    elif isflush:
        total = 6 * 10**11 + 10 * handnumbers[0] + 10**3 * handnumbers[1] + 10**5 * handnumbers[2] + 10**7 * handnumbers[3] + 10**9 * handnumbers[4]
    elif isstraight:
        total = 5 * 10**11 + max(handnumbers)
    elif is_3ofakind(numbersmultiset):
        total = 4 * 10**11 + handnumbers[2]
    elif is_2pairs(numbersmultiset):
        handset = set(handnumbers)
        handset.remove(handnumbers[1])
        handset.remove(handnumbers[3])
        singlecardvalue = next(iter(handset))
        total = 3 * 10**11 + handnumbers[3]*10**5 + handnumbers[1]*10**3 + singlecardvalue*10
    elif is_pair(numbersmultiset):
        pairvalue = [x for x in handnumbers if numbersmultiset[x]==2][0]
        remainingcards = [c for c in handnumbers if c != pairvalue]
        total = 2 * 10**11 + pairvalue * 10**9 + remainingcards[2] * 10**7 + remainingcards[1]*10**5 + remainingcards[0]*10**3
    else:
        total = 10*11 + 10**9 * handnumbers[4] + 10**7 * handnumbers[3] + 10**5 * handnumbers[2] + 10**3 * handnumbers[1] + 10**1 * handnumbers[0]

    return total 


def hand_numbers(hand):

    numbers = [x[:1] for x in hand]
    numbers2 = [x.replace('A','14').replace('K','13').replace('Q','12').replace('J','11').replace('T','10') for x in numbers]
    numbers3 = [int(x) for x in numbers2]

    return sorted(numbers3)

def is_flush(hand):

    return len({x[1:] for x in hand}) == 1

def is_straight(sorted_hand_numbers):

    return all(sorted_hand_numbers[i]+1 == sorted_hand_numbers[i+1] for i in range(0,len(sorted_hand_numbers)-1))

def is_4ofakind(numbersmultiset):

    return max(numbersmultiset.values()) == 4

def is_fullhouse(numbersmultiset):

    return (max(numbersmultiset.values()) == 3 and min(numbersmultiset.values()) == 2)


def is_3ofakind(numbersmultiset):

    return (max(numbersmultiset.values()) == 3 and min(numbersmultiset.values()) == 1)

def is_2pairs(numbersmultiset):

    return (sorted(list(numbersmultiset.values())) == [1,2,2])

def is_pair(numbersmultiset):

    return (sorted(list(numbersmultiset.values())) == [1,1,1,2])
