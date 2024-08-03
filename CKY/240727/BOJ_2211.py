import sys
import heapq

input = sys.stdin.readline
# 다익스트라 알고리즘
def dijkstra():
    queue = []
    # 다익스트라 초기값
    heapq.heappush(queue,(0,1))
    # 거리를 갱신하면서 현재 위치와 이후 위치를 갱신
    distance[1] = [0,[0,0]]
    while queue:
        # 코스트값, 다음 노드
        cost, now = heapq.heappop(queue)
        # 노드 거리가 더 작은경우 반복문 무시
        if cost > distance[now][0]:
            continue
        # 연결된 노드들 순회
        for i in graph[now]:
            # 다음 cost 값 갱신
            next = cost + i[0]
            # 다음 거리값이 더 작은경우
            if next < distance[i[1]][0]:
                # 거리 값과 움직인 노드 값을 갱신
                distance[i[1]] = [next,[now, i[1]]]
                heapq.heappush(queue,(next,i[1]))

N, M = map(int,input().split())

distance = [[10**9,[0,0]] for _ in range(N+1)]

graph = [[] for _ in range(N+1)]

for _ in range(M):
    S,E,C = map(int,input().split())
    graph[S].append((C,E))
    graph[E].append((C,S))

dijkstra()
cnt = 0
ans = []
# 초기값이 아니고 시작 노드가 아닌경우 cnt 증가 후 ans 리스트에 저장
for i in distance:
    if i[0] != 10**9 and i[0] != 0:
        cnt += 1
        ans.append(i[1])

print(cnt)
for j in ans:
    print(*j)