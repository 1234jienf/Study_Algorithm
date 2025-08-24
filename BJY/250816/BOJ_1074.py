# Z

# 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다.
## 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

## N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

# 첫째 줄에 정수 N, r, c가 주어진다.

# r행 c열을 몇 번째로 방문했는지 출력한다.


# 1 ≤ N ≤ 15
# 0 ≤ r, c < 2N

N, r, c = map(int, input().split())

# 크게 나눠서 1,2,3,4사분면으로 나눠서 재귀적으로 탐색


def z(n, r, c):
    half = 2 ** (n - 1)
    block = half * half
    if n == 1:
        return 2 * r + c
    ## n > 1일때 -> 2사분면
    if r < half and c < half:
        return 0 * block + z(n - 1, r, c)
    ## 1사분면
    elif r < half and c >= half:
        return 1 * block + z(n - 1, r, c - half)
    ## 3사분면
    elif r >= half and c < half:
        return 2 * block + z(n - 1, r - half, c)
    ## 4사분면
    else:
        return 3 * block + z(n - 1, r - half, c - half)


print(z(N, r, c))
