## 나무 M미터가 필요하다. 
## 절단기에 높이 H를 지정/ 높이를 지정하면 톱날이 땅으로부터 H미터 올라감

## 나무의 높이 20, 15, 10, 17 이라고 하자
## 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15
## 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈것이다.
## 절단기에 설정할 수 있는 높이는 양의 정수 또는 0 이다.

## 나무를 필요한만큼만 가져가려고 한다.
# 이때, 적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 
## 높이의 최댓값을 구하시오

## 나무의 수 N, 상근이가 가져가려고 하는 나무의 길이 M
### 1 <= N <= 1,000,000 / 1<= M <= 2,000,000,000

## 나무의 높이가 주어짐(나무의 높이는 항상 M보다 크거나 같다)

N, M = map(int,input().split())

t_lst = list(map(int,input().split()))

## 이분 탐색으로 자를 수 있는 나무의 높이 M 구하기
right = max(t_lst)
left = 0


def calculate(x):
  cnt = 0
  for i in range(N):
    if t_lst[i] - x > 0:
      cnt += t_lst[i] - x 
    if cnt >= M:
      return True
  return False

while left <= right:
  mid = (left + right) // 2
  if calculate(mid):
    ans = mid
    left = mid + 1
  else:
    right = mid - 1

print(ans)