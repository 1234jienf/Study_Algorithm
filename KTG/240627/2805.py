import sys
sys.stdin = open("./2805.txt", 'r')

N, M = map(int, input().split())

trees = list(map(int, input().split()))

minH = 1
maxH = max(trees)

while minH <= maxH:
    mid = (minH + maxH) // 2

    calcH = 0
    for tree in trees:
        if tree >= mid:
            calcH += tree - mid

    if calcH >= M:
        minH = mid + 1
    else:
        maxH = mid - 1

print(maxH)

# height = max(trees)
# cut = 0
#
# while M >= cut:
#     for i in range(N):
#         if trees[i] > height:
#             cut += 1
#             trees[i] -= 1
#     if cut >= M:
#         break
#     height -= 1
#
# print(height)
