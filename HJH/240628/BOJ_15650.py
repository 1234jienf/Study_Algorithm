n, m = map(int, input().split())

l = [0] * m
def show(depth, last):
    if depth == m:
        print(*l, sep=' ')
        return
    for i in range(last + 1, n - (m - depth) + 2):
        l[depth] = i
        show(depth + 1, i)

show(0, 0)