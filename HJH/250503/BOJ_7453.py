a = []
b = []
c = []
d = []
n = int(input())

for i in range(n):
    l = tuple(map(int, input().split()))
    a.append(l[0])
    b.append(l[1])
    c.append(l[2])
    d.append(l[3])

def sol(a, b, c, d):
    ab = dict()
    for aa in a:
        for bb in b:
            ab[aa+bb] = ab.get(aa+bb, 0) + 1
    
    ans = 0
    for cc in c:
        for dd in d:
            ans += ab.get(-cc-dd, 0)
    return ans

print(sol(a,b,c,d))