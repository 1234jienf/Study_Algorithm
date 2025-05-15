from collections import deque
import sys
sys.setrecursionlimit(100010)

n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(1, n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [0 for _ in range(n+1)]

def dfs(parent, node) -> int:
    cnt = 1
    for next_node in graph[node]:
        if next_node == parent:
            continue
        cnt += dfs(node, next_node)
    dp[node] = cnt
    return cnt

dfs(0, r)

for _ in range(q):
    print(dp[int(input())])