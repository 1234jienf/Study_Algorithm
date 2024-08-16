"""
문제)
각 도시마다 투자비용 당 유치 고객이 주어진다.
주어진 값은 무한대로 정수배 할 수 있다고 할 때,
최소 유치 고객을 확보하는데 필요한 최소비용은?

최소 고객 C(<= 1000), 도시 개수 N(<= 20)
비용 cost(<= 100), 고객 customer(<= 100)

해설)
dp를 사용하여 유치 고객수의 베열을 만들고,
각 도시에 투자했을 경우 각 도시의 유치 비용 + 이전 유치 비용을 비교하여 배열에 할당한다.
최소 유치 고객 수까지 계산을 마친 후 출력한다.
"""
import sys
sys.stdin = open("1106.txt", "r")
# 입력
C, N = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]
# dp 초기 설정
INF = float('inf')
dp = [INF] * 2001  # 최대값을 넉넉히 해야 함
dp[0] = 0
# dp 계산
for cost, customer in cities:
    for i in range(customer, 2001):
        dp[i] = min(dp[i], dp[i - customer] + cost)
# 출력
print(min(dp[C:]))
