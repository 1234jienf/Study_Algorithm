import sys
input = sys.stdin.readline
sys.setrecursionlimit(500050)


n, m = map(int, input().split())
roots = [i for i in range(n)]


def find(a): # 최고 부모만을 찾아 반환해준다.
    global roots
    if roots[a] == a:
        return a
    else:
        roots[a] = find(roots[a])
        return roots[a]


def union(a, b): # 연결하려는 두 노드의 최고 부모가면같으면 사이클! 아니라면 연결을 해준다.
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return False
    else:
        global roots
        roots[rb] = ra
        return True


for turn in range(m):
    if not union(*map(int, input().split())):
        print(turn+1)
        exit(0)
print(0)