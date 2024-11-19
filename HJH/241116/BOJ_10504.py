import sys
input = sys.stdin.readline

def getSum(num):
    return num * (num + 1) // 2

t = int(input())
for _ in range(t):
    target = int(input())
    # 연속된 수의 갯수 nums. 문제 조건에 따라 최소 2부터 시작한다.
    # 길이를 늘려주며 검사
    nums = 2
    ans = None
    while True:
        if ans != None and len(ans) < nums:
            break
        # 연속된 수의 합이 구하려는 수보다 커질 때 break
        s = getSum(nums)
        if s > target:
            break
        # offset을 구한다.
        offset = target - s
        # 갯수가 나누어떨어지지 않으면
        if offset % nums != 0:
            nums += 1
            continue
        else:
            if ans == None:
                ans = f'{target} = {" + ".join(map(str, list(range(offset // nums + 1, offset // nums + nums + 1))))}'
            else:
                offset = f'{target} = {" + ".join(map(str, list(range(offset // nums + 1, offset // nums + nums + 1))))}'
                ans = ans if len(ans) < len(offset) else offset
        nums += 1
    if ans == None:
        print('IMPOSSIBLE')
    else:
        print(ans)

# 15의 경우
# 2개로 표현 시, 7, 8 -> 6 + 1, 6 + 2
# 3개로 표현 시, 4, 5, 6 -> 3 + 1, 3 + 2, 3 + 3
# 5개로 표현 시, 1, 2, 3, 4, 5 -> 0 + 1, 0 + 2, 0 + 3, 0 + 4, 0 + 5

# 15의 경우를 n 개로 표현할 때
# offset을 o라고 하면
# o + 1, o + 2, ..., o + n
# o * n + (1부터 n까지의 합)으로 표현 가능

# 그러므로 3개로 표현 가능한가? 가 궁금할 땐, 1 부터 3의 합을 먼저 15에서 빼준다. 15 - 3 = 9
# 9가 3으로 나누어떨어진다면 표현이 가능한 것. 9 / 3 = 3
# 몫 3이 오프셋이 된다
# 3 + 1, 3 + 2, 3 + 3 -> 4, 5, 6이 답이 될 가능성을 가진다.