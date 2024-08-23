import sys
from collections import deque
input = sys.stdin.readline

n = 0
graph = None
used = None

def degree(i: int) -> int:
    return sum(graph[i]) + graph[i][i]

def oddDegree(node: int) -> bool:
    return degree(node) % 2 == 1

def removeOddPair(node: int, visited: list) -> int:
    
    if not oddDegree(node):
        return longestPath(i)
    if visited[node]:
        return 0
    else:
        visited[node] = True
    
    res = 0
    for next in range(7):
        if graph[node][next] > 0 and node != next and not visited[next]:
            graph[node][next] -= 1
            graph[next][node] -= 1
            temp = removeOddPair(next, visited)
            graph[node][next] += 1
            graph[next][node] += 1
            if temp > res:
                res = temp
    return res

def dfs(node: int, visited: list):
    visited[node] = True
    for next in range(7):
        if graph[node][next] > 0 and not visited[next]:
            dfs(next, visited)

def longestPath(node: int) -> int:
    oddCount = 0
    totDegrees = 0
    visited = [False] * 7

    dfs(node, visited)
    for i in range(7):
        if visited[i]:
            used[i] = True
            if oddDegree(i): oddCount += 1
            totDegrees += degree(i)

    if oddCount <= 2:
        return totDegrees // 2
    else:
        res = 0
        for j in range(7):
            if oddDegree(j):
                visited = [False] * 7
                temp = removeOddPair(j, visited)
                if temp > res: res = temp
    return res


while True:
    line = input()
    if line == '':
        break

    n = int(line)
    graph = [[0 for _ in range(7)] for __ in range(7)]
    for i in range(n):
        a, b = map(int, input().split())
        graph[a][b] += 1
        if a != b: graph[b][a] += 1

    used = [False] * 7
    ans = 0
    for i in range(7):
        if not used[i]:
            length = longestPath(i)
            if length > ans: ans = length
    
    print(ans)