# 문제
## 1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고,
## 마신 후에는 원래 위치에 다시 놓아야 한다.
## 2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

## 1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고,
## 각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때,
## 효주를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오. 

# 입력
## 첫째 줄에 포도주 잔의 개수 n이 주어진다.
## 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다
## 포도주의 양은 1,000 이하의 음이 아닌 정수이다.


# 출력
## 첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.
n = int(input())

# wine = []
# for i in range(n):
#     wine.append(int(input()))

# ans = 0
# total = 0
# total1 = 0
# total2 = 0
# # 1.
# for i in range(n):
#     if (i+1) % 3 != 1:
#         total += wine[i]
#     if (i+1) % 3 != 2:
#         total1 += wine[i]
#     if (i+1) % 3 != 0:
#         total2 += wine[i]

# ans = max(total,total1,total2)
# print(ans)

wine = [0] * 10000
dp = [0] * 10000
for i in range(n):
    wine.append(int(input()))
    
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[2] + wine[0], wine[2]+wine[1], dp[1])

for i in range(3,n):
    dp[i] = max(wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3], dp[i-1])
    
print(max(dp))
