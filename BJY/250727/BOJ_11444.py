# 피보나치 수 -> 0과 1로 시작

## 0 번째 수는 0, 1번째 순느 1, 다음 2번째부터 바로 두앞의 두 피보나치 수의 합

# Fn = Fn-1 + Fn-2 (n >= 2)

## n이 주어졌을때 , n번쨰 피보나치 수를 구하는 program 작성


n = int(input())  # n은  1,000,000,000,000,000,000보다 작거나 같은 자연수이다.


## 출력 : n번째 피보나치수를 1,000,000,007로 나눈 나머지를 출력한다.
# def pibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return pibo(n - 1) + pibo(n - 2)


# print(pibo(n))

MOD = 1_000_000_007

# 피보나치 수열의 점화식을 행렬로 표현하면 다음과 같다
# | F(n+1) |   | 1  1 |   | F(n)   |
# | F(n)   | = | 1  0 | * | F(n-1) |
# | F(n-1) |   | 1  1 |   | F(n-1)   |
# | F(n-1)   | = | 1  0 | * | F(n-1) |
#
# 이를 일반화하면 다음과 같다
# | F(n+1)  F(n)   |   | 1  1 |^n
# | F(n)    F(n-1) | = | 1  0 |
# 따라서 F(n)을 구하기 위해서는 |1 1|^n 행렬을 구해야 한다.
#                         |1 0|

Q = [[1, 1], [1, 0]]


def matrix_mul(A, B):
    ## 2x2 행렬곱
    # 각 원소의 덧셈이 모두 끝난 후 MOD 연산을 해야 올바른 결과가 나옵니다.
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD,
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD,
        ],
    ]


## 분할정복
## 이진 거듭 제곱
## 짝수 -> Qn = (Qn/2)**2
## 홀수 -> Qn = Q*Qn-1
def matrix_pow(A, n):
    # n=1이 될 때까지 재귀적으로 호출된 후, A를 반환하면서 재귀가 풀리기 시작한다.
    print("함수 호출", n)
    if n == 1:
        return A

    # n을 2로 나눈 몫으로 재귀 호출하여 절반의 거듭제곱을 구한다.
    print("함수 재귀", n)
    half_pow = matrix_pow(A, n // 2)

    # half_pow를 두 번 곱하여 A^n (n이 짝수일 때) 또는 A^(n-1) (n이 홀수일 때)를 계산한다.
    result = matrix_mul(half_pow, half_pow)
    print("result", result)

    # n이 홀수인 경우, A를 한 번 더 곱해준다. A^n = A * A^(n-1)
    if n % 2 != 0:
        result = matrix_mul(result, Q)

    print(n)
    print(half_pow)
    print(result)

    return result


def fibo(n):
    # n이 0 또는 1인 경우는 행렬 계산 없이 즉시 값을 반환합니다.
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Q^(n-1)을 계산합니다.
    # Q^k 행렬은 [[F(k+1), F(k)], [F(k), F(k-1)]] 형태를 가진다.
    # 따라서 Q^(n-1)의 [0][0] 원소는 F(n)이 됩니다.
    P = matrix_pow(Q, n - 1)

    # 확인을 위해 계산된 행렬을 출력합니다.
    print(P)

    # F(n)은 계산된 행렬의 [0][0] 위치에 있다.
    return P[0][0]


print(fibo(n))
