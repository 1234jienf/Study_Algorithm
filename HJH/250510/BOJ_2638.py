from collections import deque

n, m = map(int, input().split())
cells = [list(map(int, input().split())) for _ in range(n)]
visited = None
counter = None

def no_one():
    for line in cells:
        if 1 in line:
            return False
    return True

def make_counter():
    global counter, visited

    counter = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    q = deque([(0, 0)])
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cells[nx][ny] == 1:
                    counter[nx][ny] += 1
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
def remove_over_2():
    global cells, counter
    for i in range(n):
        for j in range(m):
            if counter[i][j] >= 2:
                cells[i][j] = 0

time = 0
while not no_one():
    make_counter()
    remove_over_2()
    time += 1
print(time)