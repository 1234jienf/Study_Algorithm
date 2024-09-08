# 문제
## 당신은 집으로 가는 도중 복잡한 교차로를 만났다!
## 이 교차로에는 사람이 지나갈 수 있는 N 개의 지역이 있고 그 지역 사이를 잇는 몇 개의 횡단보도가 있다. 
## 모든 지역은 횡단보도를 통해 직, 간접적으로 연결되어 있다. 
## 편의상 N 개의 지역을 1부터 N까지로 번호를 붙이자.

## 당신은 이미 멀리서 교차로의 신호를 분석했기 때문에 횡단보도에 파란불이 들어오는 순서를 알고 있다. 
## 횡단보도의 주기는 총 M 분이며 1분마다 신호가 바뀐다. 
## 각 주기의 1+i (0 \le i < M) 번째 신호는 i, M+i, 2M+i, 3M+i, ... 분에 시작해서 1분 동안 
## A_i번 지역과 B_i번 지역을 잇는 횡단보도에 파란불이 들어오고, 다른 모든 횡단보도에는 빨간불이 들어온다. 
## 한 주기 동안 같은 횡단보도에 파란불이 여러 번 들어올 수 있다.

## 횡단보도에 파란불이 들어오면 당신은 해당 횡단보도를 이용하여 반대편 지역으로 이동할 수 있으며 이동하는 데 1분이 걸린다. 
## 횡단보도를 건너는 도중에 신호가 빨간불이 되면 안되기 때문에 신호가 s ~ e 시간에 들어온다면 반드시 s ~ e-1 시간에 횡단보도를 건너기 시작해야 한다.

## 횡단보도와 신호의 정보가 주어질 때, 시간 0분 에서 시작해서 1번 지역에서 N번 지역까지 가는 최소 시간을 구하는 프로그램을 작성하여라.

# 입력
## 첫 번째 줄에는 지역의 수 N, 횡단보도의 주기 M이 공백으로 구분되어 주어진다.

## 두 번째 줄부터 M 개의 줄 중 1+i 번째 줄에는 i, M+i, 2M+i, 3M+i, ... 분에 시작해서
## 1분동안 파란불이 들어오는 횡단보도의 두 끝점 A_i, B_i가 공백으로 주어진다.

# 출력
## 첫 번째 줄에 1 번 지역에서 N 번 지역까지 가는데 필요한 최소 시간을 분단위로 출력한다.
import sys
import heapq

N, M = map(int,input().split())
## 인접 리스트 만들기
cross_rule = [[] for _ in range(N+1)]
for i in range(M):
  start, end = map(int,input().split())
  ## [[],
  # [(2,1),(3,3),(4,4)],
  # [(1,1),(3,5)],
  # [(4,2),(1,3),(2,5)],
  # [(3,2),(1,4)]
  # ]
  cross_rule[start].append((end,i+1))
  cross_rule[end].append((start,i+1))

def dijk(start):
  distance = [sys.maxsize] * (N+1)
  distance[start] = 0
  visited = [0] * (N+1)
  pq = []
  heapq.heappush(pq,(0,(0,start)))

  while pq:
    time, (start,end) = heapq.heappop(pq) 
    if visited[end]:
      continue
    visited[end] = True
    for tmp in cross_rule[end]:
      next = tmp[0]
      time = tmp[1]
      ## 같은 주기 안에 있는 시간
      if distance[end] % M < time:
        if distance[next] > distance[end] + (time - distance[end] % M):
          distance[next] = distance[end] + (time - distance[end] % M)
          heapq.heappush(pq,(distance[next],(end,next)))
      else:
        if distance[next] > distance[end] + ( time - distance[end] % M )+ M:
          distance[next] = distance[end] + ( time - distance[end] % M )+ M
          heapq.heappush(pq,(distance[next],(end,next)))
  return distance

result = dijk(1)
print(result[N])