# 문제
## 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
## 비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?


## 입력

# 첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)
# 두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.


# 따라서 블록 내부의 빈 공간이 생길 수 없다. 
# 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.


## 출력

# 2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.

# 빗물이 전혀 고이지 않을 경우 0을 출력하여라.


N, K = map(int,input().split())

g_map = list(map(int,input().split()))

cnt = 0

for i in range(1,K-1):
    left = max(g_map[:i])
    right = max(g_map[i+1:])
    m = min(left,right)
    if m > g_map[i]:
        cnt += m - g_map[i]
print(cnt)

# if len(g_map) > 2:
#     for i in range(len(g_map)-1):
#         if g_map[i] <= g_map[i+1]:
#             continue
#         else:
#             g_map = g_map[i:]
#             break
#     for j in range(len(g_map)-1):
#         if g_map[-1-j] <= g_map[-2-j]:
#             continue
#         else:
#             if j >= 1:
#                 g_map = g_map[0:-j]
#                 break
#         break
# cnt = 0
# sum_g = 0
# stack = []

# for i in range(len(g_map)-1):
#     stack.append(g_map[i])
#     sum_g += g_map[i]
#     if len(stack) > 2:
#         if stack[-1] >= stack[0] and stack[-1] >= g_map[i+1]:
#             cnt += (len(stack)-2) * min(stack[0],stack[-1]) - (sum_g - (stack[0]+stack[-1]))
#             stack = [stack[-1]]
#             sum_g  = stack[-1]
#             continue
#         if stack[-1] >= g_map[i+1] and stack[-1] >= g_map[-1] and stack[-1] >= stack[-2]:
#             cnt += (len(stack)-2) * min(stack[0],stack[-1]) - (sum_g - (stack[0]+stack[-1]))
#             stack = [stack[-1]]
#             sum_g  = stack[-1]
#             continue
#     if len(stack) >= 2:
#         if stack[-1] <= g_map[i+1] and i+1 == len(g_map)-1:
#             stack.append(g_map[i+1])
#             sum_g += g_map[i+1]
#             plus = 0
#             sum_p = 0
#             for i in range(1,len(stack)):
#                 if stack[i] > stack[-1]:
#                     plus += 1
#                     sum_p += stack[i]
#             cnt += (len(stack)-(2+plus)) * min(stack[0],stack[-1]) - (sum_g - (stack[0]+stack[-1]+sum_p))
#         else:
#             continue

# print(cnt)