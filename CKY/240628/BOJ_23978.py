N, K = map(int,input().split())

days = list(map(int,input().split()))
# 시작 값
start = 1
# 끝 값 구하고자 하는 돈
end = K
# 이분 탐색
while start <= end:
    # 돈의 총합 계산
    total = 0
    # 중앙 값
    cost = (start + end)//2
    # 일수 만큼 반복문 진행
    for i in range(1,N):
        # 일수 차이가 얼마나 나는지 체크하는 변수
        check = days[i] - days[i-1] -1
        # 중앙 값이 일수 차이보다 작은경우 중앙값은 무조건 1까지 내려가기 때문에 N 부터 1 까지 합 공식 적용
        if cost <= check:
            total += cost * (cost+1) // 2
        # 중앙 값이 일수 차이보다 큰 경우 M 부터 N 까지 값을 구하는 공식 적용
        else:
            total += (cost+(cost-check)) * (cost-(cost-check)+1) // 2
    # 반복문이 끝난 후 마지막 값에 대해서 N 부터 1 까지 공식 적용
    else:
        total += cost * (cost+1) // 2
    # 더한 값이 K 값보다 크거나 같은지 체크
    # 큰 경우 end 값을 갱신하여 값의 범위를 줄임
    if total >= K:
        end = cost - 1
    # 작은 경우 start 값을 높여 값을 높임
    else:
        start = cost + 1
print(start)