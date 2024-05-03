# word = list(map(str,input().strip().split(".")))

# for wor in word[:-1]:
#     wor = wor.strip()
#     print(f"# {wor}.")

import heapq

N, D = map(int,input().split())

road = [[] for _ in range(10001)]
road_weight = [[10**9,i] for i in range(N+1)]
start_road = []

for _ in range(N):
    S, E, W = map(int,input().split())
    if E <= D:
        road[S].append((W,E))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    road_weight[start][0] = 0

    while q:
        dist, now = heapq.heappop(q)
        if road_weight[now][0] < dist:
            continue

        for i in road[now]:
            cost = dist + i[1]
            if cost < road_weight[i[0]][0]:
                road_weight[i[0]][0] = cost
                road_weight[i[0]][0] = now
                