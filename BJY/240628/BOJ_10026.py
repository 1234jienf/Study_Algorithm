# 문제
## 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 
## 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

## 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 
## 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 
## 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. 
## (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

## 예를 들어, 그림이 아래와 같은 경우에

# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR

## 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 
## 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

## 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.


## 입력

## 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

## 둘째 줄부터 N개 줄에는 그림이 주어진다.

## 출력

## 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.
from collections import deque

def nor_bfs(i,j):
  q.append([i,j])
  visited[i][j] = 1

  while q:
    now = q.popleft()
    for k in range(4):
      nx,ny = now[0] + di[k], now[1] + dj[k]
      if 0 <= nx < N and 0 <= ny < N:
        if not visited[nx][ny] and color[nx][ny] == color[now[0]][now[1]]:
          q.append([nx,ny])
          visited[nx][ny] = 1


def col_bfs(i,j):
  q2.append([i,j])
  visited2[i][j] = 1

  while q2:
    now = q2.popleft()
    for k in range(4):
      nx,ny = now[0] + di[k], now[1] + dj[k]
      if 0 <= nx < N and 0 <= ny < N and not visited2[nx][ny]:
        if color[nx][ny] == color[now[0]][now[1]]:
          q2.append([nx,ny])
          visited2[nx][ny] = 1
        if color[nx][ny] != color[now[0]][now[1]]:
          if (color[nx][ny] == 'R' and color[now[0]][now[1]] == 'G') or (color[nx][ny] == 'G' and color[now[0]][now[1]] == 'R'):
            q2.append([nx,ny])
            visited2[nx][ny] = 1

N = int(input())


color = []
q = deque()
q2 = deque()
di = [0,0,1,-1]
dj = [1,-1,0,0]
visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
for _ in range(N):
  color.append(list(input()))

ans1 = 0
ans2 = 0

for i in range(N):
  for j in range(N):
    if visited[i][j] == 0:
      nor_bfs(i,j)
      ans1 += 1
    if visited2[i][j] == 0:
      col_bfs(i,j)
      ans2 += 1

print(ans1, ans2)
