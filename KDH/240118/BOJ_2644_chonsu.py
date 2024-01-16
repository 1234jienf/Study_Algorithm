from collections import deque

n = int(input())
A,B = map(int, input().split())
m = int(input())

arr = [[] for _ in range(n+1)]
visited = [0]*(n+1)
q = deque()


for _ in range(m):
    P,S = map(int, input().split())
    arr[P].append(S)
    arr[S].append(P)

def bfs(x):
    q.append(x)
    while q:
        now = q.popleft()
        for i in arr[now]:
            if not visited[i]:
                visited[i] = visited[now] + 1
                q.append(i)


visited[A] = 1
bfs(A)
if visited[B] == 0:
    print(-1)
else:
    print(visited[B]-1)




