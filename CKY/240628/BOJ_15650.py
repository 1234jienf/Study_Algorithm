def backtracking(start,end):
    global M
    global N
    if end == M:
        print(*answer)
        return
    for i in range(start,N+1):
        if answer:
            if answer[-1] != i:
                answer.append(i)
                backtracking(i,end+1)
                answer.pop()
        else:
            answer.append(i)
            backtracking(i,end+1)
            answer.pop()


N,M = map(int,input().split())

answer = []

backtracking(1,0)