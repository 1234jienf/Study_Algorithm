from copy import deepcopy

candidate = []
disc = []
result = (0, 0)
u = 0
e = 0

def discount(money, percent):
    return int(money / 100 * (100 - percent))


def dfs(ith):
    global disc
    if ith == len(disc):
        global result, u, e
        money = [0] * len(u)
        sub = 0
        users = deepcopy(u)
        for di in range(len(disc)):
            for ui in range(len(users)):
                if users[ui][1] == 0:
                    continue
                if disc[di] >= users[ui][0]:
                    emo_disc = discount(e[di], disc[di])
                    if emo_disc >= users[ui][1]:
                        users[ui][1] = 0
                        money[ui] = 0
                        sub += 1
                    else:
                        users[ui][1] -= emo_disc
                        money[ui] += emo_disc
        if sub > result[0]:
            result = (sub, sum(money))
            # print(disc)
        elif sub == result[0] and sum(money) > result[1]:
            result = (sub, sum(money))
            # print(disc)

    else:
        global candidate
        for c in candidate:
            disc[ith] = c
            dfs(ith + 1)



def solution(users, emoticons):
    global disc, u, e, result, candidate
    users.sort()
    u = users
    e = emoticons
    disc = [0] * len(emoticons)
    c = set()
    for user in users:
        c.add(user[0])
    candidate = (10, 20, 30, 40)
    dfs(0)
    return list(result)