import sys
sys.setrecursionlimit(10000) 

def DFS(node):
    for i in v[node]:
        if check[i] == 0:
            check[i] = check[node] + 1
            DFS(i)

N = int(input())
v = [[] for _ in range(N+1)]
s, e = map(int, input().split())
check = [0]*(N+1)
E = int(input())
for _ in range(E):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

DFS(s)

if check[e] > 0:
    print(check[e])
else:
    print(-1)