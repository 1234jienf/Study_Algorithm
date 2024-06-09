from heapq import *

INF = 500001

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    fixed = [False] * (N+1)
    dijk = [INF] * (N+1)
    dijk[1] = 0
    
    pq = [(0, 1)]
    while pq:
        distance, node = heappop(pq)
        if distance >= K:
            break
        if fixed[node]:
            continue
        fixed[node] = True
        for conn in graph[node]:
            if fixed[conn[0]]:
                continue
            newDist = distance + conn[1]
            if dijk[conn[0]] > newDist:
                dijk[conn[0]] = newDist
                heappush(pq, (newDist, conn[0]))
    cnt = 0
    for dij in dijk:
        if dij <= K:
            cnt += 1

    return cnt