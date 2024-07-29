# 문제
## 수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
## 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.


# 입력
## 첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)
## 둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)

# 출력
## 첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.


## 구간합 문제

N,M = map(int,input().split())
arr = list(map(int,input().split()))
d = []
d_lst = []
## 구간합 만들기
cnt = 0
answer = [0]* (M)
result = 0
## 1 3 6 7 9
for i in range(N):
  cnt += arr[i]
  d.append(cnt)


## 1 0 0 1 0
for num in d:
  d_lst.append(num % M)
for i in range(N):
  answer[d_lst[i]] += 1

for ans in answer:
  ## 개수 중 2개 고르는 경우의 수
  if ans >= 2:
    result += ans * (ans -1) // 2 

result += answer[0]

print(result)