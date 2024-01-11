import heapq
import sys
input = sys.stdin.readline
heap = []

N = int(input())

for _ in range(N):
    now = int(input())
    if now == 0:
        if heap:
            print(-(heapq.heappop(heap)))
        else:
            print(0)
    else:
        heapq.heappush(heap,-now)