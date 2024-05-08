## 문제

# 매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다. 
#  이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다.
# 어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 
# 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.


# 세준이가 운전해야 하는 거리의 최솟값을 출력하시오.



## 입력

# 첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다.
# N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다. 
# 다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다.
# 모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 
# 지름길의 시작 위치는 도착 위치보다 작다.


## 출력

# 세준이가 운전해야하는 거리의 최솟값을 출력하시오.


N, D = map(int,input().split())


dp = [i for i in range(D+1)]
lst = []

for i in range(N):
  start, end, length = map(int,input().split())
  ## 지름길 끝이 가는 곳보다 큰 경우
  if end > D:
    continue
  ## 지름길 길이가 더 긴 경우
  if end - start <= length:
    continue
  else:
    lst.append((start,end,length))
lst.sort()
# print(lst)

for s,e, length in lst:
  for i in range(1,D+1):
    if e == i:
      dp[i] = min(dp[i],dp[s]+length)
    else:
      dp[i] = min(dp[i], dp[i-1]+1)

print(dp[D])