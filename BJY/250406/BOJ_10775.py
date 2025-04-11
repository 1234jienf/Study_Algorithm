import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline  
## 게이트의 수 G  (1 ≤ G ≤ 10^^5)
G = int(input())
## 비행기의 수 P (1 ≤ P ≤ 10^^5)
P = int(input())

## parent 설정 = [0,1,2,3,4,5]
parent = [i for i in range(G+1)]

def find(x):
  if parent[x] != x:
    ## 경로 압축
    parent[x] = find(parent[x])
  return parent[x]

def union(a,b):
  a = find(a)
  b = find(b)
  parent[a] = b

cnt = 0
for i in range(P): 
  num = int(input())
  docking_gate = find(num)
  if docking_gate == 0:
    ## 도킹 불가
    break
  ## 만약 도킹이 되었다면, 도킹된 구역의 parent를 앞의 게이트로 바꿔주어 
  ## 탐색할때 건너뛰게 하기
  union(docking_gate, docking_gate -1)
  cnt += 1

print(cnt)