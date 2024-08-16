"""
계단 수를 구하는 문제로, 재귀와 백트래킹을 이용한 문제이다.
인접 수가 모두 1 차이가 나는 수를 계단수라고 하며, 길이 N 이 주어질 때 계단 수의 갯수를 구하는 문제이다.
처음 시작 수에서 +1, -1을 하며 0 ~ 9 사이임을 확인한다.
조건이 맞는 수 중에서 재귀를 N 번 진행할 때 0 ~ 9 의 방문 기록이 모두 체크되었는지를 확인한다.
조건이 충족되면, 남은 N 번은 진행하지 않고 10 ^ (N - 진행 횟수)를 통해 정답에 더해준다.
또한 조건이 만족할 수 없는 경우를 제거해준다.

=> 시간초과가 나기 때문에 dp 를 사용하는 방법을 찾아보았다.
=> 비트마스킹을 사용해야 한다... 문제가 영 별로다...
"""
import sys
sys.stdin = open("./1562.txt", "r")


def solv(s, cnt):
    global ans

    if v.count(0) > N - cnt - 1:
        return

    if cnt >= N:
        return

    if 0 not in v:
        ans += 10 ** (N - cnt - 1)
        return

    for n in [s + 1, s - 1]:
        if 0 <= n < 10:
            v[n] += 1
            solv(n, cnt + 1)
            v[n] -= 1


N = int(input())
ans = 0

for i in range(1, 10):
    v = [0] * 10
    v[i] = 1
    solv(i, 0)

print(ans)

"""
해답

n = int(input())
num_range = 10 # 0~9
bit_range = 1 << num_range # 9876543210 (0b0 ~ 0b1111111111) -> total 1024 (1023까지)
MOD = 10**9;
DP = [[[0]*(bit_range) for _ in range(num_range)] for _ in range(n+1)]

# 한자리 수 부터 시작하려면 한자리수들 다 1로 초기화
# 1 예시 0b0000000010
for k in range(num_range):
  DP[1][k][1<<k] = 1

for i in range(1,n): # n-1까지하면 n 구할수 있음
  for j in range(num_range):
    for b in range(bit_range):
      if 0<=j<9:
        more = b | 1<<(j+1)
        DP[i+1][j+1][more] += DP[i][j][b]
        DP[i+1][j+1][more] %= MOD
      if 0<j<=9:
        less = b | 1<<(j-1)
        DP[i+1][j-1][less] += DP[i][j][b]
        DP[i+1][j-1][less] %= MOD

total = 0
for k in range(1,num_range): # 0으로 시작하는 수만 제외
  total += DP[n][k][0b1111111111]
  total%=MOD
  
print(total)
"""