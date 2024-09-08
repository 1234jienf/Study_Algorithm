import sys
sys.stdin = open('./12100.txt', 'r')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 위, 오, 아, 왼쪽으로 밀었을 경우


def merge(direction: int, arr: list[list[int]]):
    # 0, 3은 정방향으로 / 1, 2은 역방향으로 검사
    ran = [0, N, 1]
    if direction in [1, 2]:
        ran = [N - 1, -1, -1]

    for y in range(*ran):
        for x in range(*ran):
            # 0, 2는 x 축 먼저 / 1, 3은 y축 먼저 검사
            if direction % 2 == 0:
                cy, cx = y, x

            else:
                cy, cx = x, y

            # 0 인 경우 패스
            if arr[cy][cx] == 0: continue

            dy, dx = directions[direction]
            ny, nx = cy + dy, cx + dx

            # 범위 밖 패스
            if ny < 0 or ny >= N or nx < 0 or nx >= N: continue

            # 합치기
            if arr[cy][cx] == arr[ny][nx]:
                arr[cy][cx] *= 2
                arr[ny][nx] = 0

    print(arr)
    # 모두 합친 후 움직이기
    return move(direction, arr)


def move(direction: int, arr: list[list[int]]):
    # 0, 3의 경우 세로로 검사 / 1, 2의 경우 가로로 검사
    targets = arr
    if direction in [0, 2]:
        targets = list(zip(*arr))

    new_arr = []
    for target in targets:
        non_zeros = [x for x in target if x != 0]
        zero_cnt = len(target) - len(non_zeros)
        if direction in [1, 2]:
            new_target = [0] * zero_cnt + non_zeros
        else:
            new_target = non_zeros + [0] * zero_cnt
        new_arr.append(new_target)

    if direction in [0, 2]:
        new_zip_arr = zip(*new_arr)
        return [list(item) for item in new_zip_arr]
    return new_arr


def dfs(arr: list[list[int]], cnt: int):
    global ans
    if cnt == 5:
        for row in arr:
            for value in row:
                ans = max(ans, value)
        return

    for i in range(4):
        dfs(merge(i, arr), cnt + 1)


ans = 0
dfs(board, 0)
print(ans)
