"""
최소 스패닝 트리 문제로, 신장 트리는 분할하여도 신장 트리라는 특성을 통해 풀 수 있음.
즉, 신장 트리를 만든 후, 가장 큰 비용의 간선을 끊어내면 가장 작은 비용의 두 노드 집합을 얻을 수 있음
최소 신장 트리를 얻는 방법은 두 가지가 있음.
 1) Union Find를 사용하는 크루스칼 알고리즘
 2) 그리디하게 풀어나가는 프림 알고리즘
 여기에서는 마지막에 가장 큰 비용의 간선을 끊으니 비용으로 정렬 후 진행하는 크루스칼 알고리즘을 사용하겠음.
"""
import sys
sys.stdin = open("./1647.txt", "r")


def find(x):
    if parent[x] != x:  # 부모가 본인이 아닌 경우, 부모를 찾아감.
        return find(parent[x])
    return x  # 본인일 경우 본인을 반환


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:  # 둘의 부모 중 더 낮은 값을 선택
        parent[x] = y
    else:
        parent[y] = x


# N: 노드 수, M: 간선 수, edges: 간선 정보
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
# 크루스칼 알고리즘을 사용하기 위해서 비용 순으로 정렬
edges.sort(key=lambda x: x[2])
# parent: 부모 노드 배열, total_cost: 신장 트리의 총 비용, final_cost: 가장 큰 비용
parent = [i for i in range(N + 1)]
total_cost = 0
final_cost = 0

for i, j, cost in edges:
    if find(i) != find(j):
        union(i, j)
        total_cost += cost
        final_cost = cost

ans = total_cost - final_cost
print(ans)
