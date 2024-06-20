# 문제
## N개의 수 A1, A2, ..., AN과 L이 주어진다.
## Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 
## 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

## 입력

# 첫째 줄에 N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)
# 둘째 줄에는 N개의 수 Ai가 주어진다. (-109 ≤ Ai ≤ 109)

## 출력

# 첫째 줄에 Di를 공백으로 구분하여 순서대로 출력한다.
import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int,input().split())
q = deque()
now = list(map(int,input().split()))

for i in range(N):
  ## 제일 끝에 존재하는 숫자가 들어올 숫자보다 크면 pop한다.
  ## 최솟값을 찾는거니깐 큰 숫자는 필요가 없음
  while q and q[-1][0] > now[i]:
    q.pop()

  ## 숫자, 인덱스 값
  q.append((now[i],i))
  ## 윈도우 범위를 벗어나면
  if q[0][1] <= i - L:
    q.popleft()

  print(q[0][0], end=' ')
