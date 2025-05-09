## 우선 순위가 높은 업무 순서대로
### 같다면, ID 번호가 작은것
## 1 <= N <= 100,000
## 1 <= Q <= 200,000
import heapq

N, Q = map(int,input().split())
idx_dict = {}
## N개의 줄에 대기목록에 있는 업무 ID, 그 업무의 우선 순위가 주어짐

## 5 3


## 1 8
## 2 4
## 3 9
## 4 1
## 5 1

q = []
for i in range(N):
	idx, priority = map(int,input().split())
	heapq.heappush(q,(-priority, idx))
	idx_dict[idx] = priority

## Q개의 줄에는 업무의 변동사항이 주어짐
### 세가지 형태 중 하나 
### 1. 대기 목록 추가 -> 6 4 (6번 아이디 4의 업무 순서를 추가)
### 2. 업무 처리 -> 일함 (업무 순서 높은 놈)
### 3. 업무 우선 순위 변경 -> 1 30000
for i in range(Q):
	## 1. 대기 목록 추가
	INPUT_STRING = list(map(str,input().split()))
	if INPUT_STRING[0] == "INSERT":
		idx, priority = int(INPUT_STRING[1]), int(INPUT_STRING[2])
		heapq.heappush(q,(-priority,idx))
		idx_dict[idx] = priority
	### 2. 업무 처리
	elif INPUT_STRING[0] == "WORK":
		while q:
			priority, idx = heapq.heappop(q)
			if idx_dict[idx] == -priority:
				del idx_dict[idx]
				break
	### 3. 업무 우선 순위 변경
	else:
		idx, changed_priority = int(INPUT_STRING[1]), int(INPUT_STRING[2])
		heapq.heappush(q,(-changed_priority, idx))
		idx_dict[idx] = changed_priority
	## 현재 대기열에 있는 것들 중 출력
	## CHANGE로 인해 버려져야하는 값 정리
	if q:
		now = heapq.heappop(q)
		if now[1] in idx_dict:
			if idx_dict[now[1]] == -now[0]:
				heapq.heappush(q, (now[0], now[1]))
	## 대기열에 값이 있다면 , print
	if q:
		now = heapq.heappop(q)
		print(now[1])
		heapq.heappush(q,(now[0], now[1]))
	else:
		print("EMPTY")