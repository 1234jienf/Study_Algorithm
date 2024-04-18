# 문제
## N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다.
## 각각의 땅에는 나라가 하나씩 존재하며, 
## r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 
##  인접한 나라 사이에는 국경선이 존재한다.
## 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

#### 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

### 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
### 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
### 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
### 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
### 연합을 해체하고, 모든 국경선을 닫는다.

### 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.


## 입력

# 첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100) 
# 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다.
# r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
# 인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

## 출력

## 인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.

## N * N 크기의 맵, 인구차가 L이상 R이하
from collections import deque

N,L,R = map(int,input().split())

arr=[list(map(int,input().split()))for _ in range(N)]


dx= [0,0,1,-1]
dy = [1,-1,0,0]



def bfs(ci,cj):
    p_sum = arr[ci][cj] # 인구 합
    alst = [(ci,cj)] # 연합에 든 나라
    q = deque()
    q.append((ci,cj))
    visited[ci][cj] = 1
    
    while q:
        now = q.popleft()
        for k in range(4):
            ni, nj = now[0] + dx[k], now[1] + dy[k]
            # 영역 내, 미방문, 인구 차가 조건 만족
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L<= abs(arr[now[0]][now[1]] - arr[ni][nj]) <= R:
                q.append((ni,nj))
                alst.append((ni,nj))
                p_sum += arr[ni][nj]
                visited[ni][nj] = 1
    if len(alst) > 1:     # 인구 이동 가능
        number = len(alst)
        for i in range(len(alst)):
            con = alst.pop()
            arr[con[0]][con[1]] = p_sum // number
        return 1
    return 0
ans = 0
while ans <= 2000:
    flag = 0
    visited = [([0]*N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                flag = max(flag, bfs(i,j))
                
    if flag == 0:
        break
    ans += 1


print(ans)