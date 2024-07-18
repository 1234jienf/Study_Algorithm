n, m = map(int, input().split())
vs = []
for i in range(m):
    vs.append(tuple(map(int, input().split())))
vs.sort(key=lambda x: x[2])

roots = [i for i in range(n+1)]

def find(node):
    if roots[node] == node:
        return node
    else:
        roots[node] = find(roots[node])
        return roots[node]

# 사이클 발생시 합치지 않고 False 반환
#     미발생시 합치고 True 반환
def union(a, b) -> bool: 
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return False
    else:
        roots[rb] = ra
        return True

ans = 0
last = 0
for a, b, c in vs:
    isUnified = union(a, b)
    if isUnified:
        ans += c
        last = c
print(ans - last)