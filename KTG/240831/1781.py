"""
그리디 알고리즘으로, 현재 시간까지 최대한의 컵라면을 챙기는 식이다.

일단 시간으로 정렬한 후, 힙에 컵라면을 넣는다.
길이(시간)이 이미 데드라인(i[0])을 넘긴 경우 가장 컵라면이 적은걸 버린다.
"""
import sys
import heapq
sys.stdin = open('1781.txt', 'r')

n = int(input())
array = [list(map(int, input().split()))]

array.sort()

pq = []

for i in array:
    heapq.heappush(pq, i[1])
    if i[0] < len(pq):
        heapq.heappop(pq)

print(sum(pq))
