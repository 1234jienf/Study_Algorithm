N, D = map(int,input().split())

road_list = []
road_weight = [0]*(D+1)

for i in range(D+1):
    road_weight[i] = i

for _ in range(N):
    S, E, W = list(map(int,input().split()))
    if E <= D:
        road_list.append((S,E,W))

road_list.sort()

print(road_weight[10])