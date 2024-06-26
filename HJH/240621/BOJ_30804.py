# import sys
# input = sys.stdin.readline
n = int(input())
fruits = tuple(map(int, input().split()))

ans = 1
l = 0
r = 1
fruitCnt = [0] * 10
fruitCnt[fruits[l]] = 1
fruitSet = set([fruits[l]])
while r < n:
    fruitCnt[fruits[r]] += 1
    fruitSet.add(fruits[r])
    r+=1
    while len(fruitSet) > 2:
        fruitCnt[fruits[l]] -= 1
        if fruitCnt[fruits[l]] == 0:
            fruitSet.remove(fruits[l])
        l += 1
    ans = max(ans, r-l)
print(ans)