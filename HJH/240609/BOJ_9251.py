import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

LCS = [[0] * (len(b)+1) for _ in range(len(a)+1)]

ans = 0
for ai in range(len(a)):
    for bi in range(len(b)):
        if a[ai] == b[bi]:
            LCS[ai+1][bi+1] = max(LCS[ai+1][bi+1], LCS[ai][bi] + 1)
        LCS[ai+1][bi+1] = max(LCS[ai+1][bi+1], LCS[ai][bi+1])
        LCS[ai+1][bi+1] = max(LCS[ai+1][bi+1], LCS[ai+1][bi])
        if ans < LCS[ai+1][bi+1]:
            ans = LCS[ai+1][bi+1]
print(ans)