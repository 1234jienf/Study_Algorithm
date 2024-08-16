n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [[0 for _ in range(100001)] for __ in range(n)]
MOD = 10000003

# 최대공약수
def gcd(a: int, b: int):
    return a if b == 0 else gcd(b, a % b)

for i in range(n):
    dp[i][arr[i]] = 1

for i in range(1, n):
    for j in range(1, 100001):
        dp[i][j] += dp[i - 1][j]
        dp[i][j] %= MOD

        tmp = gcd(arr[i], j)
        dp[i][tmp] += dp[i - 1][j]
        dp[i][tmp] %= MOD

print(dp[n-1][1])