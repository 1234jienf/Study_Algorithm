N,M = map(int,input().split())

trees = list(map(int,input().split()))

trees.sort()

start = 1
height = 2000000000

while start <= height:
    middle = (start+height)//2
    total = 0
    for i in range(N-1,-1,-1):
        if trees[i] >= middle:
            total += trees[i] - middle
    
    if total >= M:
        start = middle + 1
    elif total < M:
        height = middle -1

print(height)