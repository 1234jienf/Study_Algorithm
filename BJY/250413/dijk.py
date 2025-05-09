## N개 node, M개의 양방향 edge
## 두 도시 사아의 거리 = 두 도시 사이를 연결하는 도로 길이의 합 중 최솟값
## 다익스트라 알고리즘

## K개의 도시에 기차역이 있다
## 역세권 ? -> 어떤 도시에서 가장 가까운 기차역이 있는 도시와의 거리가 D이하라며

## 도시의 수 N, 도로의 수 M, 기차역 도시 수 K, D
### 3 <= N <= 200,000 / 0 <= M <= 300,000 / 1 <= K <= N 
### 1 <= D <= 10**18 / 1 <= Pi <= N / 도로의 길이 Ci, 1 <= Ci <= 10**9

## 5 4 2 3
## 3 1 
## 1 3 5 
## 2 4 3

import sys
import heapq

N, M, K, D = map(int,input().split())
trains = list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for i in range(M):
	a, b, c = map(int,input().split())
	graph[a].append((b,c))
	graph[b].append((a,c))
	

distance = [sys.maxsize] * (N+1)
## 시작점 - 기차역에서 각 역들의 최소 거리를 재고, 만약 그 값이 D이하라면 역세권

q = []

for train in trains:
	distance[train] = 0
	heapq.heappush(q, (0,train))

while q:
	dist, node = heapq.heappop(q)
	if dist > distance[node]:
		continue
	for next, cost in graph[node]:
		new_dist = dist + cost
		if new_dist < distance[next]:
			distance[next] = new_dist
			heapq.heappush(q, (new_dist, next))

cnt = 0
for i in range(1,N+1):
	if distance[i] <= D:
		cnt += 1
		
print(cnt)