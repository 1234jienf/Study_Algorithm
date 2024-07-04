import sys
input = sys.stdin.readline

INF = 51

n = int(input())
adj = [[INF] * (n + 1) for _ in range(n + 1)]

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    adj[a][b] = 1
    adj[b][a] = 1

for i in range(1, n + 1):
    adj[i][i] = 0

for via in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if adj[a][b] > adj[a][via] + adj[via][b]:
                adj[a][b] = adj[a][via] + adj[via][b]
                adj[b][a] = adj[a][b]

ansDist = INF
ansCand = []
for i in range(1, n + 1):
    adj[i][0] = 0
    maxDist = max(adj[i])
    if maxDist < ansDist:
        ansDist = maxDist
        ansCand = [i]
    elif maxDist == ansDist:
        ansCand.append(i)

print(f'{ansDist} {len(ansCand)}')
print(*ansCand, sep=' ')