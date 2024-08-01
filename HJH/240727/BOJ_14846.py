from collections import defaultdict

n = int(input())
mat = []
a = defaultdict(int)
for _ in range(n):
    mat.append(list(map(int, input().split())))

def dictPutNum(matrix: defaultdict, num: int) -> defaultdict:
    matrix[num] += 1
    return matrix

def dictAdd(a: defaultdict, b:defaultdict) -> defaultdict:
    for key, value in b.items():
        a[key] += value
    return a

def dictSub(a: defaultdict, b: defaultdict) -> defaultdict:
    for key, value in b.items():
        a[key] -= value
    return a

dp = [[defaultdict(int) for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i+1][j].copy()
        dp[i+1][j+1] = dictAdd(dp[i+1][j+1], dp[i][j+1])
        dp[i+1][j+1] = dictSub(dp[i+1][j+1], dp[i][j])
        dp[i+1][j+1] = dictPutNum(dp[i+1][j+1], mat[i][j])

q = int(input())
for _ in range(q):
    y, x, yy, xx = map(int, input().split())
    tmp = dp[yy][xx].copy()
    tmp = dictSub(tmp, dp[y-1][xx])
    tmp = dictSub(tmp, dp[yy][x-1])
    tmp = dictAdd(tmp, dp[y-1][x-1])
    cnt = 0
    for key, value in tmp.items():
        if value != 0:
            cnt += 1
    print(cnt)
    
# 각 숫자가 몇개씩 있는지 누적합을 합니다.
# 가능한 숫자의 목록이 1 ~ 10 이므로 n * n * 10 배열을 만들어서 갯수를 체크해줍니다.
# 저는 10개라는 사실을 모르고 작성하느라 기본값을 0으로 가지는 defaultdict를 사용했습니다.