# 문제:
## 물에 잠기지 않는 안전한 영역이라 함은 
## 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 
## 그 크기가 최대인 영역을 말한다. 

# 입력:
## 첫째 줄 // 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다
### N은 2 이상 100 이하의 정수이다
## 둘째 줄 // N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다
### 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다.
### 높이는 1이상 100 이하의 정수이다.


# 출력:
## 첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.
import sys
sys.setrecursionlimit(100000) 
from collections import deque

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

MAX_NUM = 0
for i in range(N):
    for j in range(N):
        MAX_NUM = max(arr[i][j],MAX_NUM)
        
        
dx = [0,1,-1,0]
dy = [1,0,0,-1]


def bfs(cx,cy,num):
    q = deque()
    q.append((cx, cy))
    visited[cx][cy] = 1
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] > num:
                visited[nx][ny] = 1
                q.append((nx,ny))
                

ans = 0
for num in range(MAX_NUM):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > num and not visited[i][j]:
                bfs(i,j,num)
                cnt += 1
    ans = max(cnt, ans)
print(ans)


## 런타임 에러 발생 문제로 인해서 sys 사용