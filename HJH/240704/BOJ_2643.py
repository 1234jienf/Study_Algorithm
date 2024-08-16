n = int(input())

papers = []
for i in range(n):
    a, b = map(int, input().split())
    papers.append((max(a, b), min(a, b)))
papers.sort()

def containerable(a, b):
    return papers[b][1] >= papers[a][1] and papers[b][0] >= papers[a][0]

# dp[i] = i 번쨰 색종이가 최고 높은 색종이 일 때, 최대 색종이 갯수
dp = [1] * n
ans = 1
for i in range(n-1):
    for j in range(i+1, n):
        if containerable(i, j):
            dp[j] = max(dp[j], dp[i] + 1)
            if dp[j] > ans:
                ans = dp[j]
print(ans)