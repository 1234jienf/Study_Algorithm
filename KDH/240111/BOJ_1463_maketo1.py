N = int(input())
DP = [0,0,1,1]
for i in range(4, N+1):
    ans = []
    if i % 3 == 0:
        ans.append(DP[i//3])
    if i % 2 == 0:
        ans.append(DP[i//2])
    ans.append(DP[i-1])
    DP.append(min(ans)+1)
print(DP[N])
