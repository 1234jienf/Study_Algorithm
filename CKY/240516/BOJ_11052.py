N = int(input())
card_list = [0]
check_list = list(map(int,input().split()))

for check in check_list:
    card_list.append(check)

dp = [0] * (N+1)
dp[1] = card_list[1]*N
max_value = dp[1]
for i in range(2,N+1):
    dp[i] = max((N//i * card_list[i]) + (card_list[N%i]), dp[N-i] + card_list[i])
    print(dp)
    if dp[i] > max_value:
        max_value = dp[i]
print(max_value)