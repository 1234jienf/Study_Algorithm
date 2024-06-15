import heapq

def dijkstra(distance,matrix):
    adj_matrix = []
    heapq.heappush(adj_matrix, [0,1])
    while adj_matrix:
        cost, node = heapq.heappop(adj_matrix)
        for c,n in matrix[node]:
            if cost+c < distance[n]:
                distance[n] = cost+c
                heapq.heappush(adj_matrix, [cost+c,n])

def solution(N, road, K):
    distance = [10**9] * (N+1)
    distance[1] = 0
    answer = 0
    matrix = [[] for _ in range(N+1)]
    for rod in road:
        matrix[rod[0]].append([rod[2],rod[1]])
        matrix[rod[1]].append([rod[2],rod[0]])
    dijkstra(distance,matrix)
    
    for i in distance:
        if i <= K:
            answer += 1
    
    return answer