"""
테트리스 같은 것. 아래 자리 없으면, 가능한 왼쪽 혹은 오른쪽으로 굴러서 아래로 내려감
출구를 통해서 주변 골램으로 이동. 최대한 아래로 내려갈 것
"""
import sys
sys.stdin = open('./KTG/240913/CT_magic_forest.txt', 'r')


def canDown():
  global pos
  y, x = pos;
  for dy, dx in down:
    ny, nx = y + dy, x + dx
    if board[ny][nx] == 1:
      break
  else:
    pos = [y + 1, x]
    return True
  return False


def canLeft():
  return


def canRight():
  return


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
    if canDown():
      continue
    elif canLeft():
      continue
    elif canRight():
      continue
    else:
      y, x = pos
      board[y][x] = 1
      for dy, dx in direction:
        ny, nx = y + dy, x + dx
        board[ny][nx] = 1
      break
  print(board)
  
  
