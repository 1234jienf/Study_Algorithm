INF = 10000 * 20 + 1
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
done = 1 << n
done -= 1

dp = [INF for _ in range(done+1)]
dp[0] = 0

# n 번째 사람까지, works의 일을 한 경우
def getDP(pi, works):
    global n, dp, costs
    if dp[works] != INF:
        return dp[works]
    for i in range(n):
        mask = 1 << i
        before = 0
        if works & mask != 0:
            before = getDP(pi - 1, works & ~mask)
        else:
            continue
        before += costs[pi-1][i]
        if before < dp[works]:
            dp[works] = before
    return dp[works]


print(getDP(n, done))
print(dp)