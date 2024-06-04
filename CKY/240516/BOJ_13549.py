import heapq
# 다익스트라
def dijkstra(start):
    queue = []
    # 우선순위 큐
    heapq.heappush(queue, (0,start))
    while queue:
        # 시간, 위치
        time, now = heapq.heappop(queue)
        # +1 한 값, -1 한 값, *2 한 값
        next_add = now+1
        next_min = now-1
        next_multi = now*2
        # +1 한 값이 100000 이하일 경우
        if next_add <= 100000:
            # 거리값 비교하여 시간이 작은 경우 갱신 후 리스트 추가
            if distance[next_add] > time + 1:
                distance[next_add] = time + 1
                heapq.heappush(queue, (time+1, next_add))
        # -1 한 값이 0 이상일 경우
        if next_min >= 0:
            # 거리값 비교하여 시간이 작은 경우 갱신 후 리스트 추가
            if distance[next_min] > time + 1:
                distance[next_min] = time + 1
                heapq.heappush(queue, (time+1, next_min))
        # *2힌 값이 100000 이하인 경우
        if next_multi <= 100000:
            # 거리값 비교하여 시간이 작은 경우 갱신 후 리스트 추가
            if distance[next_multi] > time:
                distance[next_multi] = time
                heapq.heappush(queue, (time, next_multi))

start, target = map(int,input().split())

if start == target:
    print(0)
else:
    distance = [10**9] * 100001

    dijkstra(start)

    print(distance[target])