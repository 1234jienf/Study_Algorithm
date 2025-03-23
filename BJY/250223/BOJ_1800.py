
## N(1<= N <= 1000), P (1 <= P <= 10,000), K (0<= K < N)
## N은 학생들의 번호(인터넷 개수), P는 케이블 연결 선, K는 공짜 인터넷 선 개수 

import heapq
import sys

N, P, K = map(int,input().split())


arr = [[] for _ in range(N+1)]
## 최대 케이블 연결 비용
max_edge = 0

for _ in range(P):
  ## 인접 리스트 구성
  com1, com2, price = map(int,input().split())
  arr[com1].append((com2,price))
  arr[com2].append((com1,price))
  max_edge = max(max_edge, price)

# 변형 다익스트라: X를 최대 부담 비용으로 가정했을 때,
# 1번에서 N번까지 이동 시, X보다 큰 케이블을 사용한 횟수의 최소값을 구합니다.

def dijkstra(limit):
  distances = [sys.maxsize] * (N+1)
  distances[1] = 0

  ## (추가비용, 노드) 쌍 -> 최소 힙
  queue = [(0,1)]

  while queue:
    ## 현재 거리와 정점
    current_d, current_n = heapq.heappop(queue)

    # 해당 노드로 가는 거리와 현재의 거리 비교
    if distances[current_n] < current_d:
      continue

    for next, weight in arr[current_n]:
      ## 만약 가중치가 limit 보다 크면 추가비용 1
      distance = current_d + ( 1 if weight > limit else 0)
      if distance < distances[next]:
        distances[next] = distance
        heapq.heappush(queue, (distance, next))
  return distances[N]

low, high = 0, max_edge
answer = -1

while low <= high:
  mid = (low + high) // 2
  ## 비싼 케이블 사용 횟수가 K 이하면 연결 가능
  if dijkstra(mid) <= K:
    answer = mid
    high = mid - 1

  else:
    low = mid + 1
  
print(answer)