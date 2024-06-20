import sys
input = sys.stdin.readline

t = int(input())

s = ''
ablist = []

def dfs(tmp: list) -> bool:
    for i in range(len(tmp)):
        if tmp[i] >= 2:
            ttmp = tmp[:]
            ttmp.pop(i)
            if len(ttmp) == 0:
                return True
            if len(ttmp) > i > 0:
                ttmp[i-1] += ttmp.pop(i)
            if dfs(ttmp):
                return True
    return False

for testcase in range(t):
    # init
    s = input().strip()
    ablist = [1]

    letter = s[0]
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            ablist[-1] += 1
        else:
            ablist.append(1)
    
    print(1 if dfs(ablist[:]) else 0)