from collections import defaultdict

n = -1
m = -1
a = None
arr = None
size = 0
nums = None
dp = None
MOD = 1000000007

def makeDP():
    global n, m, nums, dp, arr, size
    dp = [[0 for _ in range(size + 1)] for _ in range(size + 1)]
    for i in range(size + 1):
        dp[i][0] = 1
    for j in range(1, m+1):
        for i in range(j, size + 1):
            dp[i][j] = (dp[i - 1][j - 1] * arr[i-1] + dp[i - 1][j]) % MOD


def main():
    global n, m, a, dp, arr, size
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    nums = defaultdict(int)
    for num in a:
        nums[num] += 1
    
    arr = [key * value for key, value in nums.items()]
    size = len(arr)
    print(arr)
    makeDP()
    print(dp[size][m])
    

if __name__ == '__main__':
    main()