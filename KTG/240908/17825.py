"""
윳놀이와 동일한 규칙. 단, 말 곂치기는 안됨
미리 판을 만들고 시작하면 편함.
DFS는 문제에서 제시한 조건에 맞게 설정
"""
import sys
sys.stdin = open('./KTG/240908/17825.txt', 'r')

score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 30, 35, 22, 24, 28, 27, 26, 0]
table = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 27], [12], [13], [14], [15], [16, 29], [17], [18], [19], [20], [32], [22], [23], [24], [25], [26], [20], [28], [24], [30], [31], [24], [32]]


def dfs(n, add):
  global ans
  if n == 10:
    ans = max(ans, add)
    return
  
  for i in range(4):
    origin = pieces[i]
    nxt = table[origin][-1]
    for _ in range(1, dice[n]):
      nxt = table[nxt][0]
    
    if nxt == 32 or nxt not in pieces:
      pieces[i] = nxt
      dfs(n + 1, add + score[nxt])
      pieces[i] = origin
      
      
dice = list(map(int, input().split()))
pieces = [0, 0 ,0 ,0]
ans = 0
dfs(0, 0)
print(ans)