t = int(input())
aa = int(input())
a = list(map(int, input().split()))
sumA = []
bb = int(input())
b = list(map(int, input().split()))
sumB = []

sumA.append(0)
for A in a:
    sumA.append(sumA[-1] + A)

sumB.append(0)
for B in b:
    sumB.append(sumB[-1] + B)

As = []
for r in range(len(sumA)):
    for l in range(r):
        As.append(sumA[r] - sumA[l])
As.sort()
Bs = []
for r in range(len(sumB)):
    for l in range(r):
        Bs.append(sumB[r] - sumB[l])
Bs.sort()

def lb(target, a, aa):
    l = 0
    r = aa
    while l < r:
        m = (l+r) // 2
        if a[m] < target:
            l = m + 1
        else:
            r = m
    return l

def ub(target, a, aa):
    l = 0
    r = aa
    while l < r:
        m = (l+r) // 2
        if a[m] <= target:
            l = m + 1
        else:
            r = m
    return l

cnt = 0

i = 0
ii = 0
while i < len(As):
    while ii < len(As) and As[i] == As[ii]:
        ii+=1
    target = t - As[i]
    bcount = ub(target, Bs, len(Bs)) - lb(target, Bs, len(Bs))
    cnt += (ii - i) * bcount
    i = ii

print(cnt)