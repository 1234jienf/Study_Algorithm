# 문제
## 영일 코인의 발행자인 효석이는 무한개의 영일 코인을 보유하고 있고, 가격을 마음대로 조절할 수 있다.

## 어느 날, 현금이 필요해진 효석이는 영일 코인을 매도하여 K원 이상을 현금화하려고 한다.

## 효석이는 자신이 정한 N개의 날짜에 코인의 가격을 급상승시키고, 
## 처음 코인의 가격이 오른 날부터 매일 한 개씩 매도할 계획이다. 
## 효석이가 정한 날짜에 영일 코인은 X원으로 오르고, 그 후 0원이 될 때까지 하루에 1원씩 가격이 낮아진다. 
## 코인의 가격이 너무 크게 오르면 의심을 살 수 있기 때문에, 최소 금액으로 상승시켜 현금화를 하려고 한다.

## 효석이를 도와 K원 이상 현금화할 수 있는 가장 작은 정수 X를 구해보자.

# 입력
## 첫째 줄에 두 정수 N, K가 주어진다. (1 ≤ N ≤ 106, 1 ≤ K ≤ 1018)

## 둘째 줄에 효석이가 정한 N개의 날짜 A1, ..., An이 오름차순으로 주어진다. 
## 코인의 가격은 현재로부터 Ai일 뒤에 상승한다. (1 ≤ Ai ≤ 109)

# 출력
## 마지막 가격 상승 이후 코인의 가격이 0이 될 때까지 K원 이상 현금화할 수 있는 가장 작은 정수 X를 출력한다.
def is_valid(X, days, K):
    total = 0
    for i in range(len(days)):
        price = X
        total += price
        if i != len(days) -1:
          for j in range(days[i] + 1, days[i+1]):
              price -= 1
              if price > 0:
                  total += price
              if total >= K:
                  return True
        else :
            while total < K:
                price -= 1
                if price > 0:
                  total += price
            return True
            
    return total >= K

def find_min_X(N, K, days):
    left, right = 1, K
    result = K
    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid, days, K):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

# 입력 처리
N, K = map(int, input().split())
days = list(map(int, input().split()))

# 결과 출력
print(find_min_X(N, K, days))
