# from collections import deque

# N = int(input())
# num_list = list(map(int,input().split()))
# r_cnt = 0
# l_cnt = 0

# left = 0
# right = N-1
# ans_list = deque(num_list)

# while left <= right:
#     if (ans_list[left] != ans_list[right]):
#         check_list = []
#         for k in range(left):
#             check_list.append(ans_list.pop())
#         ans_list.append(ans_list[left])
#         for k in range(left):
#             ans_list.append(check_list.pop())
#         right += 1
#         r_cnt += 1
#     else:
#         left += 1
#         right -= 1

# left = 0
# right = N-1
# ans_list = deque(num_list)

# while left <= right:
#     if (ans_list[left] != ans_list[right]):
#         check_list = []
#         for k in range(left):
#             check_list.append(ans_list.popleft())
#         ans_list.appendleft(ans_list[right-left])
#         for k in range(left):
#             ans_list.appendleft(check_list.pop())
#         right += 1
#         l_cnt += 1
#     else:
#         left += 1
#         right -= 1

# print(l_cnt,r_cnt, ans_list)
# print(min(l_cnt,r_cnt))

N = int(input())
# 숫자 리스트 저장
num_list = list(map(int,input().split()))
# 리스트 역순으로 저장
reversed = num_list[::-1]
# LCS 적용 리스트
matrix = [[0] * (N+1) for _ in range(N+1)]
# 기존리스트와 역순 리스트 값을 비교해가며 같은 값의 경우 i-1, j-1 값을 +1 해줌 외의 경우 max 해서 위의 값과 왼쪽 값을 비교
for i in range(1,N+1):
    for j in range(1,N+1):
        if num_list[i-1] == reversed[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(N-matrix[N][N])