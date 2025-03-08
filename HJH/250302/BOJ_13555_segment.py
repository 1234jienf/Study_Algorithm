# 그때그때 새로운 원소가 들어오며 검사를 할 수 있어야한다.
# 구간합으로 할 수 없는 이유이다.
# (쉽게말하면) 업데이트 할 수 있는 구간합이라고 볼 수 있는 세그먼트 트리를 이용하여 문제를 풀자
def seg_add(tree: list, start, end, node, index, val):
    if not start <= index <= end: return
    tree[node] += val
    tree[node] %= MOD
    if start == end: return
    mid = (start + end) // 2
    seg_add(tree, start, mid, node * 2, index, val)
    seg_add(tree, mid + 1, end, node * 2 + 1, index, val)


def seg_sum(tree: list, start, end, node, left, right) -> int:
    if left > end or right < start: return 0
    if left <= start and end <= right: return tree[node]
    mid = (start + end) // 2
    return seg_sum(tree, start, mid, node * 2, left, right) + seg_sum(tree, mid + 1, end, node*2+1, left, right)


MOD = 5000000
# main
n, k = map(int, input().split())
arr = list(map(int, input().split()))
trees = [[0] * (100001 * 4) for _ in range(k + 1)]

for i, data in enumerate(arr):
    seg_add(trees[1], 0, 100000, 1, data, 1)
    for j in range(2, k+1):
        seg_add(trees[j], 0, 100000, 1, data, 
                seg_sum(trees[j-1], 0, 100000, 1, 0, data-1))

print(seg_sum(trees[k], 0, 100000, 1, 0, 100000) % MOD)