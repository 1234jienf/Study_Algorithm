## 1번 부터 N번까지 N개의 문제를 풀려고 한다.
## 조건에 맞춰서 문제를 풀어야한다.
### 1. N개의 문제는 모두 풀어야 한다
### 2. 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는것이 좋은 문제를 반드시 먼저 풀어야함
### 3. 가능하면 쉬운 문제부터 풀어야함

## 예를 들어 4번이 2번보다 먼저 푸는게 좋고, 3번이 1번보다 먼저푸는게 좋다면
## 4-3-2-1이 아닌 3-1-4-2로 풀어야함 (조건 3에 의해)

# 문제의 수 N (1 <= N <= 3,000)
# 먼저 풀면 좋은 문제에 대한 정보의 개수 M (1 <= M <= 100,000)
# A B -> A번 문제를 B번 문제보다 먼저 푸는 것이 좋다라는 의미

import heapq

N, M = map(int,input().split())

## 간선 표시 그래프
graph = [[] for _ in range(N+1)]
## 진입 차수 
in_degree = [0] * (N+1)
for i in range(M):
  A,B = map(int,input().split())
  graph[A].append(B)
  in_degree[B] += 1

## graph = [4] = 2, graph[3] = 1
## in_degree = [0,1,0,1,0]

heap = []
for i in range(1,N+1):
  if in_degree[i] == 0:
    heapq.heappush(heap,i)

result = []
while heap:
  ## 진입 차수가 0인 애들 중, 가장 작은(우선순위가 가장 높은 순)
  now = heapq.heappop(heap)
  result.append(now)
  for next in graph[now]:
    in_degree[next] -= 1
    if in_degree[next] == 0:
      ## 진입차수가 0이라면 일단, 힙에 넣기 (next- 순으로 들어가기 떄문에 heap에 더 작은 수가 있어도 노상관)
      heapq.heappush(heap, next)

print(*result)