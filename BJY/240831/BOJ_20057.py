# 문제
## 마법사 상어가 토네이도를 배웠고, 
## 오늘은 토네이도를 크기가 N×N인 격자로 나누어진 모래밭에서 연습하려고 한다. 
## 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 모래의 양을 의미한다.

## 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작된다. 
## 토네이도는 한 번에 한 칸 이동한다. 
## 다음은 N = 7인 경우 토네이도의 이동이다.

## 토네이도가 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 흩날리게 된다.

## 토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동한다. 
## 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다. 
## α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다. 
## 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다. 
## 위의 그림은 토네이도가 왼쪽으로 이동할 때이고, 다른 방향으로 이동하는 경우는 위의 그림을 해당 방향으로 회전하면 된다.

## 토네이도는 (1, 1)까지 이동한 뒤 소멸한다.
## 모래가 격자의 밖으로 이동할 수도 있다. 
## 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양을 구해보자.

# 입력
## 첫째 줄에 격자의 크기 N이 주어진다. 
## 둘째 줄부터 N개의 줄에는 격자의 각 칸에 있는 모래가 주어진다. 
## r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.

# 출력
## 격자의 밖으로 나간 모래의 양을 출력한다.


### 방향 기준 (<-)
###               (-2,0)
###       (-1,-1) (-1,0) (-1,1)
### (0,-2) (0,-1) (0,0)    x
###        (1,-1) (1,0) (1,1)
###               (2,0)

### 방향 기준 (v)
###        (-1,-1)  x   (-1,1)
### (0,-2) (0,-1) (0,0) (0,1) (0,2)
###        (1,-1) (1,0) (1,1)
###               (2,0)

### 방향 기준 (->)
###          (-2,0)
###  (-1,-1) (-1,0) (-1,1)
###     x     (0,0) (0,1) (0,2) 
###   (1,-1)  (1,0) (1,1)
###           (2,0)

### 방향 기준 (^)
###               (-2,0)
###       (-1,-1) (-1,0) (-1,1)   
### (0,-2) (0,-1) (0,0) (0,1) (0,2)
###        (1,-1)   x   (1,1)

# 서 남 동 북
dr = [(0,-1),(1,0),(0,1),(-1,0)]
percentage = [0.02,0.10,0.07,0.01,0.05,0.10,0.07,0.01,0.02]
sand = [
  [(-2,0),(-1,-1),(-1,0),(-1,1),(0,-2),(1,-1),(1,0),(1,1),(2,0),(0,-1)],
  [(0,-2),(1,-1),(0,-1),(-1,-1),(2,0),(1,1),(0,1),(-1,1),(0,2),(1,0)],
  [(2,0),(1,1),(1,0),(1,-1),(0,2),(-1,1),(-1,0),(-1,-1),(-2,0),(0,1)],
  [(0,-2),(-1,-1),(0,-1),(1,-1),(-2,0),(-1,1),(0,1),(1,1),(0,2),(-1,0)]
]
## 1 1 2 2 3 3 4 4 5 5 


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ci,cj = N // 2 , N // 2
cnt = 0
cnt_max = 1
now = 0
ans = 0
flag = 0
## 토네이도가 마지막에 도달하기 전까지
while (ci,cj) != (0,0):
  ci, cj = ci + dr[now][0], cj + dr[now][1]
  ## 현재 이동한 칸에 모래가 있다면
  if arr[ci][cj]:
    total = arr[ci][cj]
    remaining_sand = total
    
    for i in range(10):
      if i < 9:
        si,sj,per = ci + sand[now][i][0], cj + sand[now][i][1], percentage[i]
        move = int(total * per)
        if 0 <= si < N and 0 <= sj < N:
          arr[si][sj] += move
        else:
          ans += move
        remaining_sand -= move
      else:
        si,sj = ci + sand[now][i][0], cj + sand[now][i][1]
        if 0 <= si < N and 0 <= sj < N:
          arr[si][sj] += remaining_sand
        else:
          ans += remaining_sand
    arr[ci][cj] = 0
  cnt += 1
  if cnt == cnt_max:
    cnt = 0
    now = (now+1) % 4
    if flag == 0:
      flag = 1
    else:
      flag = 0
      cnt_max += 1

print(ans)