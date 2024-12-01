def solution(scores):
    fail = [False] * len(scores)
    l = len(scores)
    for i in range(l):
        if fail[i]:
            continue
        for j in range(l):
            if i == j:
                continue
            if fail[j]:
                continue
            if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
                fail[i] = True
            elif scores[i][0] > scores[j][0] and scores[i][1] > scores[j][1]:
                fail[j] = True
    if fail[0]:
        return -1
    for i in range(l):
        scores[i].append(i)
    scores.sort(key=lambda x: -x[0]-x[1])

    last_rank = 1
    last_idx = 0
    fail_check = 0
    for i in range(1, l):
        if fail[scores[i][2]]:
            fail_check += 1
        if scores[i][0] + scores[i][1] == scores[last_idx][0] + scores[last_idx][1]:
            pass
        else:
            last_rank = i + 1 - fail_check
            last_idx = i
        if scores[i][2] == 0:
            return last_rank
    return -1

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))