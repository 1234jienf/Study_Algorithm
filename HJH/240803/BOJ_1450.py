# 정직하게 냅색 문제를 내고 싶었던 건데
# 이상한 새로운 알고리즘을 배웠네요...
# Meet in the middle 알고리즘입니다!
import itertools

n, c = map(int, input().split())
arr = list(map(int, input().split()))

arr1 = arr[:n//2]
arr2 = arr[n//2:]

def getAllCombList(arr: list) -> list:
    ret = [0]
    for item in arr:
        lenret = len(ret)
        for i in range(lenret):
            ret.append(ret[i] + item)
    ret.sort()
    return ret

def upperbound(arr: list, target: int) -> int:
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] <= target: l = m + 1
        else: r = m
    return l


arr1 = getAllCombList(arr1)
arr1.append(10**9+1)
arr2 = getAllCombList(arr2)

ans = 0
for item in arr2:
    if item > c:
        break
    ans += upperbound(arr1, c - item)
print(ans)