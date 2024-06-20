from itertools import product


def solution(users, emoticons):

    discount = [10,20,30,40]
    people = len(users)
    products = len(emoticons)
    answer_lst = []

    def calc(lst,users):
        join = 0
        ans = 0
        for person in users:
            cnt = 0
            buy = 0
            for i in range(products):
                discount = lst[i]
                if person[0] <= discount:
                    buy += emoticons[i] * (100-discount)/100
                if buy >= person[1]:
                    join += 1
                    break
            else:
                ans += buy
        return [join, ans] 
    

    result = [0, 0]
    
    for emoticon in product([10, 20, 30, 40], repeat=products):
    
        now = calc(emoticon, users)
        if result[0] < now[0]:
            result[0] = now[0]
            result[1] = now[1]
        elif result[0] == now[0]:
            result[1] = max(result[1], now[1])
            
    return result
    