## 평범한 배낭

### 물건 N개. 물건은 (무게 W, 가치 V)

N, K = map(int,input().split())


bag = []


for i in range(N):
  w,v = map(int,input().split())
  bag.append((w,v))

## (1<= K <= 100,000)
dp = [0] * (K+1)

## 무게 : 3 , 가치 : 6 인 물건을 담을지 말지의 여부를 
## 6, 10 / 3,20 / 3,25

## dp[i] -> i만큼의 무게가 담길때의 최댓값
## dp[3] = max(dp[3], dp[0] + v)

for mat in bag:
  w, v = mat[0],mat[1]
  for i in range(K,w-1,-1):
    ## 뒤에서부터 순회
      dp[i] = max(dp[i], dp[i-w] + v)


print(dp[K])
