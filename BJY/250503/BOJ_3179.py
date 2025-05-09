## 평면 상 N개의 점이 있다.
## 여기서 3개의 점을 골라 삼각형을 만들때, 이 삼각형 안에 다른 점들이 최대로 들어가면
## 슈퍼 삼각형이라고 부른다.

## N(3<= N <= 300)
## xi,yi -> N개의 좌표

## 1. 완탐 -> 시간 초과

import itertools

def area(a,b,c):
  ## 신발끈 공식
  return abs((a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])) / 2)

N = int(input())
dots = []

for i in range(1,N+1):
  x,y = map(int,input().split())
  dots.append((i,(x,y))) 

max_cnt = 0
best_triangle = ()

for comb in itertools.combinations(dots,3):
  print(comb)
  idxs = [comb[0][0], comb[1][0], comb[2][0]]
  p1,p2,p3 = comb[0][1], comb[1][1], comb[2][1]
  S = area(p1,p2,p3)
  
  count = 0
  for dot in dots:
    p = dot[1]
    S1 = area(p,p2,p3)
    S2 = area(p1,p,p3)
    S3 = area(p1,p2,p)
    ## 오차 범위내에서 비교
    if abs(S - (S1+S2+S3)) < 1e-8:
      count += 1
  if count > max_cnt:
    max_cnt = count
    best_triangle = idxs


print(max_cnt)
print(' '.join(map(str,best_triangle)))


## 2. convex hull 을 사용한 풀이

import itertools

# 외적을 이용한 ccw (시계/반시계 방향 판별용)
def cross(a, b, c):
  return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

# 신발끈 공식으로 삼각형 면적 계산 * 2
def area(a, b, c):
  return abs(cross(a,b,c))

# Monotone Chain 방식으로 Convex Hull 구하기
def convex_hull(points):
  points = sorted(points, key=lambda p: (p[0], p[1]))  # (x, y, index)로 정렬

  lower = []
  for p in points:
    while len(lower) >= 2 and cross(lower[-2][:2], lower[-1][:2], p[:2]) <= 0:
      lower.pop()
    lower.append(p)

  upper = []
  for p in reversed(points):
    while len(upper) >= 2 and cross(upper[-2][:2], upper[-1][:2], p[:2]) <= 0:
      upper.pop()
    upper.append(p)

  return lower[:-1] + upper[:-1]

# 입력
N = int(input())
dots = []
for i in range(1, N + 1):
  x, y = map(int, input().split())
  dots.append((x, y, i))  # (x, y, index)

# Hull 계산
hull_points = convex_hull(dots)

max_cnt = 0
best_triangle = ()

# Hull 점들에서 3개 조합
for comb in itertools.combinations(hull_points, 3):
  p1, p2, p3 = comb[0][:2], comb[1][:2], comb[2][:2]
  idxs = [comb[0][2], comb[1][2], comb[2][2]]
  S  = area(p1,p2,p3)

  count = 0
  for px,py,_ in dots:
    S1 = area((px,py), p2, p3)
    S2 = area(p1, (px,py), p3)
    S3 = area(p1, p2, (px,py))
    if S == S1 + S2 + S3:
      count += 1

  if count > max_cnt:
    max_cnt = count
    best_triangle = idxs

print(max_cnt)
print(' '.join(map(str, best_triangle)))