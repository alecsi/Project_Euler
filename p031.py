def solution(total = 200, list_of_available_coins = [1,2,5,10,20,50,100,200]):
    
     if total == 0:
        return 1
     else:
        running_total = 0
        for i in list_of_available_coins:
             if total - i >= 0:
                new_list_of_available_coins = [x for x in list_of_available_coins if x <= i]
                running_total = running_total + combinations(total - i, new_list_of_available_coins)

        return running_total
