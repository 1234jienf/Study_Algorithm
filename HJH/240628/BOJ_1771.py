n = int(input())
l = list(map(int, input().split()))
s = set(l)

roots = [i for i in range(n + 1)]
# 작은 수, 큰 수, 작은 idx, 큰 idx
sets = [[] for _ in range(n + 1)]
for i in range(n):
    num = l[i]
    sets[num] = [num, num, i, i]
idx = 0

def find(a):
    if roots[a] == a:
        return a
    else:
        roots[a] = find(roots[a])
        return roots[a]

# 항상 작은 수가 루트가 되도록 하자
def union(a, b):
    ra = find(a)
    rb = find(b)
    roots[max(ra, rb)] = min(ra, rb)
    # 수정해야 될 셋의 루트 반환
    return min(ra, rb)

def addable(addSetNum) -> bool:
    setRoot = find(addSetNum)
    thisSet = sets[setRoot]
    # 앞 세트를 찾는다
    forwardSetNum = sets[setRoot][2] - 1
    # 앞 세트가 없다면
    if forwardSetNum == -1:
        return False
    # 앞 세트가 있고 합쳤다
    forwardSetRoot = find(l[forwardSetNum])
    forwardSet = sets[forwardSetRoot]
    if forwardSet[0] - 1 == thisSet[1]:
        print(forwardSet[3]+1)
        modifySet = union(setRoot, forwardSetRoot)
        sets[modifySet] = [thisSet[0], forwardSet[1], forwardSet[2], thisSet[3]]
        return True
    elif forwardSet[1] + 1 == thisSet[0]:
        print(forwardSet[3]+1)
        modifySet = union(setRoot, forwardSetRoot)
        sets[modifySet] = [forwardSet[0], thisSet[1], forwardSet[2], thisSet[3]]
        return True
    # 앞 세트가 있지만 합하지 못했다.
    else:
        return False



while idx < n:
    addSetNum = l[idx]
    idx += 1
    while addable(addSetNum):
        pass
