mod = 1000000000
mask = 1 << 10

# dp[자리수][맨 앞 자리 수][visited]
# 최대 40 * 10 * 1023 = 409200
def solution(num):
    dp = [[[0 for _ in range(mask)] for _ in range(10)] for _ in range(num+1)]
    for i in range(10):
        dp[1][i][1<<i] = 1
    
    for j in range(1, num):
        for f in range(10):
            for v in range(mask):
                if f != 0:
                    dp[j+1][f-1][v|(1<<(f-1))] += dp[j][f][v]
                    dp[j+1][f-1][v|(1<<(f-1))] %= mod
                if f != 9:
                    dp[j+1][f+1][v|(1<<(f+1))] += dp[j][f][v]
                    dp[j+1][f+1][v|(1<<(f+1))] %= mod

    ans = 0
    for f in range(1, 10):
        ans += dp[num][f][mask-1]
        ans %= mod

    return ans

if __name__ == "__main__":
    print(solution(int(input())))