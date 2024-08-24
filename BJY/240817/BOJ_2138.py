# 문제
## N개의 스위치와 N개의 전구가 있다. 
## 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. 
## i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 
## 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 
## 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.

## N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 
## 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.


# 입력
## 첫째 줄에 자연수 N(2 ≤ N ≤ 100,000)이 주어진다. 
## 다음 줄에는 전구들의 현재 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 
## 그 다음 줄에는 우리가 만들고자 하는 전구들의 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 
## 0은 켜져 있는 상태, 1은 꺼져 있는 상태를 의미한다.

# 출력
## 첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.
import sys

input = sys.stdin.readline

dict = {True: 1, False: 0}
N = int(input())
now_state = list(map(int,input().split()))
ans = list(map(int,input().split()))

def press_or_not(lst, cnt):
  for i in range(1, N):
    if lst[i-1] != ans[i-1]:
      cnt += 1
      # i번째 스위치를 누르면 i-1, i, i+1의 상태를 변경
      lst[i-1] = dict[not lst[i-1]]
      lst[i] = dict[not lst[i]]
      # 마지막 전구 확인
      if i < N - 1:
        lst[i+1] = dict[not lst[i+1]]
  if lst == ans:
    return cnt
  else:
    return -1

## 1번째 스위치를 안 눌렀을 경우
notpressedlst = now_state[:]
## 1번째 스위치를 눌렀을 경우
### 0 0 0
### 1 1 0
now_state[0] =  dict[not now_state[0]]
now_state[1] =  dict[not now_state[1]]


# if now_state == ans:
#   print(0)
# else: 
#   ans1 = press_or_not(notpressedlst, 0)
#   if ans1 != -1:
#     print(ans1)
#   else:
#     ans2 = press_or_not(now_state, 1)
#     if ans2 != -1:
#       print(ans2)
#     else:
#       print(-1)

ans = min(press_or_not(notpressedlst, 0), press_or_not(now_state, 1))
if ans == -1:
  print(-1)
else:
  print(ans)