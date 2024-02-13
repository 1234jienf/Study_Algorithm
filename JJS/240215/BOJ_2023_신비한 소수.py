import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def DFS(num):
    if len(str(num)) == n:
        print(num)
        return
    else:
        for i in range(1, 10, 2):
            next_num = num * 10 + i
            if is_prime(next_num):
                DFS(next_num)

for i in [2, 3, 5, 7]:
    DFS(i)
