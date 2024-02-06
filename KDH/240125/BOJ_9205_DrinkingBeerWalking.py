from collections import deque
t = int(input())

for _ in range(t):
    n = int(input())
    convini = []
    for i in range(n+2):
        con_x, con_y = map(int,input().split())
        convini.append((con_x,con_y))
    # rockpe = map(int, input().split())

    
    def bfs():
        visited = [0]*(n+2)
        q = deque()
        q.append(0)
        visited[0] = 1
        while q:
            now = q.popleft()
            for i in range(1,n+2):
                distance = abs(convini[now][0] - convini[i][0]) + abs(convini[now][1] - convini[i][1])
                # print(distance,'dis')
                if distance <= 1000:
                    if visited[i] == 0:
                        q.append(i)
                        visited[i] = 1
                        # print(visited,'visited')
        if visited[-1] == 1:
            print('happy')
        else:
            print('sad')

    bfs()

