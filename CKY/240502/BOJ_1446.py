import heapq

N, D = map(int,input().split())

road_list = []
road_weight = [0]*(D+1)

for i in range(D+1):
    road_weight[i] = i

for _ in range(N):
    S, E, W = list(map(int,input().split()))
    if E <= D:
        road_weight[S] = S - 0

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
