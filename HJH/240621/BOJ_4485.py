import sys
from heapq import *
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

cnt = 0
INF = 125 * 125 * 10
while True:
    cnt+=1
    n = int(input())
    if n == 0:
        break
    cells = [list(map(int, input().split())) for _ in range(n)]
    dists = [[INF] * n for _ in range(n)]
    dists[0][0] = cells[0][0]
    fixed = [[False] * n for _ in range(n)]
    pq = [(cells[0][0], 0, 0)]
    while pq:
        dist, y, x = heappop(pq)
        if fixed[y][x]:
            continue
        fixed[y][x] = True
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if not (n > yy >= 0 and n > xx >= 0):
                continue
            if fixed[yy][xx]:
                continue
            if dists[yy][xx] > dists[y][x] + cells[yy][xx]:
                dists[yy][xx] = dists[y][x] + cells[yy][xx]
                heappush(pq, (dists[yy][xx], yy, xx))

    print(f'Problem {cnt}: {dists[n-1][n-1]}')