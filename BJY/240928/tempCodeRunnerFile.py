
# 문제
## N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

## N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

## 수의 위치가 다르면 값이 같아도 다른 수이다.

# 입력
## 첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000),
## 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

# 출력
## 좋은 수의 개수를 첫 번째 줄에 출력한다.

N = int(input())
lst = list(map(int, input().split()))
ans = 0

dic = {}
for i in range(N):
  for j in range(i+1, N):
    sum_two = lst[i] + lst[j]
    if sum_two == lst[i] or sum_two == lst[j]:
      continue
    else:
      if sum_two not in dic:
        dic[sum_two] = 1
      else:
        dic[sum_two] += 1

for k in range(N):
  if lst[k] in dic:
    ans += 1

print(ans)