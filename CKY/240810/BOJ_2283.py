import sys

input = sys.stdin.readline

N, K = map(int,input().split())

number = [0]*1000001

start = 0
end = 0

for _ in range(N):
    S,E = map(int,input().split())
    for i in range(S,E):
        number[i] += 1

total = 0

while start <= end and end <= 1000001:
    if total == K:
        print(start,end)
        break
    elif total < K:
        total += number[end]
        end += 1
    else:
        total -= number[start]
        start += 1
else:
    print(0,0)