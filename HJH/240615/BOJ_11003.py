import sys
from heapq import *
input = sys.stdin.readline

n, l = map(int, input().split())
d = list(map(int, input().split()))
pq = []

counter = {}
ans = ''

for i in range(l):
    num = d[i]
    if num in counter.keys():
        counter[num] += 1
    else:
        counter[num] = 1
        heappush(pq, num)
    print(pq[0], end=' ')

for i in range(l, n):
    num = d[i]
    if num not in counter.keys() or counter[num] == 0:
        counter[num] = 1
        heappush(pq, num)
    else:
        counter[num] += 1
    subNum = d[i-l]
    counter[subNum] -= 1
    while counter[pq[0]] == 0:
        heappop(pq)
    print(pq[0], end=' ')