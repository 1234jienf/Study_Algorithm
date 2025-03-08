# 뒤통수를 쎄게 맞았다.
# 펜윅 트리가 세그먼트 트리의 일종? 이라는 의견이 많은 듯 하지만...
# 본 문제는 세그먼트 트리를 통해 풀면 시간 초과가 난다.
# 문제 잘못골라서 죄송합니다.

# https://yabmoons.tistory.com/438
# 누적합으로 더 많이 사용되는 자료구조같다.
# 누적합(10) - 누적합(2) = 구간합(2~10) 과 같이 구간합으로도 사용할수는 있어보인다.
# 하지만 최대값 최소값과 같은 연산은 불가능해보인다.

# 다시 펜윅 트리를 만들어보자.
def fw_add(tree:list, idx, val):
    while idx <= len(tree):
        tree[idx] += val
        tree[idx] %= MOD
        idx += (idx & -idx) # 최하위 비트를 마스킹하는 방법


def fw_sum(tree: list, idx):
    ans = 0
    while idx > 0:
        ans += tree[idx]
        ans %= MOD
        idx -= (idx & -idx)
    return ans


MOD = 5000000
# main
n, k = map(int, input().split())
arr = list(map(int, input().split()))
trees = [[0] * 100001 for _ in range(k + 1)]

for i, data in enumerate(arr):
    fw_add(trees[1], data, 1)
    for j in range(2, k+1):
        fw_add(trees[j], data, fw_sum(trees[j-1], data-1))

print(fw_sum(trees[k], 100000))