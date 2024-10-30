from heapq import *
import sys
input = sys.stdin.readline

T = 0
n = 0
s = 0
t = None
v = None

def solution():
    global n, s, t, v
    # 시간순으로 정렬
    tv = [(t[i], v[i]) for i in range(len(t))]
    tv.sort()
    tvi = 0

    ans = 0
    pq = []
    # 계산할 때 필요한 것 : 현재시간, 제출시간, 점수
    while True:
        # 현재 시간에 제출할 수 있는 모든 과제를 더한다.
        while tvi < len(tv) and tv[tvi][0] <= s:
            heappush(pq, (-tv[tvi][1], tv[tvi][0]))
            tvi += 1

        # 없다면 현재 시간을 늘린 후 새로 추가.
        if not pq:
            if tvi >= len(tv):
                break
            s = tv[tvi][0]
            while tvi < len(tv) and tv[tvi][0] <= s:
                heappush(pq, (-tv[tvi][1], tv[tvi][0]))
                tvi += 1

        # 과제 하나를 처리 후 시간 ++
        score, time = heappop(pq)
        ans += (s - time) * score
        s += 1
    return -ans



if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, s = map(int, input().split())
        t = list(map(int, input().split()))
        v = list(map(int, input().split()))
        print(solution())