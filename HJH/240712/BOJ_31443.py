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

# 6칸이 있을 때
# 2 2 2 => 8
# 3 3 => 9

# 4칸은 2 2로 나뉘기에 2 블럭으로 나누는 것과 같다. -> 고려 필요성 x
# 5칸 부터는 2 3 으로 나눴을 때 6의 값을 가진다.
# 나누었을때가 본래의 5 보다 큰 가치를 가지기 시작한다.

# 추론: 2, 3으로 나누되 3값을 많이 만들어야겠구나