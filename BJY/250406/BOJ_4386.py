import math

n = int(input())

stars = []
edges = []
for i in range(n):
  x, y = map(float, input().split())
  stars.append((x,y))


## union-find
def find(parent,x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x]) 
  return parent[x]

def union(parent,a,b):
  a_root = find(parent,a)
  b_root = find(parent,b)
  if a_root != b_root:
    parent[b_root] = a_root

## 모든 두 별 사이의 거리 계산
for i in range(n):
  for j in range(i+1,n):
    x1,y1 = stars[i]
    x2,y2 = stars[j]
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    ## (거리, 별A,별B)
    edges.append((dist,i,j))

## 거리 기준 오름차순 정렬
edges.sort()

## 유니온 파인드용 parent 초기화
parent = [i for i in range(n)]

total = 0.0

## 크루스칼 알고리즘
for cost,a,b in edges:
  ## 두 부모가 다를떄(이어지지 않았을때만 연결) -> 사이클 방지
  if find(parent,a) != find(parent,b):
    union(parent,a,b)
    total += cost

## 소수 둘째자리까지 출력
print(f"{total:.2f}")