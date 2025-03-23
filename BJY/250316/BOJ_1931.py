
## 한 개의 회의실이 있는데, 이를 사용하고자 하는 N개의 회의에 대해 회의실 사용표를 만들려고 함
## 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져있고,
## 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾자

## 회의는 한번 시작하면 중간에 중단할 수 없으며 한 회의가 끝나느것과 동시에 다음 회의가 시작될 수 있다.
## 회의의 시작시간과 끝나는 시간이 같을 수도 있다.

## 회의의 수 N(1<= N <= 100,000)
## N+1줄까지의 각 회의의 정보가 주어짐 (시작 시간, 끝나는 시각)
## 시작 시간과 끝나는 시간은 2^31-1보다 작거나 같은 자연수 또는 0이다.

N = int(input())

meetings = []
for i in range(N):
  start,end = int(input().split())
  meetings.append((start,end))

## 끝나는 시간 기준으로 오름차순 정렬
## 끝나는 시간이 같다면, 시작 시간이 빠른 순서대로
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
current_end_time = 0

for start, end in meetings:
  ## 회의 시작 시간이 현재까지 선택한 회의의 끝나는 시간보다 크거나 같으면 선택
  if start >= current_end_time:
    cnt += 1
    current_end_time = end


print(cnt)