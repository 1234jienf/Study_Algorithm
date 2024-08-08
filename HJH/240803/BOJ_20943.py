# 다른 기울기가 몇개인지 확인하면 된다. 동일한 직선은 없다고 했으니 c는 고려할 필요가 없다.
# 기울기는 분수로 표현하며, 기울기를 키, 갯수를 값으로 map을 만들어 사용한다.
# 기울기의 값은 서로소인 두 숫자인 값을 튜플에 넣음으로 표현한다. (물론 분자 분모 순서는 뭐가 먼저오든 상관은 없다)
# 예) (1, 2) -> 1/2, (3, 1) -> 3
# 여기서 서로소를 구하기 위해 유클리드 호제법을 통해 최대공약수를 구해준다.
import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

def euclidean(a: int, b: int) -> int:
    c = a % b
    while c != 0:
        a, b = b, c
        c = a % b
    return b

counter = defaultdict(int)
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == 0:
        counter[(0, 0)] += 1
    elif b == 0:
        # 무한대라는 특별한 표시로 분모가 0 인 분수를 넣어준다.
        counter[(1, 0)] += 1
    else:
        gdc = euclidean(a, b)
        counter[(a//gdc, b//gdc)] += 1

ans = 0
lineNum = 0
for num in counter.values():
    ans += lineNum * num
    lineNum += num

print(ans)