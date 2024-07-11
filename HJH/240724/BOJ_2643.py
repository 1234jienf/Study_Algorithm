n = int(input())

papers = []
for i in range(n):
    a, b = map(int, input().split())
    papers.append((max(a, b), min(a, b)))
papers.sort()

def containerable(a, b):
    return papers[b][1] >= papers[a][1] and papers[b][0] >= papers[a][0]

dp = [1] * n
ans = 1
for i in range(n-1):
    for j in range(i+1, n):
        if containerable(i, j):
            dp[j] = max(dp[j], dp[i] + 1)
            if dp[j] > ans:
                ans = dp[j]
print(ans)