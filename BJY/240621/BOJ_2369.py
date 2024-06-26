# 문제
## N×M(1 ≤ N, M ≤ 256)의 행렬이 하나 있다. 
## 이 행렬의 부분행렬들 중 그 성분(원)들의 합이 K(1 ≤ K ≤ 1,000,000)로 나누어떨어지는 경우가 몇 가지나 되는지 알아보려 한다.


## 부분행렬은 말 그대로 어떤 행렬에서 부분적으로 뽑아내는 행렬을 의미한다.

## 입력

## 첫째 줄에 세 개의 자연수 N, M, K가 주어진다. 
## 다음 N개의 줄에는 각 줄에 M개씩 정수들이 주어진다. 
## 각각은 행렬의 성분들이다. 각 성분은 1보다 크거나 같고, 50보다 작거나 같은 자연수이다.


## 출력

## 첫째 줄에 부분행렬의 개수를 출력한다.

N, M ,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cnt = 0

## 부분합을 저장할 리스트
D = [([0] * M)for _ in range(N)]
## 각 수는 1보다 크거나 같고, 50보다 작거나 같은 자연수이다.
num = [0] * 51

## 첫번째 열, 행 초기화
D[0][0] = arr[0][0]

for i in range(1,N):
  D[i][0] = D[i-1][0] + arr[i][0]

for j in range(1,M):
  D[0][j] = D[0][j-1] + arr[0][j]

for i in range(1,N):
  for j in range(1,M):
      D[i][j] = D[i-1][j] + D[i][j-1] + arr[i][j] - D[i-1][j-1]


for i in range(N):
  for j in range(M):
    for a in range(i,N):
      for b in range(j,M):
        s_sum = D[a][b] - D[a - 1][b] - D[a][b - 1] + D[i - 1][j - 1]
        if s_sum % K == 0:
          cnt += 1
    

print(cnt)