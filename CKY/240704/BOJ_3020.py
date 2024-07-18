import sys

input = sys.stdin.readline

N,H = map(int,input().split())

cave = []

for i in range(N):
    if i % 2 == 0:
        cave.append(int(input()))
    else:
        cave.append(-int(input()))

answer = [() for _ in range(H+1)]

for i in range(H,0,-1):
    