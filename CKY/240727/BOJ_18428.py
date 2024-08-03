import sys
import heapq

input = sys.stdin.readline

def dijkstra():
    queue = []


N, M = map(int,input().split())

for _ in range(M):
    S,E,C = map(int,input().split())