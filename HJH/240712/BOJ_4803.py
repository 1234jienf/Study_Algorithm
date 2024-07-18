from collections import deque

case = 0
n, m = 0, 0
graph = []
visited = [-1]

def isTree(i) -> bool:
    # print('Tree of')
    # print(i)
    q = deque()
    q.append((i, 1))
    visited[i] = 1
    ans = True
    while q:
        now, length = q.popleft()
        for next in graph[now]:
            if visited[next] == length - 1:
                continue
            if visited[next] != -1: # 사이클 발생
                # print('nvm')
                # print()
                ans = False
            else:
                # print(next)
                visited[next] = length + 1
                q.append((next, length+1))
    # print()
    return ans


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    case += 1

    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)

    for i in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = 0
    for i in range(1, n+1):
        if visited[i] == -1:
            istree = isTree(i)
            if istree:
                ans += 1

    if ans == 0:
        print(f'Case {case}: No trees.')
    elif ans == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {ans} trees.')