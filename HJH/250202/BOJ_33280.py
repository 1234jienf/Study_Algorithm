from collections import deque

n, m = 0, 0
cells = None
check = None
start = None
q = deque()
stack = deque()
ans = None
dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
alpha = ['R', 'D', 'L', 'U']

def solution():
    global cells, check, start, q, stack, ans, dyx

    check = [([0] * len(cells[0])) for _ in range(len(cells))]
    check[start[0]][start[1]] = 1

    stack = deque()
    q.append(start)

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy, dx = dyx[i]
            yy = y + dy
            xx = x + dx
            # 안쪽이고 체크한 적 없고 벽아니고
            if isin(yy, xx) and check[yy][xx] == 0 and cells[yy][xx] != '#':
                length = addQ(y, x, i)
                stack.append((y, x, i, length))
    
    if not isAllChecked():
        return
    
    ans = deque()
    while stack:
        addAns(stack.pop())


# 답을 ans 스택에 저장
def addAns(t):
    global check, ans, dyx, alpha
    y, x, i, length = t
    # yy = y + dyx[i][0] * length
    # xx = x + dyx[i][1] * length
    yy = y
    xx = x
    for _ in range(length):
        yy += dyx[i][0]
        xx += dyx[i][1]
        ans.append((y + 1, x + 1, check[yy][xx], alpha[i]))
        check[y][x] += check[yy][xx]


# 모두 체크한 상태가 맞는지
def isAllChecked():
    global n, m, cells, check
    for y in range(n):
        for x in range(m):
            if cells[y][x] == '.' and check[y][x] == 0:
                return False
    return True


# y, x에서 i방향으로 끝까지
def addQ(y, x, i):
    global cells, check, q, dyx
    yy = y + dyx[i][0]
    xx = x + dyx[i][1]
    cnt = 0
    while isin(yy, xx) and check[yy][xx] == 0 and cells[yy][xx] != '#':
        check[yy][xx] = 1
        q.append((yy, xx))
        cnt += 1
        yy += dyx[i][0]
        xx += dyx[i][1]
    return cnt
        

# 안에 있는가
def isin(y, x):
    global n, m
    return (0 <= y < n) and (0 <= x < m)


if __name__ == "__main__":
    n, m = map(int, input().split())
    cells = [input() for _ in range(n)]
    start = tuple(map(int, input().split()))
    start = (start[0]-1, start[1]-1)
    solution()
    if ans == None:
        print('NO')
    else:
        print('YES')
        print(len(ans))
        while ans:
            print(*ans.pop())