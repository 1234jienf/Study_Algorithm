import sys

input = sys.stdin.readline

position = []

N = int(input())

for _ in range(N):
    position.append(list(map(int,input().split())))

position.sort()

town,fuel = map(int,input().split())

if fuel >= town:
    print(0)
else:
