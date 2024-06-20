import sys
import heapq
# 다익스트라 알고리즘
def dijkstra(start):
    # 항상 초기 거리 0 선언 및 시작 위치!!! 중요
    distance[start] = 0
    queue = [(0,1)]
    # 우선순위 큐를 통해서 구현
    while queue:
        # 현재 비용과 노드 pop
        cost, now = heapq.heappop(queue)
        # 현재 거리에 cost 값과 노드에 cost 값이 더 큰 경우 반복문 마저 진행
        if cost > distance[now]:
            continue
        # 다음 노드를 matrix 에서 가져와서 거리값을 갱신
        for next in matrix[now]:
            dist = cost + next[0]
            # 거리값이 다음 노드의 가중치보다 작은 경우 갱신 후 queue에 추가
            if dist < distance[next[1]]:
                distance[next[1]] = dist
                heapq.heappush(queue,(dist,next[1]))

input = sys.stdin.readline

N, M = map(int,input().split())

distance = [10**9]* (N+1)

matrix = [[] for _ in range(N+1)]

for _ in range(M):
    S, E, C = map(int,input().split())
    matrix[S].append((C,E))
    matrix[E].append((C,S))

dijkstra(1)
print(distance[-1])