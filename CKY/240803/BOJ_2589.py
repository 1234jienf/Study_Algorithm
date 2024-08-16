from collections import deque
import sys

input = sys.stdin.readline
# 방향 탐색
direction = [(0,-1), (-1,0), (0,1), (1,0)]
# 너비 우선 탐색
def BFS(x,y):
    global max_value
    visited = [ [0] * M for _ in range(N) ]
    visited[x][y] = 1
    queue = deque([(x,y)])
    while queue:
        check = queue.popleft()
        for k in range(4):
            ny = check[0] + direction[k][0]
            nx = check[1] + direction[k][1]
            # 범위 내 존재
            if 0 <= ny < N and 0 <= nx < M:
                # 땅이고 방문하지 않았을 경우
                if matrix[ny][nx] == "L" and visited[ny][nx] == 0:
                    # 방문처리 후 최대값 비교
                    visited[ny][nx] = visited[check[0]][check[1]] + 1
                    if visited[ny][nx] > max_value:
                        max_value = visited[ny][nx]
                    queue.append((ny,nx))

N, M = map(int,input().split())

matrix = [ list(map(str,input())) for _ in range(N) ]

max_value = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == "L":
            BFS(i,j)

print(max_value-1)