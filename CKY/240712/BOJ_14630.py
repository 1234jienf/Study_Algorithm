import heapq
import sys

input = sys.stdin.readline

def dijkstra(start, end):
    global graph_length
    distance = [ 10**9 for _ in range(N+1) ]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        for index in range(1,N+1):
            if now == index:
                continue
            check = 0
            for j in range(graph_length):
                check += (graph[now][j]-graph[index][j])**2
            new_cost = cost + check
            if new_cost < distance[index]:
                distance[index] = new_cost
                heapq.heappush(q, (new_cost,index))
    return distance[end]

N = int(input())
graph = [ []]

for n in range(1,N+1):
    state = list(map(int,input().strip()))
    graph.append(state)
print(graph)
graph_length = len(graph[1])
start, end = map(int,input().split())
print(dijkstra(start,end))