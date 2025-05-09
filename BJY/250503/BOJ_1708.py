## 첫째 줄에 점의 개수 N(3 ≤ N ≤ 100,000)이 주어진다. 
## 둘째 줄부터 N개의 줄에 걸쳐 각 점의 x좌표와 y좌표가 빈 칸을 사이에 두고 주어진다. 
## 주어지는 모든 점의 좌표는 다르다. x좌표와 y좌표의 범위는 절댓값 40,000을 넘지 않는다. 
## 입력으로 주어지는 다각형의 모든 점이 일직선을 이루는 경우는 없다.

N = int(input())
points = []
for i in range(N):
  x,y = map(int,input().split())
  points.append((x,y))
# print(points)

## 1. 정렬
points.sort()
print(points)

def cross(a,b,p):
  return (b[0]-a[0]) * (p[1]-a[1]) - (b[1]-a[1]) * (p[0]-a[0])

lower = []
for p in points:
  while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
    lower.pop()
  lower.append(p) 


print(lower)

upper = []
for p in reversed(points):
  while len(upper) >= 2 and cross(upper[-2], upper[-1],p) <= 0:
    upper.pop()
  upper.append(p)

print(upper)

## 첫/끝 중복 점 제외
convex_hull = lower[:-1] + upper[:-1]


print(len(convex_hull))