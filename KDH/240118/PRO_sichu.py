n = 5
m = 8

def find(y,x):
    visited = [[0]*m for _ in range(n)]
    cnt = 1
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= ny < m and 0 <= nx < n:
            if arr[nx][ny] == 1:
                if not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = 1
                    find[ny][nx]
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 1:
                visited[i][j] == cnt


            
            


def solution(land):
    n = 5
    m = 8
    arr = land
    for i in range(n):
        for j in  range(m):
            if arr[i][j] == 1:
                find(i,j)
    for i in range(m):
        


    answer = 
    return answer