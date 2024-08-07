import sys
from collections import deque
# 시계 방향 회전
def right(target):
    check = matrix[target].pop()
    matrix[target].appendleft(check)
# 반시계 방향 회전
def left(target):
    check = matrix[target].popleft()
    matrix[target].append(check)
# 연결된 톱니바퀴 체크
def DFS(start,dir):
    # 방문처리를 통해 연결된 톱니바퀴 회전
    visited = [0,0,0,0]
    visited[start-1] = 1
    # 첫 톱니바퀴 회전
    if dir == -1:
        left(start-1)
    else:
        right(start-1)
    queue = deque([start-1])
    # 연결된 톱니바퀴 중 극이 다른 톱니바퀴 회전 시킴
    while queue:
        next = queue.popleft()
        if next != start-1:
            if next%2 != (start-1)%2:
                if dir == -1:
                    right(next)
                else:
                    left(next)
            else:
                if dir == -1:
                    left(next)
                else:
                    right(next)
        for k in range(4):
            if flag[next][k] == 1 and visited[k] == 0:
                visited[k] = 1
                queue.append(k)

input = sys.stdin.readline

matrix = [deque(list(map(int,input().strip()))) for _ in range(4)]

K = int(input())

for _ in range(K):
    number, direction = map(int,input().split())
    flag = [[0,0,0,0] for _ in range(4)]
    # 처음 톱니바퀴들의 상태를 돌며 극이 다른 톱니바퀴들을 flag 라는 2차원 배열로 체크
    for i in range(4):
        if i == 0:
            if matrix[i][2] != matrix[i+1][6]:
                flag[i][i+1] = 1
        elif i == 3:
            if matrix[i][6] != matrix[i-1][2]:
                flag[i][i-1] = 1
        else:
            if matrix[i][2] != matrix[i+1][6]:
                flag[i][i+1] = 1
            
            if matrix[i][6] != matrix[i-1][2]:
                flag[i][i-1] = 1
    
    DFS(number,direction)
# 정답을 계산할 반복문
answer = 0
for k in range(4):
    # S극의 경우 2**n 으로 점수를 계산
    if matrix[k][0] == 1:
        answer += 2**k
print(answer)