n, m, k = map(int, input().split())

# dp[a][z]
dp = [[1] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if k > dp[n][m]:
    print(-1)
    exit(0)

ans = ''
def getAns(a, z, num):
    global dp, ans
    
    if a == 0:
        ans = ans + 'z' * z
        return
    if z == 0:
        ans = ans + 'a' * a
        return

    if dp[a-1][z] >= num:
        ans = ans + 'a'
        getAns(a-1,z,num)
    else:
        ans = ans + 'z'
        getAns(a,z-1,num-dp[a-1][z])

getAns(n, m, k)
print(ans)