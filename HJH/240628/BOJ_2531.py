import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushis = []
for _ in range(n):
    sushis.append(int(input()))

sushiCnt = [0] * (d + 1)
sushiSet = set()
for i in range(k):
    sushiSet.add(sushis[i])
    sushiCnt[sushis[i]] += 1

ans = len(sushiSet) + (0 if c in sushiSet else 1)

l = -n
r = l + k 
while r < n:
    # 왼쪽 빼기
    sushiCnt[sushis[l]] -= 1
    if sushiCnt[sushis[l]] == 0:
        sushiSet.remove(sushis[l])
    l += 1
    # 오른쪽 더하기
    sushiSet.add(sushis[r])
    sushiCnt[sushis[r]] += 1
    r += 1
    # 답 갱신
    ans = max(ans, len(sushiSet) + (0 if c in sushiSet else 1))

print(ans)