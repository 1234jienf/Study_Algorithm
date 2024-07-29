"""
BFS를 이용한 문제...
문제를 잘못읽음... 마지막에 속도 1이어야하네?

그럼 우짠대...
점화식 세워보니 1, 1, 2, 2, 3, 3, 4, 4... 번이 지날 때 마다 움직임 횟수가 늘어남.
짝수번 마다 늘어나니 while 문과 %2 를 활용하여 작성
"""
import sys
sys.stdin = open("./1011.txt", "r")

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x
    cnt = 1  # 이번 차례 이동할 거리
    ans = 0  # 총 이동 횟수
    add = 0  # 총 이동한 거리
    while True:
        if add >= dist:
            break
        ans += 1
        add += cnt
        if add >= dist:
            break
        ans += 1
        add += cnt
        cnt += 1

    print(ans)

"""
from collections import deque


def bfs(s, e):
    q = deque([(s + 1, 1, 1)])
    v = {s, s + 1}

    while q:
        now, speed, time = q.popleft()

        if now == e:
            print(time)
            break

        for n_speed in [speed - 1, speed, speed + 1]:
            nxt = now + n_speed

            if nxt not in v:
                v.add(nxt)
                q.append((nxt, n_speed, time + 1))


T = int(input())

for t in range(T):
    x, y = map(int, input().split())

    bfs(x, y)
"""