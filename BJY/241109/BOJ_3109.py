import sys
N, M = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(list(input()))


# 오른쪽 위, 오른쪽, 오른쪽 아래
dx = [-1, 0, 1]
dy = [1, 1, 1]


def pipe(x, y):
  global result
  # 방문 표시
  arr[x][y] = 'o'
  # 마지막 열에 도달한 경우
  if y == M-1:
    # 파이프라인 연결 완료
    result += 1
    return True
  for k in range(3):
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < N and 0 <= ny < M:
      # 건물도 아니고, 방문한 칸도 아님
      if arr[nx][ny] != 'x' and arr[nx][ny] != 'o':
        if pipe(nx, ny):
          return True


result = 0
for i in range(N):
  pipe(i, 0)
print(result)