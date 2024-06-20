import sys
from heapq import *
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = 50000 * 1000 + 1
dist = [INF] * (n + 1)
fixed = [False] * (n+1)
pq = []
heappush(pq, (0, 1))
while pq:
    distNow, now = heappop(pq)
    if fixed[now] == True:
        continue
    for next, length in graph[now]:
        if fixed[next]:
            continue
        newDist = distNow + length
        if dist[next] > newDist:
            dist[next] = newDist
            heappush(pq, (newDist, next))
print(dist[n])