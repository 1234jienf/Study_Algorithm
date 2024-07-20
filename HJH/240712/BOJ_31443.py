mod = 10**9+7
n, m = map(int, input().split())
size = n * m
if size % 3 == 0:
    print(3 ** (size // 3) % mod)
elif size % 3 == 1:
    if size == 1:
        print(1)
    else:
        print(2 * 2 * 3 ** ((size - 4) // 3) % mod)
elif size % 3 == 2:
    print(2 * 3 ** ((size - 2) // 3) % mod)