# 문제
## 세로길이가 n, 가로길이가 m인 격자 모양의 땅 속에서 석유가 발견
from collections import deque

def solution(land):
    row = len(land)
    depth = len(land[0])
    
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]

    def bfs(cx,cy,num):
        
    for i in range(row):
        for j in range(depth):
            if land[i][j] == 1:
                land[i][j]  
    answer = 0
    return answer