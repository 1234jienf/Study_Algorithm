"""
수업시간을 연결해보자!

이전 수업이 끝난 시간에 가장 가까운 시간을 선택하고 연결, 방문기록을 남기자!
모든 수업이 사라질 때 까지 하면 끝! => 카운트 한번이 끝나면 강의실 갯수 + 1
=> 이러면 최악의 경우 시간복잡도가 N^2

힙을 이용하여 탐색 시간을 줄여보자
"""
import sys
sys.stdin = open("./11000.txt", "r")
import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[0], x[1]))

pq = [arr[0][1]]
for i in range(1, N):
    si, ti = arr[i]
    if pq[0] <= si:
        heapq.heappop(pq)
    heapq.heappush(pq, ti)

print(len(pq))

"""
s1 e1
hq: e1
s2 e2
hq: e1 e2
s3 e3
s3 <= e1
hq: e3 e2
"""