# word = list(map(str,input().strip().split(".")))

# for wor in word[:-1]:
#     wor = wor.strip()
#     print(f"# {wor}.")

import heapq

N, D = map(int,input().split())

road = [[] for _ in range(10001)]
road_weight = [ [0] * 10001 for _ in range(10001) ]
start_road = []

for _ in range(N):
    S, E, W = map(int,input().split())
    heapq.heappush(road[S],(W,E))
    start_road.append(S)

for 