# 문제
## 은하는 긴 막대에 N개의 과일이 꽂혀있는 과일 탕후루를 만들었습니다. 
## 과일의 각 종류에는 1부터 9까지의 번호가 붙어있고, 
## 앞쪽부터 차례로 S_1, S_2, ..., S_N번 과일이 꽂혀있습니다. 
## 과일 탕후루를 다 만든 은하가 주문을 다시 확인해보니 과일을 두 종류 이하로 사용해달라는 요청이 있었습니다.

## 탕후루를 다시 만들 시간이 없었던 은하는, 
## 막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기기로 했습니다. 
## 앞에서 a개, 뒤에서 b개의 과일을 빼면 S_{a+1}, S_{a+2}, ..., S_{N-b-1}, S_{N-b}번 과일, 
## 총 N-(a+b)개가 꽂혀있는 탕후루가 됩니다. (0 <= a, b; a+b < N) 
## 이렇게 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 구하세요.



## 입력

## 첫 줄에 과일의 개수 N이 주어집니다. (1 <= N <= 200,000)

## 둘째 줄에 탕후루에 꽂힌 과일을 의미하는 N개의 정수 S_1, ..., S_N이 공백으로 구분되어 주어집니다. 
## (1 <= S_i <= 9)

## 출력

## 문제의 방법대로 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 첫째 줄에 출력하세요.

# from collections import deque

# q = deque()
# N = int(input())
# fruit = list(map(int,input().split()))

# lst = [fruit[0]]
# ans = 0

# q.append([0,fruit[0]])


# for i in range(1,N):
#   ## 마지막 있는 번호랑, 현재 들어오는 과일 번호랑 같으면 pop
#   while q and q[-1][-1] == fruit[i]:
#     q.pop()
#   q.append([i,fruit[i]])
#   lst.append(fruit[i])

#   print(lst)
#   if len(set(lst)) > 2:
#     ans = max(ans,q[-1][0] - q[0][0])
#     print(q[-1][0], q[0][0])
#     lst.remove(q[0][1])
#     q.popleft()
#     print(ans)

#   if i == N-1 and len(set(lst)) <= 2:
#     ans = max(ans,q[-1][0] - q[0][0])
#     print(q[-1][0], q[0][0])
#     lst.remove(q[0][1])
#     q.popleft()
#     print(ans)
# print(ans)

def max_fruits(N, fruits):
    if N == 1:
        return 1

    left = 0
    right = 0
    max_length = 0
    fruit_count = {}

    while right < N:
        if fruits[right] in fruit_count:
            fruit_count[fruits[right]] += 1
        else:
            fruit_count[fruits[right]] = 1

        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length

# 입력
N = int(input())
fruits = list(map(int, input().split()))

# 결과 출력
print(max_fruits(N, fruits))
