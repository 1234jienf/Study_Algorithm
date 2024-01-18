def solution(friends, gifts):
    answer = 0
    n = len(friends)
    array = [[0] * n for i in range(n)]
        
    gift_lv = {}

    for friend in friends:
        gift_lv[friend] = 0
        
    next_year = gift_lv.copy()

    for gift in gifts:
        A, B = gift.split()
        array[friends.index(A)][friends.index(B)] += 1
        gift_lv[A] += 1
        gift_lv[B] -= 1

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                if array[i][j] > array[j][i]:
                    next_year[friends[i]] += 1
                elif array[i][j] == array[j][i]:
                    if gift_lv[friends[i]] > gift_lv[friends[j]]:
                        next_year[friends[i]] += 1
                    else:
                        continue

    answer = max(next_year.values())
    return answer