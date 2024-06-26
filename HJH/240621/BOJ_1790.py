import sys
# input = sys.stdin.readline

n, k = map(int, input().split())

kk = 1
kkk = 1
while True:
    if k - kk * 9 * kkk > 0:
        k -= kk * 9 * kkk
        kk *= 10
        kkk += 1
    else:
        num = k // kkk + kk
        mod = k % kkk
        if mod == 0:
            num -= 1
            mod = kkk
        if num > n:
            print(-1)
        else:
            print(str(num)[mod-1])
        break