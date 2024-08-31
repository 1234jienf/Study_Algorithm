# 문제
## 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 
## 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.


# 입력
## 첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 
## 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

# 출력
## 첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 
## 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

N, S = map(int,input().split())
lst = list(map(int,input().split()))

## 누적합 만들기
Dlst = [0 for _ in range(N)]
Dlst[0] = lst[0]
for i in range(N-1):
  Dlst[i+1] = Dlst[i] + lst[i+1]
  if lst[i] > S:
    print(1)
    exit()

# # print(*Dlst)
if Dlst[N-1] < S:
  print(0)
  exit()
# else:
#   # 1번 ~ N번 연속
#   for i in range(2,N):
#     for j in range(0,N):
#       if i + j >= N:
#         continue
#       else:
#         if Dlst[i+j] - Dlst[j] >= S:
#           print(i)
#           exit()
ans = 1e9
left, right = 0,1
while left < N:
  if Dlst[right] - Dlst[left] >= S:
    ans = min(ans,right-left)
    left += 1
  else:
    if right < N:
      right += 1
    else:
      left += 1
if ans == 1e9:
  ans = 0
print(ans)