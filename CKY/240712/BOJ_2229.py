N = int(input())
age_list = list(map(int,input().split()))

dp = [0] * (N+1)

for i in range(1,N+1):
    for j in range(i-1,-1,-1):
        score = max(age_list[j:i]) - min(age_list[j:i])
        dp[i] = max(dp[j]+score, dp[i])
print(dp[-1])