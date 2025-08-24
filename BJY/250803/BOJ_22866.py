import sys

input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

visible_count = [0] * N
closest = [None] * N

# 왼쪽에서 볼 수 있는 건물
stack = []
for i in range(N):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    if stack:
        visible_count[i] += len(stack)
        closest[i] = stack[-1]
    stack.append(i)

# 오른쪽에서 볼 수 있는 건물
stack = []
for i in range(N - 1, -1, -1):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    if stack:
        visible_count[i] += len(stack)
        if closest[i] is None:
            closest[i] = stack[-1]
        else:
            # 거리 비교
            if abs(closest[i] - i) > abs(stack[-1] - i):
                closest[i] = stack[-1]
            elif abs(closest[i] - i) == abs(stack[-1] - i):
                closest[i] = min(closest[i], stack[-1])
    stack.append(i)

# 출력
for i in range(N):
    if visible_count[i] == 0:
        print(0)
    else:
        print(visible_count[i], closest[i] + 1)  # 번호는 1-based
