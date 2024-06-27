import sys
from collections import deque
sys.stdin = open("./1516.txt", 'r')


N = int(input())
pre = [[] for _ in range(N + 1)]
order = [0] * (N + 1)
times = [0] * (N + 1)
q = deque()

for j in range(1, N + 1):
    node = list(map(int, input().split()))
    times[j] = node[0]
    if len(node) == 2:
        q.append(j)
    for k in node[1:-1]:
        pre[k].append(j)
        order[j] += 1

ans = [0] * (N + 1)
while q:
    now: int = q.popleft()
    ans[now] += times[now]
    for nxt in pre[now]:
        order[nxt] -= 1
        ans[nxt] = max(ans[nxt], ans[now])
        if order[nxt] == 0:
            q.append(nxt)

for i in range(1, N + 1):
    print(ans[i])
