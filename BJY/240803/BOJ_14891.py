# 문제
## 총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 아래 그림과 같이 일렬로 놓여져 있다. 
## 또, 톱니는 N극 또는 S극 중 하나를 나타내고 있다. 
## 톱니바퀴에는 번호가 매겨져 있는데, 가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번이다.

## 이때, 톱니바퀴를 총 K번 회전시키려고 한다. 톱니바퀴의 회전은 한 칸을 기준으로 한다. 
## 회전은 시계 방향과 반시계 방향이 있고, 아래 그림과 같이 회전한다.

## 톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야 한다. 
## 톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고,  회전시키지 않을 수도 있다. 
## 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다. 


# 입력
## 첫째 줄에 1번 톱니바퀴의 상태, 
## 둘째 줄에 2번 톱니바퀴의 상태, 
## 셋째 줄에 3번 톱니바퀴의 상태, 
## 넷째 줄에 4번 톱니바퀴의 상태가 주어진다. 
## 상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다. 
## N극은 0, S극은 1로 나타나있다.

## 다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 
## 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다. 
## 각 방법은 두 개의 정수로 이루어져 있고, 
## 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

# 출력
## 총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다. 점수란 다음과 같이 계산한다.

## 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
## 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
## 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
## 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
from collections import deque

# 입력 받기
wheels = [deque(map(int, input().strip())) for _ in range(4)]
K = int(input())
rotations = [tuple(map(int, input().split())) for _ in range(K)]

def spin(idx, direction):
  # 회전할 톱니바퀴 목록과 방향을 저장할 리스트
  to_rotate = [(idx, direction)]
    
  # 왼쪽 톱니바퀴 확인
  d = direction
  for i in range(idx, 0, -1):
    if wheels[i][6] != wheels[i-1][2]:
      d *= -1
      to_rotate.append((i-1, d))
    else:
      break
    
  # 오른쪽 톱니바퀴 확인
  d = direction
  for i in range(idx, 3):
    if wheels[i][2] != wheels[i+1][6]:
      d *= -1
      to_rotate.append((i+1, d))
    else:
      break
    
  # 모든 회전 리스트에 대해 실제 회전 적용
  for i, d in to_rotate:
    if d == 1:  # 시계 방향 회전
      wheels[i].appendleft(wheels[i].pop())
    elif d == -1:  # 반시계 방향 회전
      wheels[i].append(wheels[i].popleft())

# K번의 회전 수행
for now, direction in rotations:
  spin(now - 1, direction)

# 점수 계산
score = 0
for i in range(4):
  if wheels[i][0] == 1:  # 12시 방향이 S극인 경우
    score += 2**i

print(score)
