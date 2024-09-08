import sys
input = sys.stdin.readline

n = int(input())

arr = [250001]
depths = [0] * 250002

def lowerbound(num):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] < num:
            l = m + 1
        else:
            r = m
    return l

ans = 0
for _ in range(n):
    num = int(input())
    index = lowerbound(num)
    lo = arr[index - 1]
    hi = arr[index]

    arr.insert(index, num)
    depths[num] = max(depths[lo], depths[hi]) + 1
    ans += depths[num]
print(ans)