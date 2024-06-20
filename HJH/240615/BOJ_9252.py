import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
# 음수 인덱스를 활용한다. 파이썬이기에 가능
for ai in range(len(a)):
    for bi in range(len(b)):
        if a[ai] == b[bi]:
            dp[ai][bi] = max(dp[ai][bi], dp[ai-1][bi-1] + 1)
        dp[ai][bi] = max(dp[ai][bi], dp[ai][bi-1])
        dp[ai][bi] = max(dp[ai][bi], dp[ai-1][bi])

ans = []
ai = len(a)-1
bi = len(b)-1
while ai >= 0 and bi >= 0:
    if a[ai] == b[bi] and dp[ai][bi] - 1 == dp[ai-1][bi-1]:
        ans.append(a[ai])
        ai -= 1
        bi -= 1
    elif dp[ai][bi] == dp[ai-1][bi]:
        ai -= 1
    elif dp[ai][bi] == dp[ai][bi-1]:
        bi -= 1

print(len(ans))
while ans:
    print(ans.pop(), end='')