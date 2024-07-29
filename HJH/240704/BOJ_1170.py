import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
# 현재 방문 순서
orders = []
# i 노드는 몇번째에 방문되었는가
orderIdx = [-2] * (n+1)
sets = []

def dfs(node: int, depth: int) -> bool:
    visited[node] = True
    orders.append(node)
    orderIdx[node] = depth
    for next in graph[node]:
        # 직전 노드 제외
        if orderIdx[next] == depth - 1:
            continue
        if visited[next]:
            sets.append(set(orders[orderIdx[next]:]))
        else:
            dfs(next, depth+1)
    orders.pop()


ans = 0
for start in range(1, n+1):
    if not visited[start]:
        orders = []
        orderIdx = [-2] * (n+1)
        sets = []
        dfs(start, 0)
        totalLen = 0
        totalSet = set()
        for s in sets:
            totalLen += len(s)
            totalSet = totalSet.union(s)
        if totalLen == len(totalSet):
            ans += 1
print(ans)
# 1. bfs 돌면서 사이클 검출 (직전 노드와 헷갈리면 안됨)
# 2. 검출한 사이클 set으로 저장
# {1 2 3} {3 4 5} -> 3 + 3 = 6
# {1 2 3 4 5} -> 5
# 3. 중복 발생! -> 선인장 아님