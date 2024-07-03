import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]
#순방향
for i in range(1, n+1):
    #역방향
    for j in range(1, n+1):
        if array[i-1] == array[-j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(n-dp[n][n])