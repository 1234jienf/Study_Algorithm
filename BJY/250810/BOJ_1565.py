## 문제

# 배열 D와, 배열 M이 주어졌을 때, D에 있는 모든 수의 배수이며,
# M에 있는 모든 수의 약수인 수의 개수를 구하는 프로그램을 작성하시오.

## 입력

# 첫째 줄에 D의 크기와 M의 크기가 주어진다.
# 둘째 줄에 배열 D, 셋째 줄에 배열 M이 주어진다.
# D와 M의 크기는 50보다 작거나 같고, 그 속에 들어있는 수는 모두 109보다 작거나 같은 양의 정수이다.

## 출력

# 첫째 줄에 개수를 출력한다.

D_size, M_size = map(int, input().split())
D = list(map(int, input().split()))
M = list(map(int, input().split()))

# D에 있는 모든 수의 배수 -> D의 최소공배수의 배수
# M에 있는 모든 수의 약수 -> M의 최대공약수의 약수

# M에 있는 수들 -> 최대 공약수 찾기


## LCM(D) <= X <= GCD(M)
# LCM(D) = m 이고, GCD(M) = n이면,
## lcm(d) = 18, gcd(m) = 60
# X는 m*K(K는 자연수)
## 60 = 18 * K * y
# 이것이 n를 나눠야하므로, m*K <= n 이어야한다.
# 또, 나눠떨어져야하므로 n % (m*K) == 0 이어야한다.
# 즉, m*K*y = n 이어야한다.

# K = n / (m*y)이므로,  n/m * 1/y ->  n/m의 약수 이어야함
## -> K는 n/m의 약수의 개수


## 유클리드 호제법
def gcd(x, y):
    bigger_num = max(x, y)
    smaller_num = min(x, y)

    next_small_num = bigger_num % smaller_num
    if next_small_num == 0:
        return smaller_num
    else:
        return gcd(smaller_num, next_small_num)


def lcm(a, b):
    return a // gcd(a, b) * b


## LCM(D) = m 구하기
m = D[0]
for i in range(1, D_size):
    m = lcm(m, D[i])

## GCD(M) = n 구하기
n = M[0]
for i in range(1, M_size):
    n = gcd(n, M[i])

## n/m이 안되면 답은 0
if n % m != 0:
    print(0)
else:
    # 4) t = n // m 의 약수 개수 = 정답
    t = n // m
    cnt = 0
    i = 1
    while i * i <= t:
        if t % i == 0:
            cnt += 1  # i
            if i * i != t:
                cnt += 1  # 짝 약수 t//i
        i += 1
    print(cnt)
