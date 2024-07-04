from collections import deque

N = int(input())
num_list = list(map(int,input().split()))
r_cnt = 0
l_cnt = 0

left = 0
right = N-1
ans_list = deque(num_list)

while left <= right:
    if (ans_list[left] != ans_list[right]):
        check_list = []
        for k in range(left):
            check_list.append(ans_list.pop())
        ans_list.append(ans_list[left])
        for k in range(left):
            ans_list.append(check_list.pop())
        right += 1
        r_cnt += 1
    else:
        left += 1
        right -= 1

left = 0
right = N-1
ans_list = deque(num_list)

while left <= right:
    if (ans_list[left] != ans_list[right]):
        check_list = []
        for k in range(left):
            check_list.append(ans_list.popleft())
        ans_list.appendleft(ans_list[right-left])
        for k in range(left):
            ans_list.appendleft(check_list.pop())
        right += 1
        l_cnt += 1
    else:
        left += 1
        right -= 1

print(l_cnt,r_cnt, ans_list)
print(min(l_cnt,r_cnt))