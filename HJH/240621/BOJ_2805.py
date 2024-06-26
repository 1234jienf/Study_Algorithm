n, m = map(int, input().split())
arr = tuple(map(int ,input().split()))

def check(mid):
    total = 0
    for a in arr:
        total += max(0, a - mid)
    return total >= m

l = 0
r = max(arr) + 1
while l + 1 != r:
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid
print(l)