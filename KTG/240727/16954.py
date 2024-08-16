"""
bfs 를 돌며 탐색을 하되, 예외가 되는 상황을 모두 제거하도록 한다.

먼저, bfs 로 8방향으로 이동하는 경우 + 제자리에 있는 경우를 큐에 넣고
체스판을 벗어나는 경우, 벽이 있는 경우, 다음 번에 벽이 되는 경우를 제외시킨다.

이를 위해 벽의 위치를 저장하고, 다음 번에 벽이 되는 칸을 미리 계산해둔다.
=> 혹은 벽을 이동시키면서 제거해도 될 듯

방문 기록을 해야하는데, 해당 라인에 벽이 남아있을 때를 기준으로 해야하는지 고민중...

큐가 비었을 때 마지막칸에 도달하지 못했다면 0, bfs 도중에 마지막 칸에 도달하면 1을 출력한다.

!!왼쪽 아래에서 오른쪽위로 이동하므로 index에 주의할것
"""
import sys
from collections import deque
sys.stdin = open("./16954.txt", "r")

# 체스판 입력
arr = [list(input().strip()) for _ in range(8)]
# 방향 배열
direction = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
# 벽 정보
walls = []
for y in range(8):
    for x in range(8):
        if arr[y][x] == '#':
            walls.append((y, x))


# 벽의 위치를 갱신해주는 함수
def renew_wall():
    for i in range(len(walls)):
        walls[i] = (walls[i][0] + 1, walls[i][1])


# 다음 지점이 갈 수 있는 지점인지 확인하는 함수
def check_wall(y, x):
    if (y, x) in walls:
        return False
    for i in range(len(walls)):
        if (y, x) == (walls[i][0] + 1, walls[i][1]):
            return False
    return True


# bfs
def bfs(sy, sx, ey, ex):
    # bfs 초기 설정
    q = deque([(sy, sx)])
    # bfs를 한번 돈 후 벽의 위치를 갱신해 주는 함수를 호출
    while q:
        for i in range(len(q)):
            cy, cx = q.popleft()
            # 현재 지점에 벽이 있다면 패스
            if (cy, cx) in walls:
                continue
            # 한쪽 끝에 도달했다면 이미 벽이 다 내려간 후 이므로 성공
            if cy == ey or cx == ex:
                print(1)
                exit()
            # 다음 지점을 계산하여 벽이 있는지 확인 후 큐에 넣기
            for dy, dx in direction:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < 8 and 0 <= nx < 8 and check_wall(ny, nx):
                    q.append((ny, nx))
        # 다음 bfs 하기 전에 벽 갱신
        renew_wall()
    # 함수 종료 후 도달하지 못했다면 불가능
    else:
        print(0)


bfs(7, 0, 0, 7)
