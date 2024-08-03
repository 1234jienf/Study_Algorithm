import heapq

def minimum_classrooms(N, schedule):
    if N == 0:
        return 0

    # 수업을 시작 시간(Si)을 기준으로 오름차순 정렬
    schedule.sort(key=lambda x: x[0])

    # 우선순위 큐를 사용하여 강의실 관리
    classrooms = []

    # 첫 번째 수업을 첫 번째 강의실에 배정
    heapq.heappush(classrooms, schedule[0][1])

    for i in range(1, N):
        if schedule[i][0] >= classrooms[0]:
            # 현재 강의실의 종료 시간(Ti)가 다음 수업의 시작 시간(Si)보다 작거나 같으면
            # 같은 강의실에서 이어서 들을 수 있으므로 우선순위 큐를 업데이트
            heapq.heappop(classrooms)
        # 다음 수업을 해당 강의실로 배정
        heapq.heappush(classrooms, schedule[i][1])

    # 필요한 강의실의 개수 반환
    return len(classrooms)

# 입력 받기
N = int(input())
schedule = []
for _ in range(N):
    Si, Ti = map(int, input().split())
    schedule.append((Si, Ti))

# 결과 출력
result = minimum_classrooms(N, schedule)
print(result)