import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
timeRequired = [-1] * (n+1)
time = [0] * (n+1)
graph = [[] for _ in range(n+1)]
prerequired = [set() for _ in range(n+1)]
q = deque()
for i in range(1, n+1):
    data = list(map(int, input().split()))
    timeRequired[i] = data[0]
    prerequired[i] = set(data[1:-1])
    if len(prerequired[i]) == 0:
        q.append(i)
    for j in range(1, len(data)-1):
        graph[data[j]].append(i)

while q:
    now = q.popleft()
    for next in graph[now]:
        prerequired[next].remove(now)
        if len(prerequired[next]) == 0:
            q.append(next)
        time[next] = max(time[next], time[now] + timeRequired[now])

for i in range(1, n+1):
    print(time[i] + timeRequired[i])