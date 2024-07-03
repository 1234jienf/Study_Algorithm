from collections import deque

n = int(input())
cells = [input() for _ in range(n)]

cnt = 0
cntColorBlind = 0
visited = [[False] * n for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y: int, x: int, isColorBlindness: bool):
    areaColor = cells[y][x]
    if isColorBlindness and areaColor in 'RG':
        areaColor = 'RG'
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        visited[y][x] = True
        for d in range(4):
            yy = y + dy[d]
            xx = x + dx[d]
            if not (0 <= yy < n and 0 <= xx < n):
                continue
            if visited[yy][xx] or cells[yy][xx] not in areaColor:
                continue
            # 중요! 빼먹지 말자
            visited[yy][xx] = True
            q.append((yy, xx))

for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            bfs(y, x, False)
            cnt += 1

visited = [[False] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            bfs(y, x, True)
            cntColorBlind += 1

print(cnt, cntColorBlind)