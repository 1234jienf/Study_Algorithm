"""
대표적인 DFS 백트래킹 문제로, 사선으로 그룹을 엮어 DFS를 순회하며 최대 경우를 찾는 문제임.
시간 초과를 해결하기 위해 백트래킹은 물론, 문제를 분할하여 생각할 수 있어야 함.
"""
import sys
sys.stdin = open("./1799.txt", "r")


def dfs(n, cnt):
    global ans  # cnt + L - n
    if ans >= (cnt + (L+1 - n)//2):  # 더 진행해도 정답일 가능성이 없는 경우
        return

    if n >= L:  # 종료 조건
        ans = max(ans, cnt)
        return

    for ci, cj in lst[n]:
        if v[ci - cj] == 0:  # 오른쪽 아래 방향에 방문한 적이 없다면 방문
            v[ci - cj] = 1
            dfs(n + 2, cnt + 1)
            v[ci - cj] = 0
    dfs(n + 2, cnt)  # 해당 노드를 방문하지 않고 넘어가는 경우


# N: 체스판 크기, arr: 체스판
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 대각선 방향으로 그룹화 하기
lst = [[] for _ in range(2*N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] != 1:  # 놓을 수 없는 위치는 continue
            continue
        lst[i + j].append((i, j))  # 오른쪽 위 방향 사선을 집합으로 묶음

L = 2*N - 1
v = [0] * (2*N)
ans = 0
dfs(0, 0)
t = ans
ans = 0
dfs(1, 0)
print(t + ans)
