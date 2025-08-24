## 자연수 n이 주어졌을 때, GCD(n, k) = 1을 만족하는
## 자연수 1 ≤ k ≤ n 의 개수를 구하는 프로그램을 작성하시오.

## 입력
# 첫째 줄에 자연수 n (1 ≤ n ≤ 1012)이 주어진다.

## 출력
# GCD(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 출력한다.


import sys

n = int(input())

result = n
p = 2
# n의 제곱근까지만 탐색
while p * p <= n:
    # p가 n의 소인수이면
    if n % p == 0:
        # 오일러 피 함수 공식 -> 소인수 찾아서 소인수의 배수들 제거 하는 공식
        result = result * (1 - 1 / p)
        # n에서 소인수 p를 모두 제거
        while n % p == 0:
            n //= p
    p += 1

# 위 반복문이 끝난 후 n이 1보다 크면,
# 남은 n은 p*p > (원래 n)인 소인수이다.
if n > 1:
    result = result * (1 - 1 / n)

print(int(result))
