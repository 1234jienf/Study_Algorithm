# 문제
## N×M의 모눈종이 위에 아주 얇은 치즈가 <그림 1>과 같이 표시되어 있다. 
## 단, N 은 세로 격자의 수이고, M 은 가로 격자의 수이다. 
## 이 치즈는 냉동 보관을 해야만 하는데 실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다. 
## 그런데 이러한 모눈종이 모양의 치즈에서 각 치즈 격자(작 은 정사각형 모양)의 4변 중에서 
## 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다. 
## 따라서 아래 <그림 1> 모양과 같은 치즈(회색으로 표시된 부분)라면 C로 표시된 모든 치즈 격자는 한 시간 후에 사라진다.

## 모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다. 
## 입력으로 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 구하는 프로그램을 작성하시오.


## 입력

## 첫째 줄에는 모눈종이의 크기를 나타내는 두 개의 정수 N, M (5 ≤ N, M ≤ 100)이 주어진다.
## 그 다음 N개의 줄에는 모눈종이 위의 격자에 치즈가 있는 부분은 1로 표시되고, 
## 치즈가 없는 부분은 0으로 표시된다. 또한, 각 0과 1은 하나의 공백으로 분리되어 있다.


## 출력

## 출력으로는 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 정수로 첫 줄에 출력한다.


### 치즈 내부 구간 2로 표시하기 
from collections import deque

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
q = deque()
di = [0,0,1,-1]
dj = [1,-1,0,0]
ans = 0
flag = 0
### 치즈 내부 구역 업데이트
def bfs(i,j):
  q.append([i,j])
  visited[i][j] = 1


  while q:
    now = q.popleft()
    for k in range(4):
      nx, ny = now[0] + di[k], now[1] + dj[k]
      if 0 <= nx < N and 0 <= ny < M:
        if not visited[nx][ny] and arr[nx][ny] == 0:
          q.append([nx,ny])
          visited[nx][ny] = 1
        elif arr[nx][ny] == 1:
          visited[nx][ny] += 1

while flag == 0:
  flag = 1
  ("도는 횟수")
  visited=[[0 for _ in range(M)] for _ in range(N)]
  bfs(0,0)
  ## 탐색이 모두 끝나면
  ans += 1

  for i in range(N):
    for j in range(M):
      if visited[i][j] >= 2:
        arr[i][j] = 0

  for i in range(N):
    for j in range(M):
      if arr[i][j] == 1:
        flag = 0
        break
    if flag == 0:
      break

print(ans)
