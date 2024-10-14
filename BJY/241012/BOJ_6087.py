# 문제
## 크기가 1×1인 정사각형으로 나누어진 W×H 크기의 지도가 있다. 
## 지도의 각 칸은 빈 칸이거나 벽이며, 두 칸은 'C'로 표시되어 있는 칸이다.

## 'C'로 표시되어 있는 두 칸을 레이저로 통신하기 위해서 설치해야 하는 거울 개수의 최솟값을 구하는 프로그램을 작성하시오. 
## 레이저로 통신한다는 것은 두 칸을 레이저로 연결할 수 있음을 의미한다.

## 레이저는 C에서만 발사할 수 있고, 빈 칸에 거울('/', '\')을 설치해서 방향을 90도 회전시킬 수 있다.

## 아래 그림은 H = 8, W = 7인 경우이고, 빈 칸은 '.', 벽은 '*'로 나타냈다. 
## 왼쪽은 초기 상태, 오른쪽은 최소 개수의 거울을 사용해서 두 'C'를 연결한 것이다

# 7 . . . . . . .         7 . . . . . . .
# 6 . . . . . . C         6 . . . . . /-C
# 5 . . . . . . *         5 . . . . . | *
# 4 * * * * * . *         4 * * * * * | *
# 3 . . . . * . .         3 . . . . * | .
# 2 . . . . * . .         2 . . . . * | .
# 1 . C . . * . .         1 . C . . * | .
# 0 . . . . . . .         0 . \-------/ .
#   0 1 2 3 4 5 6           0 1 2 3 4 5 6

# 입력
## 첫째 줄에 W와 H가 주어진다. (1 ≤ W, H ≤ 100)

## 둘째 줄부터 H개의 줄에 지도가 주어진다. 
## 지도의 각 문자가 의미하는 것은 다음과 같다.

## .: 빈 칸
## *: 벽
## C: 레이저로 연결해야 하는 칸

## 'C'는 항상 두 개이고, 레이저로 연결할 수 있는 입력만 주어진다.

# 출력
## 첫째 줄에 C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값을 출력한다.

# mirror = {
#   (1,0) : [(0,1),(0,-1)],
#   (-1,0) : [(0,1),(0,-1)],
#   (0,1) : [(1,0),(-1,0)],
#   (0,-1) : [(1,0),(-1,0)],
# }


# def simulate(x,y,dx,dy,visited):

#   cnt = 0
#   while arr[x +dx][y+dy] != "C":
#     if 0 <= x + dx < H and 0 <= y + dy < W:
#       nx = x + dx
#       ny = y + dy
#       if visited[nx][ny] == True:
#         break
#       visited[nx][ny] = True
#       now = arr[nx][ny]
#       if now == "*":
#         min_cnt = 1e9
#         for next_dr in mirror[dx,dy]:
#           # next_dr[0], next_dr[1]
#           cnt +=1
#           min_cnt = min(min_cnt, simulate(x,y,next_dr[0],next_dr[1],visited))
#         return cnt + min_cnt
#     else:
#       min_cnt = 1e9
#       for next_dr in mirror[dx,dy]:
#         # next_dr[0], next_dr[1]
#         cnt +=1
#         min_cnt = min(min_cnt, simulate(x,y,next_dr[0],next_dr[1],visited))
#       return cnt + min_cnt
#   return cnt
    

# W, H = map(int,input().split())
# arr = [list(map(str,input())) for _ in range(H)]
# laser = []

# for i in range(H):
#   for j in range(W):
#     if arr[i][j] == 'C':
#       start_x,start_y = i,j
#       break

# visited = [[False] * W for _ in range(H)]

# result = []
# result.append(simulate(start_x,start_y,0,1,visited))
# result.append(simulate(start_x,start_y,0,-1,visited))
# result.append(simulate(start_x,start_y,1,0,visited))
# result.append(simulate(start_x,start_y,-1,0,visited))
# result.sort()
# print(result)
# print(result[0])

import heapq

## 동서남북
dir = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs_mirror(start,end):
  queue = []
  for i in range(4):  # 모든 방향에서 시작할 수 있도록 설정
    heapq.heappush(queue, (0, start[0], start[1], i))
  # 각 위치에서 방향별 최소 거울 개수를 저장하는 3차원 visited 배열
  visited = [[[float('inf')] * 4 for _ in range(W)] for _ in range(H)]
  for i in range(4):  # 시작 지점의 모든 방향 초기화
    visited[start[0]][start[1]][i] = 0


  while queue:
    mirrors , x, y, p_dir = heapq.heappop(queue)

    ## 목표 위치 도달시 종료
    if (x,y) == end:
      return mirrors
    
    ## 4방향 탐색
    for i, (dx,dy) in enumerate(dir):
      nx, ny = x + dx, y + dy
      new_mirrors = mirrors + (0 if i == p_dir else 1)

      # 벽을 만나지 않는 범위까지 직진
      while 0 <= nx < H and 0 <= ny < W and arr[nx][ny] != '*':
        if visited[nx][ny] > new_mirrors:
          visited[nx][ny] = new_mirrors
          heapq.heappush(queue, (new_mirrors, nx, ny, i))
                
        # 같은 방향으로 계속 진행
        nx += dx
        ny += dy
  return -1

W, H = map(int,input().split())
arr = [list(map(str,input())) for _ in range(H)]

lasers = [(i,j) for i in range(H) for j in range(W) if arr[i][j] == 'C']
start,end = lasers[0], lasers[1]

print(bfs_mirror(start,end))