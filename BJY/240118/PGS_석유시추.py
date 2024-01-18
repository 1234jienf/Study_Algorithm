# 문제
## 세로길이가 n, 가로길이가 m인 격자 모양의 땅 속에서 석유가 발견
# from collections import deque

# def solution(land):
#     width = len(land)
#     depth = len(land[0])
    
#     dx = [0,1,-1,0]
#     dy = [1,0,0,-1]

#     visited = [[0] * (width) for _ in range(depth)]
#     result = [0 for _ in range(width)]
#     def bfs(cx,cy):
#         min_x, max_x = depth,0
#         num = 0
#         visited[cx][cy] = 1
#         q = deque()
#         q.append((cx,cy))
#         while q:
#             cx,cy = q.popleft()
#             min_x = min(min_x, cx)
#             max_x = max(max_x, cx)
#             num += 1
#             for i in range(4):
#                 nx = cx + dx[i]
#                 ny = cy + dy[i]
#                 if 0 <= nx  < width and  0 <= nx < depth and not visited[nx][ny] and land[nx][ny]:
#                     visited[nx][ny] = 1
#                     q.append((nx,ny))
                    
#         for i in range(min_x, max_x+1):
#             result[i] += num


#     for i in range(width):
#         for j in range(depth):
#             if land[i][j] == 1 and not visited[i][j]:
#                 bfs(i,j) 
                
#     answer = max(result)
#     return answer


from collections import deque
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    result = [0 for i in range(m+1)]
    visited = [[0 for i in range(m)] for j in range(n)]
    def bfs(a, b):
        count = 0
        visited[a][b] = 1
        q = deque()
        q.append((a,b))
        min_y, max_y = b, b
        while q:
            x,y = q.popleft()
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            count += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
        
        for i in range(min_y, max_y+1):
            result[i] += count
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i,j)
    answer = max(result)
    return answer