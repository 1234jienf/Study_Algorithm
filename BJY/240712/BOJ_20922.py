# 문제
## 홍대병에 걸린 도현이는 겹치는 것을 매우 싫어한다. 
## 특히 수열에서 같은 원소가 여러 개 들어 있는 수열을 싫어한다. 
## 도현이를 위해 같은 원소가 $K$개 이하로 들어 있는 최장 연속 부분 수열의 길이를 구하려고 한다.

## $100\,000$ 이하의 양의 정수로 이루어진 길이가 $N$인 수열이 주어진다. 
## 이 수열에서 같은 정수를 $K$개 이하로 포함한 최장 연속 부분 수열의 길이를 구하는 프로그램을 작성해보자.

# 입력
## 첫째 줄에 정수 $N$ ($1 \le N \le 200\,000$)과 $K$ ($1 \le K \le 100$)가 주어진다.

## 둘째 줄에는 ${a_1, a_2, ... a_n}$이 주어진다 ($1 \le a_i \le 100\,000$)

# 출력
## 조건을 만족하는 최장 연속 부분 수열의 길이를 출력한다.
from collections import deque
N, K = map(int,input().split())
arr = list(map(int,input().split()))
left = 0
visited = [0] * 100001
q = deque()
ans = 0

for right in range(N):
  q.append(arr[right])
  visited[arr[right]] += 1
  
  while visited[arr[right]] > K:
    visited[q[0]] -= 1
    q.popleft()
    left += 1

  ans = max(ans, len(q))


print(ans)