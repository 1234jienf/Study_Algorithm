N = int(input())
arr = [(list(map(int, input().split()))for _ in range(N))]
M_height = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] > M_height:
            M_height = arr[i][j]

for k in range(1,M_height):
    visited = [([0]*N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k:
                if not visited[i][j]:
                    

            


