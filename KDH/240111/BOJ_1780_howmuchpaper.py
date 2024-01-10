N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
minus, zero, plus = 0, 0, 0


def dev(x, y, N):
    global minus, zero, plus
    start = arr[x][y]
    for a in range(x, x+N):
        for b in range(y, y+N):
            if start != arr[a][b]:
                for i in range(3):
                    for j in range(3):
                        dev(x+i*N//3, y+j*N//3, N//3)
                return

    if start == -1:
        minus += 1
    elif start == 0:
        zero += 1
    else:
        plus += 1

dev(0,0,N)
print(minus)
print(zero)
print(plus)