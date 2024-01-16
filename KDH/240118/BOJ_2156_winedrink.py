n = int(input())
wine = [0]*(n+1)
dp = [0]*(n+1)
for i in range(1,n+1):
    a = int(input())
    wine[i] = a

if n == 1:
    print(wine[1])
elif n == 2:
    print(wine[1]+wine[2])
else:

    # print(wine,'wine')
    dp[1] = wine[1]
    # print(dp,1)
    dp[2] = wine[2] + wine[1]
    # print(dp,2)
    if n == 3:
        dp[3] = max(wine[3]+wine[2],wine[3]+dp[1],dp[3-1])
    # print(wine[3]+wine[3-1],'wine3+wine2')
    # print(wine[3]+dp[3-2],'wine3+dp1')
    # print(dp[2],'dp2')
    # print(dp,3)
    for i in range(3,n+1):
        # 2개전에 안먹고, 하나전에 안먹고, 지금 안먹는거 비교
        dp[i] = max(dp[i-3]+wine[i-1]+wine[i],wine[i]+dp[i-2],dp[i-1])
        # print(dp,i)
    print(dp[n])



