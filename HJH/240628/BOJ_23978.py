n, k = map(int, input().split())
dates = list(map(int, input().split()))

# m원 a일 뒤
def adder(m, a):
    if a > m:
        a = m
    b = m
    a = m - a + 1
    if (b - a + 1) % 2 == 0:
        return (a + b) * (b - a + 1) // 2
    else:
        return (a + b) * (b - a) // 2 + (a + b) // 2

def check(m) -> bool:
    total = 0
    for i in range(n - 1):
        dueration = dates[i + 1] - dates[i]
        total += adder(m, dueration)
    total += adder(m, m)
    return total >= k

l = -1
r = k
while l + 1 != r:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m
print(r)