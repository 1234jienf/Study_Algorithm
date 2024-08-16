"""
일반적인 부분합 문제로, 투 포인터를 이용하여 해결할 수 있다.
수열은 길이가 N으로, 10,000 이하의 자연수로 이루어진다.
부분 합이 S 이상 되는 것 중 길이가 가장 짧은 것의 길이를 구하면 된다.
해결 방법은 오른쪽 포인터를 진행시키다 합이 S 이상이 되면 현재 길이를 저장하고,
왼쪽 포인터를 진행시키며 합이 S 보다 작아질 때 까지 길이를 저장한다.
다시 합이 S 보다 작아지면 오른쪽 포인터를 진행하는 것을 반복한다.

=> 포인터를 진행시키며 왼쪽 포인터 진행에서 오른쪽 포인터 진행으로 바뀌기 직전에 길이를 저장하면 될듯?
"""
import sys
sys.stdin = open("./1806.txt", "r")

N, S = map(int, input().split())
arr = list(map(int, input().split()))

if sum(arr) < S: # 어떻게 해도 합이 S 보다 작은 경우
    print(0)
    exit()

left, right = -1, 0
total = arr[0]
ans = N

while left < N:
    if total < S:
        if right == N - 1: # 오른쪽 포인터 이동
            break
        right += 1
        total += arr[right]
    else:  # 왼쪽 포인터 이동
        ans = min(ans, right - left)
        left += 1
        total -= arr[left]

print(ans)

# 질문 있?