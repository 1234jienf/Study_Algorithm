import sys

input = sys.stdin.readline

N = int(input())
work_list = []

dp = [0] * (N+1)
for _ in range(N):
    work_list.append(list(map(int,input().split())))

dp[1] = work_list[0][1]

for i in range(1,N+1):
     

print(dp)