# 문제
## 가로 A(1≤A≤100), 세로 B(1≤B≤100) 크기의 땅이 있다. 
## 이 땅 위에 로봇들이 N(1≤N≤100)개 있다.

## 로봇들의 초기 위치는 x좌표와 y좌표로 나타난다. 
## 위의 그림에서 보듯 x좌표는 왼쪽부터, y좌표는 아래쪽부터 순서가 매겨진다. 
## 또한 각 로봇은 맨 처음에 NWES 중 하나의 방향을 향해 서 있다. 초기에 서 있는 로봇들의 위치는 서로 다르다.


## 이러한 로봇들에 M(1≤M≤100)개의 명령을 내리려고 한다. 
## 각각의 명령은 순차적으로 실행된다. 즉, 하나의 명령을 한 로봇에서 내렸으면, 
## 그 명령이 완수될 때까지 그 로봇과 다른 모든 로봇에게 다른 명령을 내릴 수 없다.
## 각각의 로봇에 대해 수행하는 명령은 다음의 세 가지가 있다.

# 1.L: 로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전한다.
# 2.R: 로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전한다.
# 3.F: 로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직인다.

## 간혹 로봇들에게 내리는 명령이 잘못될 수도 있기 때문에, 
## 당신은 로봇들에게 명령을 내리기 전에 한 번 시뮬레이션을 해 보면서 
# 안전성을 검증하려 한다. 이를 도와주는 프로그램을 작성하시오.


# 잘못된 명령에는 다음의 두 가지가 있을 수 있다.

# 1.Robot X crashes into the wall: X번 로봇이 벽에 충돌하는 경우이다. 즉, 주어진 땅의 밖으로 벗어나는 경우가 된다.
# 2.Robot X crashes into robot Y: X번 로봇이 움직이다가 Y번 로봇에 충돌하는 경우이다.

# 입력
## 첫째 줄에 두 정수 A, B가 주어진다. 
## 다음 줄에는 두 정수 N, M이 주어진다. 
## 다음 N개의 줄에는 각 로봇의 초기 위치(x, y좌표 순) 및 방향이 주어진다. 
## 다음 M개의 줄에는 각 명령이 명령을 내리는 순서대로 주어진다. 
## 각각의 명령은 명령을 내리는 로봇, 명령의 종류(위에 나와 있는), 명령의 반복 회수로 나타낸다. 
## 각 명령의 반복 회수는 1이상 100이하이다.

# 출력
## 첫째 줄에 시뮬레이션 결과를 출력한다. 
## 문제가 없는 경우에는 OK를, 그 외의 경우에는 위의 형식대로 출력을 한다. 
## 만약 충돌이 여러 번 발생하는 경우에는 가장 먼저 발생하는 충돌을 출력하면 된다.

# 가로 A , 세로 B
A,B = map(int,input().split())
arr = [[0] * A for _ in range(B)]
# 로봇 N개
N,M = map(int,input().split())
# 방향 N,E,S,W
#     0,1,2,3
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 로봇 명령
# 왼쪽 회전 :  0->3,3->2,2->1,1->0
# 오른쪽 회전 : 0->1,1->2,2->3,3->0

# 방향 - idx 연결
dict_idx = {
  'N': 0,
  'E': 1,
  'S': 2,
  'W': 3
}

robot_loc = []
robot = []
for i in range(N):
  x,y,d = input().split()
  x, y = int(x), int(y)
  robot.append([x,y,dict_idx[d]])


commands = []
for _ in range(M):
    idx, order, cnt = input().split()
    commands.append([int(idx) - 1, order, int(cnt)])

# sum = 0
# while sum != M:
#   idx, order, cnt = map(int,input().split())
#   now_d = robot[idx-1][2]
#   now_x,now_y = robot[idx-1][0],robot[idx-1][1]
#   for j in range(cnt):
#     if order == 'F':
#       next_x, next_y = now_x + dx[dict_idx[now_d]], now_y + dy[dict_idx[now_d]]
#       if (next_x, next_y) in robot[]:


def simulation():
  for idx, order, cnt in commands:
    for _ in range(cnt):
      if order == 'L':
        robot[idx][2] = (robot[idx][2] - 1) % 4
      elif order == 'R':
        robot[idx][2] = (robot[idx][2] + 1) % 4
      elif order == 'F':
        nx = robot[idx][0] + dx[robot[idx][2]]
        ny = robot[idx][1] + dy[robot[idx][2]]

        # 벽 충돌 확인
        if nx < 1 or nx > A or ny < 1 or ny > B:
          return f"Robot {idx + 1} crashes into the wall"
        
        # 다른 로봇과 충돌 확인
        for j in range(N):
          if j != idx and robot[j][0] == nx and robot[j][1] == ny:
            return f"Robot {idx + 1} crashes into robot {j + 1}"
                
        # 위치 업데이트
        robot[idx][0] = nx
        robot[idx][1] = ny
  return "OK"

print(simulation())
