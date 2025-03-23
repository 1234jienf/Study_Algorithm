## 자기 공보다 크기가 작고, 색이 다른 공을 잡을 수 있음

## N -> 공의 개수 (1<= N <= 200,000)
## i번째줄에는 i번째 공의 색을 나타내는 자연수 C와 크기를 나타내는 S
## ( 1<= C <= N, 1<= S <= 2,000)
## 서로 같은 크기 혹은 같은 색의 공이 있을 수 있다.

import sys

N = int(input())
INF = 200000
balls = []

for i in range(N):
  color, size = map(int, sys.stdin.readline().split())
  balls.append((size, color, i))

balls.sort()

color_count = [0] * (INF+1)

total = 0
j = 0
ans = [0] * (N+1)
for i in range(N):
  ## 공사이즈에 대한 조건
  while balls[j][0] < balls[i][0]:
    color_count[balls[j][1]] += balls[j][0]
    total += balls[j][0]
    j+= 1

    ans 