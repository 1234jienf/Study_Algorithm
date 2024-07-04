"""
지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!
미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부,
그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.
지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다.
불은 각 지점에서 네 방향으로 확산된다.
지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.
지훈이와 불은 벽이 있는 공간은 통과하지 못한다.

입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다.
단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.
다음 입력으로 R줄동안 각각의 미로 행이 주어진다.
각각의 문자들은 다음을 뜻한다.
    #: 벽
    .: 지나갈 수 있는 공간
    J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
    F: 불이 난 공간
J는 입력에서 하나만 주어진다.

지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.
지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.
"""
import sys
sys.stdin = open("./4179.txt", "r")
from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 입력
R, C = map(int, input().split())         # 행, 열
arr = [list(input()) for _ in range(R)]  # 배열
jr, jc = 0, 0                            # 지훈의 위치
F = []                                   # 불의 위치
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'J':
            jr, jc = r, c
        elif arr[r][c] == 'F':
            F.append((r, c))


q = deque()                     # 큐
q.append((jr, jc, 1))           # row, column, isJ
if len(F) != 0:
    for fr, fc in F:
        q.append((fr, fc, 0))
        arr[fr][fc] = '#'

# BFS => 지훈 먼저 이동, 이미 불이 번진 곳은 벽과 동일
while q:
    cr, cc, isJ = q.popleft()
    if isJ and (cr == 0 or cc == 0 or cr == R - 1 or cc == C - 1):
        if arr[cr][cc] == '#':
            continue
        print(len(arr[cr][cc]))
        break
    for dr, dc in direction:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < R and 0 <= nc < C:
            if arr[nr][nc] != '#' and not isJ:
                arr[nr][nc] = '#'
                q.append((nr, nc, 0))
            elif arr[nr][nc] == '.' and isJ and arr[nr][nc] != '#':
                arr[nr][nc] = arr[cr][cc] + 'J'
                q.append((nr, nc, 1))
else:
    print('IMPOSSIBLE')

