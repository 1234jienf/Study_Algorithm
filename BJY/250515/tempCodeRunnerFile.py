##어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 제곱수는 정수의 제곱이다. 
## min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

import math


Mn,Mx = map(int,input().split())

size = Mx - Mn + 1
lst = [True] * size

## 2부터 Mx의 루트 까지 반복
limit = int(math.isqrt(Mx))
for i in range(2,limit+1):
  sq = i * i
  start = (Mn + sq - 1 )// sq * sq

  for multiple in range(start,Mx+1, sq):
    lst[multiple - Mn] = False

print(sum(lst))