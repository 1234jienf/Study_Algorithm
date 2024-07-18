n = int(input())
students = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    # i - j 까지의 최대값에 i-j~i 구간의 값을 더한다
    # 역순으로 간다 최대 최소 구하기 쉽게
    minimum = students[i]
    maximum = students[i]
    dpi = dp[i-1] # 파이썬이므로 굳이 -1을 처리해주지 말자
    for j in range(i-1, -1, -1):
        minimum = minimum if minimum < students[j] else students[j]
        maximum = maximum if maximum > students[j] else students[j]
        if dpi < maximum - minimum + dp[j-1]:
            dpi = maximum - minimum + dp[j-1]
    dp[i] = dpi

print(dp[-1])