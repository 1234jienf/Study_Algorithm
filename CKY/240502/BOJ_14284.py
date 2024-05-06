import sys
import heapq

input = sys.stdin.readline



N, M = map(int,input().split())

matrix = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    S,E,W = map(int,input().split())
    matrix[S][E] = W
    matrix[E][S] = W

S,T = map(int,input().split())