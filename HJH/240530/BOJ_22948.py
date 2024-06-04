import sys
from heapq import *
input = sys.stdin.readline

n = int(input())

datas = []

for _ in range(n):
    num, point, radius = map(int, input().split())
    datas.append((point-radius, num))
    datas.append((point+radius, num))

datas.sort()

stack = [0]
graph = [[] for _ in range(n + 1)]
for data in datas:
    if len(stack) == 0 or stack[-1] != data[1]:
        stack.append(data[1])
    # 원이 겹치는 경우는 없으므로 다른 경우는 없다고 가정
    else:
        now = stack.pop()
        graph[now].append(stack[-1])
        graph[stack[-1]].append(now)

start, end = map(int, input().split())
def dijk(start: int, end: int):
    global graph
    pq = [(0, start)]
    fixed = [False] * (n + 1)
    dists = [300000] * (n + 1)
    dists[start] = 0
    paths = [[] for _ in range(n + 1)]
    paths[start] = [start]

    while pq:
        dist, now = heappop(pq)
        if now == end:
            return paths[now]
        if fixed[now]:
            continue
        fixed[now] = True
        for conn in graph[now]:
            if dists[conn] > dist + 1:
                dists[conn] = dist + 1
                paths[conn] = paths[now][:]
                paths[conn].append(conn)
                pq.append((dists[conn], conn))

ans = dijk(start, end)
print(len(ans))
print(*ans, sep=' ')