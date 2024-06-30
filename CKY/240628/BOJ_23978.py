N, K = map(int,input().split())

days = list(map(int,input().split()))

maximun = K // N

for i in range(1,maximun+1):
    total = 0
    today = [0] * (days[-1]+i)
    for day in days:
        