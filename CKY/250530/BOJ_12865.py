import sys

input = sys.stdin.readline

N, K = map(int,input().split())
# 가방
bag = []
# weight, value 값 가방에 저장
for _ in range(N):
    weight, value = map(int,input().split())
    bag.append((weight,value))
# dp 값을 K(무게) +1 만큼 생성
dp = [0] * 100001
# N개의 물건 개수만큼 반복
for i in range(N):
    # weight, value 값 분해
    w, v = bag[i]
    # 끝에서부터 반복문 진행
    for j in range(K,w-1,-1):
        # 이미 가방에 값이 있는경우 그 값과 그 값에서 weight 뺀 무게 + value 값중 큰 값으로 갱신
        # 여기서 끝에서부터가 아닌 weight 값부터 시작할 경우 의도치 않은 갱신이 발생하기 때문에 큰값에서 -1 씩 해나감
        dp[j] = max(dp[j], dp[j-w]+v)

print(dp[K])