"""
문제)
숫자가 써있는 보드에 동전을 놓고 숫자만큼 한쪽 방향으로 움직인다.
구멍에 떨어지거나 바닥에 떨어지지 않고 최대한 많이 움직일 수 있는 경우를 계산한다.

해설)
반복문으로 보드를 돌면서 현재 움직인 횟수를 기록한다.
해당 칸이 현재 움직인 횟수보다 적은 경우에만 계속 진행한다.
최종적으로 모든 보드 칸에서 최댓값을 출력한다.
"""
import sys
sys.stdin = open("./1103.txt", "r")


def dfs(cy, cx, t):
    global ans
    ans = max(t, ans)
    # 현재 칸의 번호
    cn = int(board[cy][cx])
    for dy, dx in directions:
        # 다음 칸의 좌표
        ny, nx = cy + dy * cn, cx + dx * cn
        # 보드를 벗어나거나 구멍이면 취소
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if board[ny][nx] == 'H':
            continue
        if dp[ny][nx] >= t + 1:
            continue
        # 종료 조건
        if visited[ny][nx]:
            print(-1)
            exit()
        # 방문 기록
        dp[ny][nx] = t + 1
        visited[ny][nx] = 1
        dfs(ny, nx, t + 1)
        visited[ny][nx] = 0


# 입력
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
# 필요 값들
dp = [[0] * M for _ in range(N)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = 0
# dfs 초기 조건
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
dfs(0, 0, 1)
print(ans)
