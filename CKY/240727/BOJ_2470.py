N = int(input())

bottle_list = list(map(int,input().split()))

bottle_list.sort()

left = 0
right = N-1
# 정답 범위
ans = (0,0)
# 목표값 초기설정
target = 10**11
# 왼쪽 시작값이 마이너스인지
l_flag = 0
# 오른쪽 시작값이 마이너스인지
r_flag = 0

# 시작값이 마이너스면 l_flag 1로
if bottle_list[left] < 0:
    l_flag = 1
# 시작값이 마이너스면 r_flag 1로
if bottle_list[right] < 0:
    r_flag = 1
# 둘다 시작값이 마이너스면 오른쪽 첫값 둘째값 합이 제일 적음
if l_flag == 1 and r_flag == 1:
    print(bottle_list[right-1], bottle_list[right])
# 둘다 시작값이 양수면 왼쪽두개의 값이 제일 작음
elif l_flag == 0 and r_flag == 0:
    print(bottle_list[left], bottle_list[left+1])
# 외의 경우 투포인터
else:
    while left < right:
        # 양 끝값의 합을 구함
        check = bottle_list[right] + bottle_list[left]
        # 기존의 초기값에 절대값을 씌운 후 계산한 값도 절대값을 씌움
        value_1 = abs(target)
        value_2 = abs(check)
        # 만약 기존의 값이 계산 값보다 큰 경우
        if value_1 > value_2:
            # 계산 값을 갱신 후 용액 저장
            target = check
            ans = (bottle_list[left],bottle_list[right])
        # 기존의 값들의 절대값을 비교해 오른쪽이 크면 오른쪽 값을 -1 아니면 왼쪽값 +1
        if abs(bottle_list[left]) < abs(bottle_list[right]):
            right -= 1
        else:
            left += 1
print(*ans)