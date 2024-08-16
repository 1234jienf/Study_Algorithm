import sys
input = sys.stdin.readline

t = int(input())

n, m = 0, 0
# 세그먼트 트리
tree = []
# 현재 위치의 인덱스를 저장해준다.
loc = []
top = -1

# 세그먼트 트리를 만드는 재귀함수
def initST(start: int, end: int, node: int):
    if start == end:
        if start < n:
            tree[node] = 1
        else:
            tree[node] = 0
        return tree[node]

    mid = (start + end) // 2
    tree[node] = initST(start, mid, node * 2) + initST(mid + 1, end, node * 2 + 1)
    return tree[node]

# 세그먼트 트리를 이용해 구간합을 구해준다
def sumST(start: int, end: int, node: int, left: int, right: int):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sumST(start, mid, node * 2, left, right) + sumST(mid + 1, end, node * 2 + 1, left, right)

# 배열 내 idx 번째 숫자를 val로 바꿔준다.
def updateST(start: int, end: int, node: int, index: int, diff: int):
    # 범위 밖
    if index < start or end < index: return
    tree[node] += diff
    if start == end: return
    mid = (start + end) // 2
    updateST(start, mid, node * 2, index, diff)
    updateST(mid + 1, end, node * 2 + 1, index, diff)

# 1. n + m 칸만큼의 세그먼트 트리를 만든다.
# 2. loc 배열 초기화
def init() -> None:
    global tree, loc, top
    # nlogn 크기의 트리를 만들 때는 4배 크기로 만들면 절대로 제한 크기를 넘기지 않습니다.
    tree = [0] * ((n + m) * 4)
    initST(0, n + m - 1, 1)
    # n-1, n-2, ... 0
    loc = [n - 1 - i for i in range(n)]
    top = n

for _ in range(t):
    n, m = map(int, input().split())
    init()
    for book in tuple(map(int, input().split())):
        book -= 1
        print(sumST(0, n + m - 1, 1, loc[book] + 1, top - 1), end=' ')
        updateST(0, n + m - 1, 1, loc[book], -1) # loc[book] 의 위치의 누적합들에 -1 씩
        updateST(0, n + m - 1, 1, top, 1) # top의 위치의 누적합들에 1 씩
        loc[book] = top
        top += 1
    print()