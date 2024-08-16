import sys

input = sys.stdin.readline

N, M = map(int,input().split())
K = int(input())
# 공사중인 도로 리스트
roads = []
# 도로 생성
matrix = [ [0] * (M+1) for _ in range(N+1) ]

for _ in range(K):
    roads.append(list(map(int,input().split())))
# x 부분 초기값 설정
for i in range(1,N+1):
    if [i-1,0,i,0] in roads or [i,0,i-1,0] in roads:
        break
    else:
        matrix[i][0] = 1
# y 부분 초기갑 설정
for i in range(1,M+1):
    if [0,i-1,0,i] in roads or [0,i,0,i-1] in roads:
        break
    else:
        matrix[0][i] = 1
# 도로를 탐색하면서 공사중인 부분에 포함됐는지 안됐는지 체크하여 둘다 공사중인 경우 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if ([i,j,i-1,j]  in roads or [i-1,j,i,j]  in roads) and ([i,j-1,i,j] in roads or [i,j,i,j-1] in roads):
            matrix[i][j] = 0
        # 위 왼쪽 막힌경우 안막힌쪽 값 더하기
        elif ([i,j-1,i,j] in roads or [i,j,i,j-1] in roads):
            matrix[i][j] = matrix[i-1][j]
        elif ([i-1,j,i,j] in roads or [i,j,i-1,j] in roads):
            matrix[i][j] = matrix[i][j-1]
        else:
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

print(matrix[-1][-1])