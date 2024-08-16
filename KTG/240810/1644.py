"""
1. 에라토스테네스의 체: N 까지 소수를 구하는
def eratosthenes(num: int = 4000000):
    MAX = num + 1
    LIM = int(num ** 0.5) + 1
    REST = lambda strt, end, gap: set(range(strt, end, gap))

    prime = REST(5, MAX, 6) | REST(7, MAX, 6)
    if num > 2: prime.add(3)
    if num > 1: prime.add(2)
    for i in range(5, LIM, 6):
        if i in prime:
            prime -= REST(i * i, MAX, i * 6) | REST(i * (i + 2), MAX, i * 6)
        j = i + 2
        if j in prime:
            prime -= REST(j * j, MAX, j * 6) | REST(j * (j + 4), MAX, j * 6)

    return prime

2. 투포인터
"""
import sys
sys.stdin = open("1644.txt", "r")

# 입력
N = int(input())

# 소수 구하기
check = [True] * (N + 1)
check[0], check[1] = False, False
prime_list = []
for i in range(2, N + 1):
    if check[i]:
        prime_list.append(i)
        for j in range(2 * i, N + 1, i):
            check[j] = False
    
# 투포인터
left, right, ans = 0, 0, 0
while right <= len(prime_list):
    total = sum(prime_list[left:right])
    if total == N:
        ans += 1
        left += 1
    elif total < N:
        right += 1
    else:
        left += 1

print(ans)
