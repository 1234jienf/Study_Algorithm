N = int(input())
K = int(input())
num_list = list(map(int,input().split()))
# 집중국의 개수가 더 많으면 그냥 다 놓기때문에 0 처리
if K >= N:
    print(0)
# 외의 경우
else:
    # 중복된 개수를 체크하는 변수
    cnt = 0
    # 기지국 정렬
    num_list.sort()
    # 기지국들 거리를 체크할 리스트
    answer_list = []
    # 기지국 반복문 진행
    for i in range(1,N):
        # 앞뒤값을 비교하므로 그 값이 다른 경우 체크
        if num_list[i] != num_list[i-1]:
            # 정답 리스트에 추가
            answer_list.append(num_list[i]-num_list[i-1])
        # 같은경우 cnt 값 추가
        else:
            cnt += 1
    # 앞뒤 거리를 계산한리스트 정렬
    answer_list.sort()
    # N개의 기지국에서 K 개의 기지국을 빼준 범위값만큼 구함 => 결국 차가 큰부분에 집중국을 설치하기 때문에
    print(sum(answer_list[:N-cnt-K]))