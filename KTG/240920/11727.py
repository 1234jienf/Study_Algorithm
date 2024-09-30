"""
DP 기본문제, 앞으로 매주 DP랑 시뮬레이션 난이도 올리면서 하나씩 낼 예정
"""
import sys
sys.stdin = open('./KTG/240920/11727.txt', 'r')

n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 3

if n < 3:
  print(dp[n])
  exit()
  
for i in range(3, n + 1):
  dp[i] = dp[i-2] * 2 + dp[i-1]
  
print(dp[n] % 10007)
