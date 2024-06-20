# 문제
## 농부 현서는 농부 찬홍이에게 택배를 배달해줘야 합니다. 
## 그리고 지금, 갈 준비를 하고 있습니다. 평화롭게 가려면 가는 길에 만나는 모든 소들에게 맛있는 여물을 줘야 합니다.
## 물론 현서는 구두쇠라서 최소한의 소들을 만나면서 지나가고 싶습니다.
## 농부 현서에게는 지도가 있습니다. N (1 <= N <= 50,000) 개의 헛간과, 
## 소들의 길인 M (1 <= M <= 50,000) 개의 양방향 길이 그려져 있고,
## 각각의 길은 C_i (0 <= C_i <= 1,000) 마리의 소가 있습니다. 
## 소들의 길은 두 개의 떨어진 헛간인 A_i 와 B_i (1 <= A_i <= N; 1 <= B_i <= N; A_i != B_i)를 잇습니다.
## 두 개의 헛간은 하나 이상의 길로 연결되어 있을 수도 있습니다. 
## 농부 현서는 헛간 1에 있고 농부 찬홍이는 헛간 N에 있습니다.
## 다음 지도를 참고하세요.

#          [2]---
#          / |    \
#         /1 |     \ 6
#        /   |      \
#     [1]   0|    --[3]
#        \   |   /     \2
#        4\  |  /4      [6]
#          \ | /       /1
#           [4]-----[5] 
#                3  
## 농부 현서가 선택할 수 있는 최선의 통로는 1 -> 2 -> 4 -> 5 -> 6 입니다.
## 왜냐하면 여물의 총합이 1 + 0 + 3 + 1 = 5 이기 때문입니다.


## 입력

# 첫 번째 줄에는 스킬 개수 N(1 ≤ N ≤ 5)과 몬스터의 체력(HP)을 나타내는 정수(1 ≤ HP ≤ 100000)가 주어진다.
# 두 번째 줄부터는 줄마다 스킬의 대기 시간을 초 단위로 나타내는 정수 C(1 ≤ C ≤ 10)와 
# 스킬의 대미지를 나타내는 정수 D(HP/10 ≤ D ≤ HP)가 공백을 두고 주어진다. 
# 모든 스킬의 대기 시간은 다르며, 모든 D의 합은 HP보다 작다.

## 농부 현서의 지도가 주어지고, 지나가는 길에 소를 만나면 줘야할 여물의 비용이 주어질 때 
## 최소 여물은 얼마일까요? 농부 현서는 가는 길의 길이는 고려하지 않습니다.


## 입력
### 첫째 줄에 N과 M이 공백을 사이에 두고 주어집니다.
### 둘째 줄부터 M+1번째 줄까지 세 개의 정수 A_i, B_i, C_i가 주어집니다.

## 출력

# 첫째 줄에 농부 현서가 가져가야 될 최소 여물을 출력합니다.

import heapq

## N은 노드의 개수, M은 간선의 개수
N, M = map(int,input().split())
## 거리배열
distance = [float('inf')] * (N + 1)
## 방문 배열
visited = [0] * (N+1)

lst = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,v = map(int,input().split())
    lst[s].append((e,v))
    lst[e].append((s,v))

pq = []
heapq.heappush(pq, (0, 1))
distance[1] = 0

while pq :
    ## 우선순위를 기점으로 pop
    dist, current = heapq.heappop(pq)
    ## 현재 정점 번호를 받음
    if visited[current]:
        continue
    visited[current] = 1
    for tmp in lst[current]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[current] + value:
            distance[next] = distance[current] + value
            ## 우선 순위에 따라 저장함
            heapq.heappush(pq, (distance[next],next))

print(distance[N])


# import math
# from queue import PriorityQueue

# ## N은 노드의 개수, M은 간선의 개수
# N, M = map(int, input().split())
# q = PriorityQueue()
# ## 거리배열
# distance = [math.inf] * (N + 1)
# ## 방문 배열
# visited = [0] * (N + 1)
# lst = [[] for _ in range(N + 1)]

# for _ in range(M):
#     s, e, v = map(int, input().split())
#     lst[s].append((e, v))
#     lst[e].append((s, v))

# q.put((0, 1))
# distance[1] = 0

# while not q.empty():
#     ## 우선순위를 기점으로 pop
#     dist, current = q.get()
#     ## 이미 방문한 노드는 스킵
#     if visited[current]:
#         continue
#     visited[current] = 1

#     for next_node, value in lst[current]:
#         if distance[next_node] > distance[current] + value:
#             distance[next_node] = distance[current] + value
#             ## 우선 순위에 따라 저장함
#             q.put((distance[next_node], next_node))

# print(distance[N])
