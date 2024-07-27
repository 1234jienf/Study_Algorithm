import sys
sys.stdin = open("./1577.txt", "r")

N, M = map(int, input().split())
K = int(input())
arr = [list(map(int, input().split())) for _ in range(K)]
v = [[0] * N for _ in range(M)]
v[0][0] = 1
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 0
stack = [()]


print(cnt)