mini = 10000000001
maxi = -10000000001
n = int(input())
arr = tuple(map(int, input().split()))
ops = list(map(int, input().split()))


def dfs(depth: int, num: int):
    global mini, maxi, n
    if depth == n:
        mini = mini if mini < num else num
        maxi = maxi if maxi > num else num
        return
    for i in range(4):
        if ops[i] == 0:
            continue
        ops[i] -= 1
        if i == 0:
            dfs(depth + 1, num + arr[depth])
        elif i == 1:
            dfs(depth + 1, num - arr[depth])
        elif i == 2:
            dfs(depth + 1, num * arr[depth])
        else:
            if num < 0 and arr[depth] > 0:
                dfs(depth + 1, -(-num // arr[depth]))
            elif num > 0 and arr[depth] < 0:
                dfs(depth + 1, -(num // -arr[depth]))
            else: 
                dfs(depth + 1, num // arr[depth])
        ops[i] += 1


dfs(1, arr[0])
print(maxi)
print(mini)