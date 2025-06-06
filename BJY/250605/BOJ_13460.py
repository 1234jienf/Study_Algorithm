# 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

# 보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 
# 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 
# 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.

# 이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 
# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

# 각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 
# 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 
# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

# 보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

## 첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 
## 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. 
# '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다. 
# 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.

# 입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 
# 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 
# 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.
from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy):
    count = 0
    # 현재 위치가 'O'인지 먼저 확인
    if board[x][y] == 'O':
        return x, y, count
    # 다음 칸이 벽이거나 현재 칸이 구멍일 때까지 이동
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
        if board[x][y] == 'O':
            break
    return x, y, count

def solution():
    # 초기 구슬 위치 찾기
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
                board[i][j] = '.'
            elif board[i][j] == 'B':
                bx, by = i, j
                board[i][j] = '.'
    
    # 방문 체크를 위한 set
    visited = set()
    visited.add((rx, ry, bx, by))
    
    q = deque()
    q.append((rx, ry, bx, by, 0))
    
    while q:
        rx, ry, bx, by, count = q.popleft()
        
        if count >= 10:
            break
            
        for i in range(4):
            # 빨간 구슬과 파란 구슬 이동
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            
            # 파란 구슬이 구멍에 빠졌다면 실패
            if board[nbx][nby] == 'O':
                continue
                
            # 빨간 구슬만 구멍에 빠졌다면 성공
            if board[nrx][nry] == 'O':
                return count + 1
            
            # 두 구슬이 같은 위치에 있다면
            if nrx == nbx and nry == nby:
                # 이동 거리가 더 큰 구슬이 한 칸 뒤로
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            # R**B** -> ****RB
            # GOOD ~
            # UNDERSTAND??
            # OKAY BYE BYE
            
            # 새로운 상태라면 큐에 추가
            new_state = (nrx, nry, nbx, nby)
            if new_state not in visited:
                visited.add(new_state)
                q.append((nrx, nry, nbx, nby, count + 1))
    
    return -1

print(solution())