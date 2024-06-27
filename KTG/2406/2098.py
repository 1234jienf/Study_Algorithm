import sys
sys.stdin = open("./2098.txt", "r")

N = int(input())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = {}


def solv(x, visited):
    if visited == (1 << N) - 1:
        if edges[x][0]:
            return edges[x][0]
        else:
            return int(1e9)

    if (x, visited) in dp:
        return dp[(x, visited)]

    cost = int(1e9)
    for i in range(1, N):
        if not edges[x][i] or visited & (1 << i):
            continue
        cost = min(cost, solv(i, visited | (1 << i)) + edges[x][i])

    dp[(x, visited)] = cost

    return dp[(x, visited)]


print(solv(0, 1))
