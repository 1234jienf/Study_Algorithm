N,S = map(int,input().split())
numList = list(map(int,input().split()))

left = 0
right = 0
# 누적합 구하는 변수
total = 0
# 최소 길이 측정
minLength = 10**9
# right 값이 끝에 도달할때까지
while right < N:
    # right 인덱스를 계속해서 더해나감
    total += numList[right]
    # 합이 S보다 크거나 같아지는 경우
    if total >= S:
        # S값보다 작아질때까지 left 값 더해나감
        while total >= S:
            # right - left 길이 체크
            check = right - left
            # 최소 길이가 더 큰경우 갱신
            if minLength > check:
                minLength = check
            # 합에서 left 뺴고 left 1 증가
            total -= numList[left]
            left += 1
    right += 1

# 최소 길이가 초기값인 경우 0 출력 외에는 minLength에서 +1 해줌
if minLength == 10**9:
    print(0)
else:
    print(minLength+1)