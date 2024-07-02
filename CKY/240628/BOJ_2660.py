from collections import deque
import sys

input = sys.stdin.readline

def BFS(start):
    queue = deque(start)
    visited[start[0]][start[1]] = True


N = int(input(()))

matrix = [ [0] * (N+1) for _ in range(N+1) ]
answer_list = []
while True:
    S, E = map(int,input().split())
    if S == -1 and E == -1:
        break
    else:
        matrix[S][E] = 1
        matrix[E][S] = 1

for i in range(1,N+1):
    for j in range(1,N+1):
        BFS((i,j))