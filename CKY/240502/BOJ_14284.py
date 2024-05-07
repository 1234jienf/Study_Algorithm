import sys
import heapq

input = sys.stdin.readline



N, M = map(int,input().split())

distance = [10 ** 9] *(N+1)
graph = [[]for _ in range(N+1)]

for _ in range(M):
    S,E,W = map(int,input().split())
    graph[S].append((W,E))
    graph[E].append((W,S))

S,T = map(int,input().split())
cnt = 0
def dijkstra(start):
    global cnt
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        heapq.heappop(graph[now])

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[0]]:
                if distance[i[0]] == 10**9:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
                else:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
                    cnt += 1
                if i[0] == T:
                    print(cnt)
                    exit()

dijkstra(S)
print(cnt)