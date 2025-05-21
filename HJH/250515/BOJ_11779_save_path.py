'''
경로를 저장하는 방식으로 푼 파일

다익스트라에서
1-2경로 : 1 2
1-3경로 : 1 4 3
일 때
1 -> 2 보다 1 -> 3 -> 2가 빠르다는 것을 검사했다면
이는 1 4 3 2 루트를 통한다는 뜻이 된다.

최대 문자열 길이
"1 2 3 ... 1000"
을 1000개 가지고 있다고 하더라도
3mb정도밖에 차지하지 않음을 알고 시도해 본 방식이다.
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
route = [str(i) for i in range(n + 1)]
r_count = [1] * (n + 1)
fixed = [False] * (n + 1)
h = []
heappush(h, (0, start))
while h:
    d, now = heappop(h)
    if fixed[now]:
        continue
    fixed[now] = True
    for next, cost in graph[now]:
        if dist[next] > d + cost:
            dist[next] = d + cost
            route[next] = route[now] + " " + str(next)
            r_count[next] = r_count[now] + 1
            heappush(h, (dist[next], next))
print(dist[end])
print(r_count[end])
print(route[end])