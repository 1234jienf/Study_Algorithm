import heapq

start, target = map(int,input().split())

distance = [10**9] * 100001

def dijkstra(start):
    global target
    queue = []
    heapq.heappush(queue, (0,start))
    while queue:
        time, now = heapq.heappop(queue)
        next_add = now+1
        next_min = now-1
        next_multi = now*2
        if next_add <= 100000:
            if distance[next_add] > time + 1:
                distance[next_add] = time + 1
                heapq.heappush(queue, (time+1, next_add))
        if next_min >= 0:
            if distance[next_min] > time + 1:
                distance[next_min] = time + 1
                heapq.heappush(queue, (time+1, next_min))
        if next_multi <= 100000:
            if distance[next_multi] > time:
                distance[next_multi] = time
                heapq.heappush(queue, (time, next_multi))

        if next_multi == target or next_add == target or next_min == target:
            print(time+1)
            break


dijkstra(start)