"""
각도를 이용하여 계산할 수 있을 듯?
현재 건물 (i, ih), 상대 건물 (j, jh) 라고 했을 때,
cos 공식으로 현재 건물과 각도를 구하고,
abs(i - j_1) > abs(i - j_2) 일 때, cos_1 > cos_2 인 경우를 구한다.
즉, 보다 멀리 있는 건물이 각도가 더 크면 현재 건물에서 보인다는 뜻이다.

=> 기울기 공식이 훨씬 쉬울듯
"""
import sys
sys.stdin = open("./1027.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
ans = 0

for i in range(N):
    ih = arr[i]

    left_cnt = 0
    left_max = float('inf')
    for j in range(i - 1, -1, -1):
        jh = arr[j]
        slope_left = (jh - ih)/(j - i)
        if left_max > slope_left:
            left_cnt += 1
            left_max = slope_left

    right_cnt = 0
    right_max = -float('inf')
    for j in range(i + 1, N):
        jh = arr[j]
        slope_right = (jh - ih)/(j - i)
        if right_max < slope_right:
            right_cnt += 1
            right_max = slope_right

    ans = max(ans, right_cnt + left_cnt)

print(ans)
