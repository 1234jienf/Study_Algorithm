n = 0
ans = []

def sol():
    global n, ans

    while n != 0:
        if n & 1 == 1:
            n *= 2
            ans.append('/')
        elif n & 2 != 0:
            n -= 2
            ans.append('+')
        else:
            n //= 2
            ans.append('*')
    ans.reverse()


if __name__ == "__main__":
    n = int(input())
    sol()
    print(len(ans))
    print('[' + '] ['.join(ans) +']')