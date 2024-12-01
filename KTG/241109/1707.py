"""
이분그래프 개념 알기
"""
import sys
sys.setrecursionlimit(1000000)


def dfs(prev: int, group: int):
    # 방문 기록 남기기 (그룹 으로)
    visited[prev] = group
    # 연결된 지점 중 방문한 적 없다면 dfs, 같은 그룹 이라면 False
    for j in graph[prev]:
        if not visited[j]:
            nxt = dfs(j, -group)
            if not nxt:
                return False
        elif visited[j] == visited[prev]:
            return False
    # 연결된 점이 없거나 같은 그룹이 아니 라면 True
    return True


K = int(input())
for _ in range(K):
    # 입력
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    # 무향 그래프
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 모든 정점 에서 dfs
    result = False
    for i in range(1, V + 1):
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")
