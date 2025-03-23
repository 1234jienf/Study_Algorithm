## 소가 길을 건너간 이유6
## 존의 정사각형 목초지 N*N (2<= N <= 100)에서 인접한 목초지는 
## 자유롭게 건널수 있지만 그 중 일부는 길을 건너야한다.
## 농장의 바깥에는 높은 울타리가 있어서 소가 농장밖으로 나갈 일이 없다

## K마리의 ( 1<= K <= 100, K <= N2) 소가 농장에 있고, 각 소는
## 서로 다른 목초지에 있다. 
## 어떤 두소는 길을 건너지 않으면 못만남. 이런 소가 몇쌍인지 세어보자


# from itertools import combinations
from collections import deque

N,K,R = map(int,input().split())
## 길에 대한 행렬 R줄 
# tlst = []
# for _ in range(R):
#   r,c,r2,c2 = map(int,input().split())
#   tlst.append((r,c,r2,c2))
#   tlst.append((r2,c2,r,c))

roads = [[set() for _ in range(N+1)] for _ in range(N+1)]
for _ in range(R):
  r,c,r2,c2 = map(int,input().split())
  roads[r][c].add((r2,c2))
  roads[r2][c2].add((r,c))


cow = []
for _ in range(K):
  row, column = map(int,input().split())
  cow.append((row,column))

# comlst = list(combinations(cow,2))
# ans = 0
# for cows in comlst:
#   cow1,cow2 = cows[0],cows[1]
#   startR, startC = cow1[0],cow1[1]
#   endR, endC = cow2[0], cow2[1]
  
  
directions = [(-1,0),(1,0),(0,-1),(0,1)]
arr = [[0] * (N+1) for _ in range(N+1)]
cnt = 0
cowsinarr = [] ## 각 arr에 맞게 소가 있는 갯수

for i in range(1, N+1):
  for j in range(1,N+1):
    if arr[i][j] == 0:
      cnt += 1
      cowCNT = 0
      queue = deque([(i, j)])
      arr[i][j] = cnt
      if (i,j) in cow:
        cowCNT += 1
      while queue:
        r,c = queue.popleft()
        for dr,dc in directions:
          nr,nc = r+ dr, c+ dc
          if not (1<= nr <= N and 1<= nc <= N):
            continue 
          if arr[nr][nc] != 0:
            continue
          if (nr,nc) in roads[r][c]:
            continue
          arr[nr][nc] = cnt
          if (nr,nc) in cow:
            cowCNT += 1
          queue.append((nr,nc))
      cowsinarr.append(cowCNT)

# def bfs(start, end):
#   queue = deque([start])
#   visited = [[0] * (N+1) for _ in range(N+1)]
#   visited[start[0]][start[1]] = 1
#   directions = [(-1,0),(1,0),(0,-1),(0,1)]

#   while queue:
#     r,c = queue.popleft()
#     if (r,c) == end:
#       return True
#     for dr,dc in directions:
#       nr, nc = r + dr , r+ dc
#       if 1 <= nr <= N and 1 <= nc <= N and not visited[nr][nc]:
#         ## 만약 길이 있다면 건너지못함ㄴ
#         if (r,c,nr,nc) in tlst:
#           continue
#         visited[nr][nc] = True
#         queue.append((nr,nc))
#   return False

# ans = 0

# for cow1, cow2 in combinations(cow,2):
#   if not bfs(cow1,cow2):
#     ans += 1
# print(ans)

total = K * (K - 1) // 2

pairs = 0
for cnts in cowsinarr:
  pairs += cnts * (cnts -1) //2

print(total - pairs)