"""
테트리스 같은 것. 아래 자리 없으면, 가능한 왼쪽 혹은 오른쪽으로 굴러서 아래로 내려감
출구를 통해서 주변 골램으로 이동. 최대한 아래로 내려갈 것
"""
import sys
sys.stdin = open('./KTG/240913/CT_magic_forest.txt', 'r')

R, C, K = map(int, input().split())
unit = [list(map(int, input().split())) for _ in range(K)]
arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
exit_set = set()

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj):
  q = []
  v = [[0] * (C+2) for _ in range(R+4)]
  mx_i = 0
  
  q.append((si, sj))
  v[si][sj] = 1
  
  while q:
    ci, cj = q.pop(0)
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      ni, nj = ci+di, cj+dj
      if v[ni][nj] == 0 and (arr[ci][cj] == arr[ni][nj] or ((ci, cj) in exit_set and arr[ni][nj] > 1)):
        q.append((ni, nj))
        v[ni][nj] = 1
        mx_i = max(mx_i, ni)
  
  return mx_i - 2


ans = 0
num = 2
for cj, dr in unit:
  ci = 1
  while True:
    if arr[ci+1][cj-1] + arr[ci+2][cj] + arr[ci+1][cj+1] == 0:
      ci += 1
    elif arr[ci-1][cj-1] + arr[ci][cj-2] + arr[ci+1][cj-1] + arr[ci+1][cj-2] + arr[ci+2][cj-1] == 0:
      ci += 1
      cj -= 1
      dr = (dr-1)%4
    elif arr[ci-1][cj+1] + arr[ci][cj+2] + arr[ci+1][cj+1] + arr[ci+1][cj+2] + arr[ci+2][cj+1] == 0:
      ci += 1
      cj += 1
      dr = (dr+1)%4
    else:
      break
    
  if ci < 4:
    arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
    exit_set = set()
    num = 2
  else:
    arr[ci+1][cj]=arr[ci-1][cj]=num
    arr[ci][cj-1:cj+2]=[num]*3
    num += 1

    exit_set.add((ci+di[dr], cj+dj[dr]))
    
    ans += bfs(ci, cj)
    
print(ans)
    
"""
def canMove(dir: list[list[int, int]], turn: int):
  global pos, d
  y, x = pos;
  for dy, dx in dir:
    ny, nx = y + dy, x + dx
    if ny <= 0 or C + 2 < ny or nx <= 0 or R + 2 < nx:
      break
    if board[ny][nx] > 0:
      break
  else:
    pos = [y + 1, x]
    d = (d + turn) % 4
    return True
  return False


direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
down = [[2, 0], [1, -1], [1, 1]]
left = [[0, -2], [-1, -1], [1, -1]]
right = [[0, 2], [-1, 1], [1, 1]]
R, C, K = map(int, input().split())

board =  [[1] + [0 for _ in range(C)] + [1] for _ in range(R + 1)] + [[1 for _ in range(C + 2)]]

for k in range(K):
  c, d = map(int, input().split())
  pos = [0, c]
  while True:
    if canMove(down, 0):
      continue
    elif canMove(left, -1):
      continue
    elif canMove(right, 1):
      continue
    else:
      y, x = pos
      if 0 < y < R + 1:  
        board[y][x] = 1
        for dy, dx in direction:
          ny, nx = y + dy, x + dx
          board[ny][nx] = 1
        dy, dx = direction[d]
        ny, nx = y + dy, x + dx
        board[ny][nx] += 1
      break
    
  pprint.pprint(board)
"""