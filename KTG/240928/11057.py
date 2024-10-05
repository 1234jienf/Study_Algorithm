import sys
sys.stdin = open('./KTG/240928/11057.txt')

n = int(input())
dp = [1] * 10

for i in range(n):
  for j in range(1, 10):
    dp[j] += dp[j - 1]
  
print(dp[9] % 10007)
