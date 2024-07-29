import sys
import heapq

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0
    while queue:
        cost, now = heapq.heappop(queue)
        if distance[now] < cost:
            continue
        for i in matrix[now]:
            next = i[0]+cost
            if distance[i[1]] > next:
                distance[i[1]] = next
                heapq.heappush(queue,(next,i[1]))

input = sys.stdin.readline

N,M,X = map(int,input().split())

answer = [ 0 for _ in range(N+1)]

matrix = [ [] for _ in range(N+1) ]

for _ in range(M):
    S,E,W = map(int,input().split())
    matrix[S].append((W,E))


for i in range(1,N+1):
    distance = [ 10**9 for _ in range(N+1) ]
    dijkstra(i)
    if i == X:
        for j in range(1,N+1):
            if j != i:
                answer[j] += distance[j]
    else:
        answer[i] += distance[X]

print(max(answer))