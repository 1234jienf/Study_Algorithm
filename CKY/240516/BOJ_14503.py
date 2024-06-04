def directionChange(dir):
    if dir == 0:
        return 3
    elif dir == 1:
        return 0
    elif dir == 2:
        return 1
    elif dir == 3:
        return 2
    
def DFS(start):
    global cnt
    if matrix[start[0]][start[1]] == 0:
        cnt += 1
        matrix[start[0]][start[1]] = 1
    stack = [start]

    while stack:
        y, x = stack.pop()
        for k in range(4):
            dy = y + direction[k][0]
            dx = x + direction[k][1]
            if 0 <= dy < M and 0 <= dx < N:

direction = [(0,-1), (-1,0), (0,1), (1,0)]

N, M = map(int,input().split())

x, y, d = map(int,input().split())

matrix = [ list(map(int,input().split())) for _ in range(M) ]

cnt = 0