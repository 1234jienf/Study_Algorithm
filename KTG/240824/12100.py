from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 위, 오, 아, 왼쪽으로 밀었을 경우


def merge(direction: int, arr: list[list[int]]):
    # 0, 3은 정방향으로 / 1, 2은 역방향으로 검사
    ry, rx = [0, N, 1], [1, N, 1]
    if 0 < direction < 3:
        ry, rx = [N - 1, -1, -1], [N - 2, -1, -1]

    for y in range(*ry):
        last_val_y = 0
        if 0 < direction < 3:
            last_val_y = N - 1
        for x in range(*rx):
            # 0, 2는 x 축 먼저 / 1, 3은 y축 먼저 검사
            if direction % 2 != 0:
                cy, cx = y, x
            else:
                cy, cx = x, y

            # 0 인 경우 패스
            if arr[cy][cx] == 0: continue

            # 값을 저장하고 버림
            tmp = arr[cy][cx]
            arr[cy][cx] = 0

            # 저장한 값을 이전 값과 비교
            if direction % 2 == 0:
                if arr[last_val_y][cx] == 0:  # 이전 값이 0이라면 자리 옮김
                    arr[last_val_y][cx] = tmp
                elif arr[last_val_y][cx] == tmp:  # 이전 값과 같다면 합침
                    arr[last_val_y][cx] *= 2
                    if 0 < direction < 3:
                        last_val_y -= 1
                    else:
                        last_val_y += 1
                else:  # 이전 값과 같지 않다면 자리만 옮기고 다음 칸으로 이동
                    if 0 < direction < 3:
                        last_val_y -= 1
                    else:
                        last_val_y += 1
                    arr[last_val_y][cx] = tmp
            else:
                if arr[cy][last_val_y] == 0:  # 이전 값이 0이라면 자리 옮김
                    arr[cy][last_val_y] = tmp
                elif arr[cy][last_val_y] == tmp:  # 이전 값과 같다면 합침
                    arr[cy][last_val_y] *= 2
                    if 0 < direction < 3:
                        last_val_y -= 1
                    else:
                        last_val_y += 1
                else:  # 이전 값과 같지 않다면 자리만 옮기고 다음 칸으로 이동
                    if 0 < direction < 3:
                        last_val_y -= 1
                    else:
                        last_val_y += 1
                    arr[cy][last_val_y] = tmp

    return arr


def dfs(arr: list[list[int]], cnt: int):
    global ans
    if cnt == 5:
        for row in arr:
            for value in row:
                ans = max(ans, value)
        return

    for i in range(4):
        copy_arr = deepcopy(arr)
        dfs(merge(i, copy_arr), cnt + 1)


ans = 0
dfs(board, 0)
print(ans)
