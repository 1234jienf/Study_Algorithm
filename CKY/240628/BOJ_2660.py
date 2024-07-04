from collections import deque
import sys

input = sys.stdin.readline
# 너비 우선 탐색 진행
def BFS(start):
    queue = deque([start])
    # 친구의 점수를 리턴해줄 변수
    max_value = 0
    # 처음 시작점 0 으로 선언
    distance[start] = 0
    # queue가 존재할때 까지 반복
    while queue:
        check = queue.popleft()
        for i in graph[check]:
            # 거리가 -1 인 경우 값을 이전 값 +1 로 갱신 후 queue에 추가
            if distance[i] == -1:
                distance[i] = distance[check] + 1
                queue.append(i)
            # max_value 갱신
            if distance[i] > max_value:
                max_value = distance[i]
    return max_value

N = int(input())
# 그래프로 접근
graph = [ [] for _ in range(N+1)]
# -1, -1 나올때 까지 인풋 받기
while True:
    S, E = map(int,input().split())
    if S == -1 and E == -1:
        break
    else:
        graph[S].append(E)
        graph[E].append(S)
# min 값 저장
min_value = 10**9
# N+1 까지 반복
for i in range(1,N+1):
    # 거리 초기값 -1로 선언
    distance = [-1] * (N+1)
    # i 에 대한 친구 점수 저장
    value = BFS(i)
    # min 값 갱신 후 최소값이 변경됐기 떄문에 answer_list 초기화
    if value < min_value:
        min_value = value
        answer_list = [(value, i)]
    # 값이 min 값과 같으면 리스트에 추가
    elif value == min_value:
        answer_list.append((value,i))
# 최소 값, 길이 출력
print(min_value, len(answer_list))
ans = ""
# 리스트 순회하며 ans 라는 str 에 저장
for answer in answer_list:
    ans += str(answer[1]) + " "
print(ans.strip())