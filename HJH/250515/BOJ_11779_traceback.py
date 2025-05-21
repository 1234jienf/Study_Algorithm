'''
역추적이 가능하도록 만들어 푼 파일

같은 원리로 인해서
1 4 3 2 가 있을때,
2 이전에 들른 곳이 어딘지만 저장을 해주면 된다.

편의상 1 4 3 2로 고친 예를 보여주면
last라는 배열에 [0, 0, 3, 4, 1]를 저장해준다.
이제 역추적 해주면 그것이 루트가 된다.
last[2] = 3
last[3] = 4
last[4] = 1
last[1] = 0 (존재하지 않는 노드인 0에 도달하면 끝으로 생각하자)

방문보다 저장이 빠를 것이라 생각했지만 저장하는 데 드는 시간 때문인지 더 오래걸렸다.
루트를 여러번 찾아야 되는 경우에는 저장이 더 빠를 것이라고 생각한다...
'''
import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())
dist = [float('inf')] * (n + 1)
dist[start] = 0
last = [0] * (n + 1)
h = []
heappush(h, (0, start))
while h:
    d, x = heappop(h)
    if dist[x] < d:
        continue
    for y, c in graph[x]:
        if dist[y] > d + c:
            dist[y] = d + c
            last[y] = x
            heappush(h, (dist[y], y))
path = []
now = end
while now:
    path.append(now)
    now = last[now]

print(dist[end])
print(len(path))
print(*path[::-1])