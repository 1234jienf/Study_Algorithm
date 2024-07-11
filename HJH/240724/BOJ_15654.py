n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = [-1] * m
usedIdx = set()

def dfs(depth, lastIdx):
    if depth == m:
        print(*arr)
        return
    
    for i in range(n):
        if i not in usedIdx:
            usedIdx.add(i)
            arr[depth] = nums[i]
            dfs(depth+1, i)
            usedIdx.remove(i)
    
dfs(0, -1)